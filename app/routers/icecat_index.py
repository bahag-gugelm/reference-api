from fastapi import APIRouter, Depends
from app.models.reference import IcecatSKU, IcecatEAN
from app.utils.dependencies import verify_token
import json

router = APIRouter()


@router.get('/sku_ean')
async def lookup(sku: str, brand: str, dependencies=Depends(verify_token)):
    sku_resp = await IcecatSKU.objects.get_or_none(sku=sku, brand=brand)
    if sku_resp:
        icecat_id = json.loads(sku_resp.json()).get("id")
        ean_resp = await IcecatEAN.objects.all(id=icecat_id)
        return ean_resp
    else:
        return None
