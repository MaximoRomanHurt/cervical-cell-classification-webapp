"""
Blueprint: Health Check
Endpoints: GET /api/v1/health/ping   -> Verifica que la API está activa
           GET /api/v1/health/db     -> Verifica la conexión a MySQL
"""
from flask import Blueprint, jsonify
from datetime import datetime

health_bp = Blueprint("health", __name__)


@health_bp.get("/ping")
def ping():
    """Endpoint de health check básico. Siempre debe responder 200."""
    return jsonify({
        "status":  "ok",
        "message": "CervixAI API is running",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat()
    }), 200


@health_bp.get("/db")
def db_check():
    """Verifica la conexión a la base de datos MySQL."""
    # TODO: Implementar verificación real de conexión en Fase 2
    return jsonify({"status": "not_implemented", "message": "DB check pending"}), 200