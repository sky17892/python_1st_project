from datetime import datetime
from sqlalchemy import Sequence
from aismartfarm import db

class Member(db.Model):
    __tablename__ = 'member'

    mem_no = db.Column(
        db.Integer,
        Sequence('MEM_NO'),
        primary_key=True, autoincrement=True
    )
    mem_name = db.Column(db.String(50))
    mem_email = db.Column(db.String(100), unique=True)
    mem_password = db.Column(db.String(200))
    mem_phone = db.Column(db.String(20))
    join_date = db.Column(db.DateTime, default=datetime.utcnow())

class FarmInfo(db.Model):
    __tablename__ = 'farm_info'

    survey_year = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(40), primary_key=True)
    farm_num = db.Column(db.Integer, primary_key=True)

    district = db.Column(db.String(40))
    city = db.Column(db.String(40))

class Environment(db.Model):
    __tablename__ = 'environment'

    survey_year = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(40), primary_key=True)
    farm_num = db.Column(db.Integer, primary_key=True)
    measure_time = db.Column(db.DateTime, primary_key=True)

    district = db.Column(db.String(50))
    city = db.Column(db.String(50))

    harvest_part = db.Column(db.Integer)

    out_temp = db.Column(db.Float)
    out_wind_direction = db.Column(db.Integer)
    out_wind_speed = db.Column(db.Float)

    solar_radiation = db.Column(db.Integer)
    solar_radiation_sum = db.Column(db.Integer)

    rain = db.Column(db.Integer)

    inside_temp = db.Column(db.Float)
    humidity = db.Column(db.Float)
    carbon_dioxide = db.Column(db.Integer)
    soil_temp = db.Column(db.Float)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['survey_year', 'item', 'farm_num'],
            ['farm_info.survey_year', 'farm_info.item', 'farm_info.farm_num'],
            ondelete='CASCADE'
        ),
    )

class GrowthData(db.Model):
    __tablename__ = 'growth_data'

    survey_year = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(40), primary_key=True)
    farm_num = db.Column(db.Integer, primary_key=True)
    measure_time = db.Column(db.DateTime, primary_key=True)
    plant_num = db.Column(db.Integer, primary_key=True)

    district = db.Column(db.String(40))
    city = db.Column(db.String(40))

    harvest_part = db.Column(db.Integer)
    branch_num = db.Column(db.Integer)

    plant_height = db.Column(db.Float)
    growth_length = db.Column(db.Float)

    leaf_count = db.Column(db.Integer)
    leaf_length = db.Column(db.Float)
    leaf_width = db.Column(db.Float)

    branch_width = db.Column(db.Float)
    cluster_height = db.Column(db.Float)

    blooming_width = db.Column(db.Integer)
    fruits_width = db.Column(db.Integer)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['survey_year', 'item', 'farm_num'],
            ['farm_info.survey_year', 'farm_info.item', 'farm_info.farm_num'],
            ondelete='CASCADE'
        ),
    )

class ProductionDataRaw(db.Model):
    __tablename__ = 'production_data_raw'

    shipment_id = db.Column(db.Integer, primary_key=True)

    survey_year = db.Column(db.Integer, nullable=False)
    item = db.Column(db.String(40), nullable=False)
    farm_num = db.Column(db.Integer, nullable=False)

    shipment_date = db.Column(db.DateTime, nullable=False)

    total_quantity = db.Column(db.Float)
    total_sales = db.Column(db.Integer)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['survey_year', 'item', 'farm_num'],
            ['farm_info.survey_year', 'farm_info.item', 'farm_info.farm_num']
        ),
    )

class ProductionData(db.Model):
    __tablename__ = 'production_data'

    shipment_id = db.Column(db.Integer, primary_key=True)

    survey_year = db.Column(db.Integer, nullable=False)
    item = db.Column(db.String(40), nullable=False)
    farm_num = db.Column(db.Integer, nullable=False)

    district = db.Column(db.String(50))
    city = db.Column(db.String(50))

    production_date = db.Column(db.DateTime, nullable=False)

    total_quantity = db.Column(db.Float)
    total_sales = db.Column(db.Integer)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['survey_year', 'item', 'farm_num'],
            ['farm_info.survey_year', 'farm_info.item', 'farm_info.farm_num']
        ),
    )

class ProductionDataDaily(db.Model):
    __tablename__ = 'production_data_daily'

    survey_year = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(40), primary_key=True)
    farm_num = db.Column(db.Integer, primary_key=True)
    shipment_date = db.Column(db.DateTime, primary_key=True)

    total_quantity = db.Column(db.Float)
    total_sales = db.Column(db.Integer)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['survey_year', 'item', 'farm_num'],
            ['farm_info.survey_year', 'farm_info.item', 'farm_info.farm_num']
        ),
    )

class CultivationInfo(db.Model):
    __tablename__ = 'cultivation_info'

    survey_year = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(40), primary_key=True)
    farm_num = db.Column(db.Integer, primary_key=True)

    seq_no = db.Column(db.Integer)

    harvest_part = db.Column(db.Integer)
    district = db.Column(db.String(50))
    city = db.Column(db.String(50))

    greenhouse_type = db.Column(db.String(50))
    greenhouse_form = db.Column(db.String(50))

    total_area = db.Column(db.Float)
    planting_area = db.Column(db.Float)
    planting_density = db.Column(db.Float)

    planting_date = db.Column(db.DateTime)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['survey_year', 'item', 'farm_num'],
            ['farm_info.survey_year', 'farm_info.item', 'farm_info.farm_num']
        ),
    )

class CultivationVariety(db.Model):
    __tablename__ = 'cultivation_variety'

    survey_year = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(40), primary_key=True)
    farm_num = db.Column(db.Integer, primary_key=True)
    variety = db.Column(db.String(50), primary_key=True)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['survey_year', 'item', 'farm_num'],
            ['cultivation_info.survey_year', 'cultivation_info.item', 'cultivation_info.farm_num']
        ),
    )

class ItemVariety(db.Model):
    __tablename__ = 'item_variety'

    variety_id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(40), nullable=False)
    variety_name = db.Column(db.String(40), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('item', 'variety_name', name='item_variety_uq'),
    )