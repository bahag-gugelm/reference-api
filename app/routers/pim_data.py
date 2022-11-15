from fastapi import APIRouter, Depends

from app.models.reference import PimQuery20_5, PimQuery29

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


@router.get('/product/{ean}')
async def get_product_info(ean: str, dependencies=Depends(verify_token)):
    attribs_exclude_fields = {
            'id', 'Material_group', 'Variant_product',
            'Mandators', 'SAP_name',
            }
    res205 = ean and await PimQuery20_5.objects.get_or_none(EAN=ean)
    res = res205 and res205.dict()
    if res:
        res29 = await PimQuery29.objects.all(Variant_product=res['Variant_product'])
        res['Attributes'] = [item.dict(exclude=attribs_exclude_fields) for item in res29]
        return res