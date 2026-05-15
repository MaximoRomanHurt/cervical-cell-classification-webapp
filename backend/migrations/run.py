"""
Punto de entrada de la aplicación Flask.
Uso:
  python run.py                         # Modo development
  FLASK_ENV=production python run.py    # Modo production
"""
import os
from app import create_app

config_name = os.getenv("FLASK_ENV", "development")
app = create_app(config_name)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    print(f"\n🔬 CervixAI API running on http://localhost:{port}")
    print(f"📋 Environment : {config_name}")
    print(f"📖 API Prefix  : /api/v1\n")
    app.run(host="0.0.0.0", port=port)