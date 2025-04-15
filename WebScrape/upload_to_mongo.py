import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()

mongo_pwd = os.getenv("MONGO_PWD")

mongo_uri = f"mongodb+srv://JuneWay:{mongo_pwd}@ethanc.qgevd.mongodb.net/JobDB"

client = MongoClient(mongo_uri)
db = client["JobDB"]
collection = db["jobs"]

csv_file = "Data_Science_Internship_Full.csv"
df = pd.read_csv(csv_file)

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df = df.where(pd.notnull(df), None)

collection.insert_many(df.to_dict(orient="records"))

print(f"Successfully inserted {len(df)} documents from {csv_file} into 'jobs' collection.")
