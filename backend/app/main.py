
from fastapi import FastAPI
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
app = FastAPI()
@app.get("/")
async def read_root():
    return {"message": "Bienvenue sur OracleIA !"}

# Création des tables dans Supabase si elles n'existent pas encore
Base.metadata.create_all(bind=engine)

@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    """ Vérifie si FastAPI arrive à se connecter à PostgreSQL """
    return {"message": "Connexion réussie avec Supabase ✅"}
