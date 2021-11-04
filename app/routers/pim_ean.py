from fastapi import APIRouter, Depends

from app.models.reference import PimEan

from app.utils.dependencies import verify_token


router = APIRouter()


@router.get('/pim_ean/{ean}')
async def lookup(ean: str, dependencies=Depends(verify_token)):
    item = await PimEan.objects.get_or_none(ean=ean)
    return item
    
