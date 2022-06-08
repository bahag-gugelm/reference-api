from fastapi import APIRouter, Depends
from app.models.reference import IcecatIndex
from app.utils.dependencies import verify_token

router = APIRouter()


@router.get('/sku_ean')
async def lookup(sku: str, brand: str, dependencies=Depends(verify_token)):
    resp = await IcecatIndex.objects.get_or_none(sku=sku, brand=brand)
    if resp:
        return resp
    else:
        return None