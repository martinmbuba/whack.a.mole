import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

from app import Base
from app.models import *  # import all models so Alembic can detect them

# Load .env file
load_dotenv()

# This is the Alembic Config object, which provides access to the .ini values
config = context.config

# --- Database URL setup ---
# Try DATABASE_URL first
database_url = os.getenv("DATABASE_URL")

# If not found, build from individual env vars
if not database_url:
    driver = os.getenv("DB_DRIVER", "postgresql+psycopg")
    user = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    db = os.getenv("DB_NAME")

    database_url = f"{driver}://{user}:{password}@{host}:{port}/{db}"

# Override sqlalchemy.url in alembic.ini
config.set_main_option("sqlalchemy.url", database_url)

# --- Logging setup ---
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata for autogenerate (from models)
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
