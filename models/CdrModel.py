from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from providers import get_app, get_db

app = get_app()
db = get_db()

class CdrModel(db.Model):
    __tablename__ = 'cdr'

    id = Column(Integer, primary_key=True)
    call_type = Column(Integer)
    service_code = Column(Integer)
    ne_code = Column(String(255))
    in_route = Column(String(255))
    out_route = Column(String(255))
    imsi = Column(String(255))
    sgsn_address = Column(String(255))
    a_number = Column(String(255))
    b_number = Column(String(255))
    c_number = Column(String(255))
    apn_address = Column(String(255))
    pdp_address = Column(String(255))
    call_date = Column(String(255))
    call_duration = Column(Integer)
    data_volume_inc = Column(Integer)
    data_volume_out = Column(Integer)
    teleservice = Column(String(255))
    bearerservice = Column(String(255))
    camel_flag = Column(String(255))
    camel_service_level = Column(String(255))
    camel_service_key = Column(String(255))
    camel_default_call_handling = Column(String(255))
    camel_server_address = Column(String(255))
    camel_msc_address = Column(String(255))
    camel_call_ref_num = Column(String(255))
    camel_init_cf_indicator = Column(String(255))
    camel_destination_num = Column(String(255))
    camel_modification = Column(String(255))
    supplimentary_num = Column(String(255))
    network_time = Column(String(255))
    reason_for_cleardown = Column(String(255))
    partial_indicator = Column(String(255))
    partial_seq_num = Column(String(255))
    imei_num = Column(String(255))
    chrono_num = Column(String(255))
    charging_id = Column(String(255))
    subscriber_type = Column(String(255))
    