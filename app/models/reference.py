import ormar

from app.db import metadata, database



class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class PimEan(ormar.Model):
    class Meta(BaseMeta):
        tablename = "pim_ean"

    id = ormar.Integer(primary_key=True)
    variant_product = ormar.String(max_length=24)
    base_product = ormar.String(max_length=24)
    material_group = ormar.String(max_length=24)
    ean = ormar.String(max_length=24)
    