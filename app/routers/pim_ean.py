from fastapi import APIRouter, Depends

from app.models.reference import PimQuery20_5

from app.utils.dependencies import verify_token


router = APIRouter()


@router.get('/pim_ean/{query}')
async def lookup(query: str, dependencies=Depends(verify_token)):
    if len(query) == 13:
        resp =  await PimQuery20_5.objects.get_or_none(EAN=query)
    else:
        resp = await PimQuery20_5.objects.get_or_none(Variant_product=query)

    if resp:
        return {
            'variant_product': resp.Variant_product,
            'base_product': resp.Base_product,
            'material_group': resp.Material_group.split(' - ')[0],
            'ean': resp.EAN,
        }
