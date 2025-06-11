from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:ac040487@localhost:3306/WarehouseTesting")

meta = MetaData()
conn = engine.connect()
