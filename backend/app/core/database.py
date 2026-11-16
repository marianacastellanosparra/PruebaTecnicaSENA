from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.models import Base


# Crear la conexión con PostgreSQL
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)


# Crear las sesiones de la base de datos
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Obtener una sesión para cada petición
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()