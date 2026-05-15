"""
Configuración por entornos: Development | Testing | Production.
Las variables sensibles se leen desde el archivo .env.
"""
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Configuración base compartida por todos los entornos."""
    SECRET_KEY: str                = os.getenv("SECRET_KEY", "change-me-in-production")
    JWT_SECRET_KEY: str            = os.getenv("JWT_SECRET_KEY", "jwt-secret-key")
    JWT_ACCESS_TOKEN_EXPIRES       = timedelta(hours=8)
    JWT_REFRESH_TOKEN_EXPIRES      = timedelta(days=30)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS      = {"pool_pre_ping": True}

    UPLOAD_FOLDER: str             = os.getenv("UPLOAD_FOLDER", "uploads/temp")
    PROCESSED_FOLDER: str          = os.getenv("PROCESSED_FOLDER", "uploads/processed")
    MAX_CONTENT_LENGTH: int        = 16 * 1024 * 1024          # 16 MB máximo por imagen
    ALLOWED_EXTENSIONS: set        = {"jpg", "jpeg", "png", "tiff", "bmp"}

    # Futuro: endpoint del microservicio de IA
    AI_SERVICE_URL: str            = os.getenv("AI_SERVICE_URL", "http://ai-service:5001")
    AI_SERVICE_TIMEOUT: int        = 30


class DevelopmentConfig(BaseConfig):
    """Entorno de desarrollo local."""
    DEBUG         = True
    TESTING       = False
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:root@localhost:3306/cervixai_dev"
    )
    CORS_ORIGINS  = ["http://localhost:4200"]


class TestingConfig(BaseConfig):
    """Entorno de pruebas automatizadas (usa SQLite en memoria)."""
    DEBUG         = False
    TESTING       = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    CORS_ORIGINS  = ["*"]


class ProductionConfig(BaseConfig):
    """Entorno de producción."""
    DEBUG         = False
    TESTING       = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "")
    CORS_ORIGINS  = os.getenv("CORS_ORIGINS", "https://cervixai.example.com").split(",")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)


# Mapa de entornos: usado en create_app()
config_map = {
    "development": DevelopmentConfig,
    "testing":     TestingConfig,
    "production":  ProductionConfig,
}