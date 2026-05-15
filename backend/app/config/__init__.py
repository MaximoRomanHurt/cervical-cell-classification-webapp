"""
CervixAI - Aplicativo Web de Clasificación Citológica Cervical
Inicialización de la aplicación Flask con factory pattern.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()


def create_app(config_name: str = "development") -> Flask:
    """
    Application Factory Pattern.
    Permite instanciar la app con diferentes configuraciones
    (development, testing, production).
    """
    app = Flask(__name__)

    # Cargar configuración según el entorno
    from app.config.settings import config_map
    app.config.from_object(config_map[config_name])

    # Inicializar extensiones
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    CORS(app, resources={r"/api/*": {"origins": app.config.get("CORS_ORIGINS", "*")}})

    # Registrar Blueprints (rutas)
    from app.routes.auth_routes import auth_bp
    from app.routes.classification_routes import classification_bp
    from app.routes.history_routes import history_bp
    from app.routes.health_routes import health_bp

    app.register_blueprint(auth_bp,            url_prefix="/api/v1/auth")
    app.register_blueprint(classification_bp,  url_prefix="/api/v1/classification")
    app.register_blueprint(history_bp,         url_prefix="/api/v1/history")
    app.register_blueprint(health_bp,          url_prefix="/api/v1/health")

    return app