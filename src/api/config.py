"""Seleção da engine de banco (SQLite ou PostgreSQL) com base em USE_SQLITE."""

from src.infra.config.engine import CreateEngine
from src.infra.config.url_connections import SQLiteUrlConnetion, PostgresUrlConnection
import os
from dotenv import load_dotenv

load_dotenv()
if os.getenv("USE_SQLITE") == "1":
    ENGINE = CreateEngine.create(SQLiteUrlConnetion)
else:
    ENGINE = CreateEngine.create(PostgresUrlConnection)