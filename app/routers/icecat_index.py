from fastapi import APIRouter, Depends
from app.models.reference import IcecatSKU, IcecatEAN, IcecatIndex
from app.utils.dependencies import verify_token
import json

router = APIRouter()


@router.get('/sku_ean')
async def lookup(sku: str, brand: str, dependencies=Depends(verify_token)):
    sku_resp = await IcecatIndex.objects.all(sku=sku, brand=brand)
    return sku_resp
