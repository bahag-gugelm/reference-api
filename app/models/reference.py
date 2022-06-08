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
    

class PimQuery20_5(ormar.Model):
    class Meta(BaseMeta):
        tablename = "PIM_aktuell_Query20_5_DE_view"

    id = ormar.Integer(primary_key=True)
    Variant_product = ormar.String(max_length=15)
    Base_product = ormar.String(max_length=9)		
    EAN = ormar.String(max_length=13)
    Product_name = ormar.String(max_length=400)		
    SAP_name = ormar.String(max_length=120)	
    Mandators = ormar.String(max_length=90)
    Suppliers = ormar.String(max_length=350)
    Main_material_group = ormar.String(max_length=1)	
    KSP = ormar.String(max_length=2)	
    Material_group_subgroup = ormar.String(max_length=5)
    Material_group_node = ormar.String(max_length=5)
    Material_group = ormar.String(max_length=75)
    SAP_status = ormar.String(max_length=13)
    Approval = ormar.String(max_length=12)
    Status_data_maintenance = ormar.String(max_length=35)
    Flag_status = ormar.String(max_length=12)
    Online_reservation = ormar.String(max_length=3)
    Maintenance_classification = ormar.String(max_length=2)
    Processed_by_tool = ormar.String(max_length=5)
    Initial_responsibility = ormar.String(max_length=20)
    General_responsibility = ormar.String(max_length=20)
    Private_brand___brand = ormar.String(max_length=50)
    Product_line = ormar.String(max_length=50)
    Product_name_category = ormar.String(max_length=50)
    Type_designation = ormar.String(max_length=80)
    Description = ormar.String(max_length=10000)
    USP_1 = ormar.String(max_length=110)
    USP_2 = ormar.String(max_length=110)
    USP_3 = ormar.String(max_length=110)
    USP_4 = ormar.String(max_length=110)
    USP_5 = ormar.String(max_length=110)
    Name_attributes = ormar.String(max_length=125)
    Primary_frontend_category = ormar.String(max_length=8)
    Secondary_frontend_categories = ormar.String(max_length=110)
    Count_available_images = ormar.String(max_length=5)
    Count_active_images = ormar.String(max_length=5)
    URL_main_image = ormar.String(max_length=100)
    AM_SystemCreated = ormar.DateTime()
    AM_SystemModified = ormar.DateTime()
    AM_ExcelFileWithPath = ormar.String(max_length=500)


class PimQuery29(ormar.Model):
    class Meta(BaseMeta):
        tablename = "PIM_akutell_Query29_DE_view"
    
    id = ormar.Integer(primary_key=True)
    Material_group = ormar.String(max_length=60)
    Variant_product = ormar.String(max_length=60)
    Mandators = ormar.String(max_length=33)
    SAP_name = ormar.String(max_length=75)
    Product_name_category = ormar.String(max_length=110)
    Classifying_category = ormar.String(max_length=80)
    Attribute_identifier = ormar.String(max_length=80)
    Attribute_name = ormar.String(max_length=80)
    Attribute_type = ormar.String(max_length=9)
    Value_identifier = ormar.String(max_length=300)
    Value_name = ormar.String(max_length=300)
    Value_unit = ormar.String(max_length=60)
    Value_position = ormar.String(max_length=4)
    Value_language = ormar.String(max_length=35)
    lfd_nr = ormar.Integer()
    AM_SystemCreated = ormar.DateTime()
    AM_SystemModified = ormar.DateTime()
    AM_ExcelFileWithPath = ormar.String(max_length=500)


class IcecatIndex(ormar.Model):
    class Meta(BaseMeta):
        tablename = "icecat_index"

    id = ormar.Integer(primary_key=True)
    sku = ormar.String(max_length=100)
    brand = ormar.String(max_length=100)
    ean = ormar.String(max_length=5000)