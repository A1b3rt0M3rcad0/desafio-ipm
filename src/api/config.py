from src.infra.config.engine import CreateEngine
from src.infra.config.url_connections import SQLiteUrlConnetion

ENGINE = CreateEngine.create(SQLiteUrlConnetion)