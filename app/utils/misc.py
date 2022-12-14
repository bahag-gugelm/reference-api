from app.models.reference import PimQuery20_5

async def get_q205(query: str):
    if len(query) == 13:
        return  await PimQuery20_5.objects.get_or_none(EAN=query.lstrip('0'))
    else:
        return await PimQuery20_5.objects.get_or_none(Variant_product=query)
