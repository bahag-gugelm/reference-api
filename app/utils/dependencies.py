from fastapi import Header, HTTPException

from app.core.config import settings



async def verify_token(X_Token: str = Header(...)):
    if X_Token != settings.API_KEY:
        raise HTTPException(status_code=400, detail="X-Token header invalid")
