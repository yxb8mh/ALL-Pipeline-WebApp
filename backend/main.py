from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()
mongo_pwd = os.getenv("MONGO_PWD")

app = FastAPI()
client = MongoClient(f"mongodb+srv://JuneWay:{mongo_pwd}@ethanc.qgevd.mongodb.net/")
db = client['JobDB']
collection = db['jobs']

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return {"mysterious man": "Welcome to the Job Data API landing page! Type '/api/jobs' to get the latest scraped job data!"}

@app.get('/api/jobs')
def get_jobs():
    jobs = list(collection.find({},{"_id": 0}))
    return jobs