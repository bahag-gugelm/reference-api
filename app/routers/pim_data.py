from fastapi import APIRouter, Depends

from app.models.reference import PimQuery20_5, PimQuery29

from app.utils.dependencies import verify_token
from app.utils.misc import get_q205


router = APIRouter()


@router.get('/pim_ean/{query}')
async def lookup(query: str, dependencies=Depends(verify_token)):
    resp205 = await get_q205(query=query)
    if resp205:
        return {
            'variant_product': resp205.Variant_product,
            'base_product': resp205.Base_product,
            'material_group': resp205.Material_group.split(' - ')[0],
            'ean': resp205.EAN,
        }


@router.get('/product/{query}')
async def get_product_info(query: str, dependencies=Depends(verify_token)):
    attribs_exclude_fields = {
            'id', 'Material_group', 'Variant_product',
            'Mandators', 'SAP_name',
            }
    resp205 = await get_q205(query=query)
    resp205 = resp205 and resp205.dict()
    if resp205:
        res29 = await PimQuery29.objects.all(Variant_product=resp205['Variant_product'])
        resp205['Attributes'] = [item.dict(exclude=attribs_exclude_fields) for item in res29]
        return resp205
