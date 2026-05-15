"""
Modelo Analysis - Representa cada análisis citológico realizado.
Tabla: analyses
"""
from app import db
from datetime import datetime


class Analysis(db.Model):
    """
    Almacena los metadatos de cada clasificación solicitada.
    Los resultados de la IA (label, confidence) se guardan aquí
    una vez el microservicio de IA responda.
    """
    __tablename__ = "analyses"

    id               = db.Column(db.Integer,     primary_key=True)
    user_id          = db.Column(db.Integer,     db.ForeignKey("users.id"), nullable=False)
    original_filename= db.Column(db.String(255), nullable=False)
    stored_filename  = db.Column(db.String(255), nullable=False)   # UUID seguro en disco
    file_path        = db.Column(db.String(500), nullable=False)
    status           = db.Column(db.String(50),  default="pending")
    # status: 'pending' | 'processing' | 'completed' | 'failed'

    # Resultado de la clasificación IA (se completa en fase posterior)
    ai_label         = db.Column(db.String(50),  nullable=True)    # 'Normal' | 'Anormal'
    ai_confidence    = db.Column(db.Float,       nullable=True)    # 0.0 – 1.0
    ai_details       = db.Column(db.JSON,        nullable=True)    # Detalle extendido

    notes            = db.Column(db.Text,        nullable=True)    # Notas del especialista
    created_at       = db.Column(db.DateTime,    default=datetime.utcnow)
    updated_at       = db.Column(db.DateTime,    default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relaciones
    user             = db.relationship("User",   back_populates="analyses")

    def __repr__(self):
        return f"<Analysis id={self.id} status={self.status} label={self.ai_label}>"