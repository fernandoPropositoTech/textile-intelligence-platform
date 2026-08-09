#Lê a URL do banco.
#Cria uma conexão reutilizável.
#echo=True faz o SQL aparecer no terminal, útil para aprendizado.
#Mais tarde mudaremos para False em produção.
from sqlalchemy import create_engine

from app.core.settings import settings


engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)