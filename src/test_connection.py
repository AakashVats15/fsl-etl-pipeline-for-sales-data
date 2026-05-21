from sqlalchemy import create_engine

engine = create_engine("postgresql+pg8000://postgres:1234@localhost:5432/salesdb")
conn = engine.connect()
print("Connected!")