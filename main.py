# run.py
import uvicorn
from dotenv import load_dotenv
from alembic import command
from alembic.config import Config


def run_migrations() -> None:
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


def main() -> None:
    load_dotenv()
    run_migrations()

    uvicorn.run(
        "src.api.app:app",
        host="0.0.0.0",
        port=8080,
        reload=False,
    )


if __name__ == "__main__":
    main()