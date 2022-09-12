from fastapi import APIRouter, Depends
from app.models.reference import IcecatIndex, PimQuery20_5
from app.utils.dependencies import verify_token
import json

router = APIRouter()


@router.get('/sku_ean')
async def lookup(sku: str, brand: str, dependencies=Depends(verify_token)):
    sku_resp = await IcecatIndex.objects.all(sku=sku, brand=brand)
    response=[]
    if sku_resp:
        for item in sku_resp:
            item = json.loads(item.json())
            ean = item.get("ean")
            if len(ean)>=10:
                ean = ean.zfill(13)
                resp =  await PimQuery20_5.objects.all(EAN=ean)
                if resp:
                    resp = json.loads(resp[0].json())
                    resp = {
                        "EAN": resp.get("EAN"),
                        "Variant_product":resp.get("Variant_product"),
                        "Base_product": resp.get("Base_product"),
                        "Material_group": resp.get("Material_group"),
                        "SKU": sku,
                        "brand": brand
                    }
                    response.append(resp)
                else:
                    response.append({
                        "EAN": ean,
                        "Variant_product": None,
                        "Base_product": None,
                        "Material_group": None,
                        "SKU": sku,
                        "brand": brand
                    })
    return response