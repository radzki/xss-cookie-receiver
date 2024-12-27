from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import SessionLocal, PayloadModel

app = FastAPI()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for the request
class Payload(BaseModel):
    data: str

@app.post("/rcv")
async def receive_data(payload: Payload, db: Session = Depends(get_db)):
    # Save to database
    db_payload = PayloadModel(data=payload.data)
    db.add(db_payload)
    db.commit()
    db.refresh(db_payload)
    return {"data_received": True, "id": db_payload.id}

@app.get("/payloads")
async def get_payloads(db: Session = Depends(get_db)):
    payloads = db.query(PayloadModel).all()
    return {"payloads": [{"id": p.id, "data": p.data} for p in payloads]}

@app.post("/clear-payloads")
async def clear_payloads(db: Session = Depends(get_db)):
    """Delete all entries in the payloads table."""
    db.query(PayloadModel).delete()
    db.commit()
    return {"message": "All payloads have been cleared."}