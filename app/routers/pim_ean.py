from fastapi import APIRouter, Depends

from app.models.reference import PimEan

from app.utils.dependencies import verify_token


router = APIRouter()


@router.get('/pim_ean/{query}')
async def lookup(query: str, dependencies=Depends(verify_token)):
    if len(query) == 13:
        return await PimEan.objects.get_or_none(ean=query)
    return await PimEan.objects.get_or_none(variant_product=query)
