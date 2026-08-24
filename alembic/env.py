from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from app.core.settings import settings
from app.database.base import Base
from app.models.machine import Machine


# Alembic Config
config = context.config


# Faz o Alembic usar a mesma DATABASE_URL da aplicação
config.set_main_option(
    "sqlalchemy.url",
    settings.DATABASE_URL
)


# Configuração de logs
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# Metadata usada pelo autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Executa migrations sem criar uma conexão direta."""

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
    """Executa migrations usando conexão com o banco."""

    connectable = engine_from_config(
        config.get_section(
            config.config_ini_section,
            {}
        ),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()