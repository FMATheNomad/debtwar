import os
import re
import logging
import asyncpg

logger = logging.getLogger(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")
_pool = None


async def get_pg_connection():
    global _pool
    if not _pool:
        _pool = await asyncpg.create_pool(DATABASE_URL, min_size=1, max_size=10)
    conn = await _pool.acquire()
    return PGWrapper(conn, _pool)


class PGRow:
    def __init__(self, data: dict):
        self._data = data
        self._keys = list(data.keys())

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._data[self._keys[key]] if key < len(self._keys) else None
        return self._data.get(key)

    def __iter__(self):
        return iter(self._data.values())

    def __len__(self):
        return len(self._keys)

    def get(self, key, default=None):
        return self._data.get(key, default)

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def __contains__(self, key):
        return key in self._data


_SQL_REPLACEMENTS = [
    (r"datetime\('now',\s*'localtime'\)", "NOW()"),
    (r"MAX\(\?,\s*", "GREATEST($1, "),
    (r"MAX\(\$1,\s*", "GREATEST($1, "),
    (r"\bMIN\(", "LEAST("),
    (r"changes\(\)", "1"),
    (r"last_insert_rowid\(\)", "lastval()"),
    (r"INSERT OR IGNORE INTO", "INSERT INTO"),
    (r"INSERT OR REPLACE INTO", "INSERT INTO"),
]

_PARAM_RE = re.compile(r"(?<!\w)\?(?!\w)")


def convert_sql(sql: str, params=None):
    for pattern, repl in _SQL_REPLACEMENTS:
        sql = re.sub(pattern, repl, sql, flags=re.IGNORECASE)
    if params and "?" in sql:
        count = 0
        def repl(m):
            nonlocal count
            count += 1
            return f"${count}"
        sql = _PARAM_RE.sub(repl, sql)
    return sql, params


class PGWrapper:
    def __init__(self, conn, pool):
        self._conn = conn
        self._pool = pool

    def execute(self, sql, params=None):
        return PGExec(self._conn, sql, params)

    async def executescript(self, sql):
        for stmt in sql.split(";"):
            stmt = stmt.strip()
            if stmt:
                try:
                    await self._conn.execute(stmt)
                except Exception as e:
                    if "already exists" not in str(e).lower():
                        logger.warning(f"PG script: {e}")

    async def commit(self):
        pass

    async def close(self):
        if self._pool:
            await self._pool.release(self._conn)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass


class PGExec:
    def __init__(self, conn, sql, params):
        self._conn = conn
        self._sql = sql
        self._params = params
        self._rows = None
        self._idx = 0

    def __await__(self):
        return self._run().__await__()

    async def _run(self):
        sql, params = convert_sql(self._sql, self._params)
        try:
            if params:
                await self._conn.execute(sql, *params)
            else:
                await self._conn.execute(sql)
        except Exception as e:
            logger.error(f"PG exec: {sql[:80]} {e}")

    async def __aenter__(self):
        sql, params = convert_sql(self._sql, self._params)
        try:
            if params:
                rows = await self._conn.fetch(sql, *params)
            else:
                rows = await self._conn.fetch(sql)
            self._rows = [PGRow(dict(r)) for r in rows] if rows else []
        except Exception as e:
            logger.error(f"PG query: {sql[:80]} {e}")
            self._rows = []
        return self

    async def __aexit__(self, *args):
        pass

    async def fetchone(self):
        if self._rows and self._idx < len(self._rows):
            r = self._rows[self._idx]
            self._idx += 1
            return r
        return None

    async def fetchall(self):
        r = self._rows or []
        self._rows = None
        return r

    def __aiter__(self):
        return self

    async def __anext__(self):
        r = await self.fetchone()
        if r is None:
            raise StopAsyncIteration
        return r
