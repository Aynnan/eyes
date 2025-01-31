import os
import psycopg2
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("✅ Connexion réussie à PostgreSQL sur Render !")
    conn.close()

except Exception as e:
    print(f"❌ Erreur de connexion : {e}")
