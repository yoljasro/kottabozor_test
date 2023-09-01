import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database file path
DATABASE_URI = 'sqlite:///offers.db'

# Create the database engine and session
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Base model for the offers table
Base = declarative_base()

class Offer(Base):
    __tablename__ = 'offers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    brand = Column(String)
    category = Column(String)
    merchant = Column(String)
    ram = Column(String)
    rom = Column(String)
    image_url = Column(String)

# Download data from the API
url = 'https://www.kattabozor.uz/hh/test/api/v1/offers'
response = requests.get(url)
data = response.json()

# Save data to the database
for offer_data in data['offers']:
    offer = Offer(
        id=offer_data['id'],
        name=offer_data['name'],
        brand=offer_data['brand'],
        category=offer_data['category'],
        merchant=offer_data['merchant'],
        ram=next((attr['value'] for attr in offer_data['attributes'] if attr['name'] == 'RAM'), None),
        rom=next((attr['value'] for attr in offer_data['attributes'] if attr['name'] == 'ROM'), None),
        image_url=offer_data['image']['url']
    )
    session.add(offer)

session.commit()