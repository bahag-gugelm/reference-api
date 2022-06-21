import ormar

from app.db import metadata, database



class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
    

class PimQuery20_5(ormar.Model):
    class Meta(BaseMeta):
        tablename = "PIM_query20_5"

    Variant_product = ormar.String(max_length=15, primary_key=True)
    Base_product = ormar.String(max_length=9, nullable=True)		
    EAN = ormar.String(max_length=13, index=True, nullable=True)
    Product_name = ormar.String(max_length=400, nullable=True)		
    SAP_name = ormar.String(max_length=120, nullable=True)	
    Mandators = ormar.String(max_length=90, nullable=True)
    Suppliers = ormar.String(max_length=350, nullable=True)
    Main_material_group = ormar.String(max_length=1, nullable=True)	
    KSP = ormar.String(max_length=2, nullable=True)	
    Material_group_subgroup = ormar.String(max_length=5, nullable=True)
    Material_group_node = ormar.String(max_length=5, nullable=True)
    Material_group = ormar.String(max_length=75, nullable=True)
    SAP_status = ormar.String(max_length=13, nullable=True)
    Approval = ormar.String(max_length=12, nullable=True)
    Status_data_maintenance = ormar.String(max_length=35, nullable=True)
    Flag_status = ormar.String(max_length=12, nullable=True)
    Online_reservation = ormar.String(max_length=3, nullable=True)
    Maintenance_classification = ormar.String(max_length=2, nullable=True)
    Processed_by_tool = ormar.String(max_length=5, nullable=True)
    Initial_responsibility = ormar.String(max_length=20, nullable=True)
    General_responsibility = ormar.String(max_length=20, nullable=True)
    Private_brand___brand = ormar.String(max_length=50, nullable=True)
    Product_line = ormar.String(max_length=50, nullable=True)
    Product_name_category = ormar.String(max_length=50, nullable=True)
    Type_designation = ormar.String(max_length=80, nullable=True)
    Description = ormar.String(max_length=10000, nullable=True)
    USP_1 = ormar.String(max_length=110, nullable=True)
    USP_2 = ormar.String(max_length=110, nullable=True)
    USP_3 = ormar.String(max_length=110, nullable=True)
    USP_4 = ormar.String(max_length=110, nullable=True)
    USP_5 = ormar.String(max_length=110, nullable=True)
    Name_attributes = ormar.String(max_length=150, nullable=True) # changed from 125 because ftp dumps break the field lenghth
    Primary_frontend_category = ormar.String(max_length=8, nullable=True)
    Secondary_frontend_categories = ormar.String(max_length=150, nullable=True)
    Count_available_images = ormar.String(max_length=5, nullable=True)
    Count_active_images = ormar.String(max_length=5, nullable=True)
    URL_main_image = ormar.String(max_length=100, nullable=True)


class PimQuery29(ormar.Model):
    class Meta(BaseMeta):
        tablename = "PIM_query29"
    
    id = ormar.Integer(primary_key=True)
    Material_group = ormar.String(max_length=60, nullable=True)
    Variant_product = ormar.String(max_length=60, index=True)
    Mandators = ormar.String(max_length=33, nullable=True)
    SAP_name = ormar.String(max_length=75, nullable=True)
    Product_name_category = ormar.String(max_length=110, nullable=True)
    Classifying_category = ormar.String(max_length=80, nullable=True)
    Attribute_identifier = ormar.String(max_length=100, nullable=True)
    Attribute_name = ormar.String(max_length=80, nullable=True)
    Attribute_type = ormar.String(max_length=9, nullable=True)
    Value_identifier = ormar.String(max_length=300, nullable=True)
    Value_name = ormar.String(max_length=2500, nullable=True)
    Value_unit = ormar.String(max_length=60, nullable=True)
    Value_language = ormar.String(max_length=35, nullable=True)


class IcecatIndex(ormar.Model):
    class Meta(BaseMeta):
        tablename = "icecat_index"

    ean = ormar.String(primary_key=True, max_length=13)
    id = ormar.Integer()
    sku = ormar.String(max_length=100)
    brand = ormar.String(max_length=100)