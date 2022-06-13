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
            if len(ean)==13:
                resp =  await PimQuery20_5.objects.all(EAN=ean)
                if resp:
                    resp = json.loads(resp[0].json())
                    resp = {
                        "ean": resp.get("EAN"),
                        "variant_product":resp.get("Variant_product"),
                        "base_product": resp.get("Base_product"),
                        "material_group": resp.get("Material_group"),
                        "sku": sku,
                        "brand": brand
                    }
                    response.append(resp)
                else:
                    response.append({
                        "ean": ean,
                        "variant_product": None,
                        "base_product": None,
                        "material_group": None,
                        "sku": sku,
                        "brand": brand
                    })
    return response