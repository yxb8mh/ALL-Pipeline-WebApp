#! /bin/bash
set -a
source .env
set +a

echo "clearing existing documents in jobs_data collection..."
mongoimport --uri "mongodb+srv://JuneWay:$MONGO_PWD@ethanc.qgevd.mongodb.net/JobDB" \
    --eval "db.jobs_data.deleteMany({})" 
    
echo "Running scraper..."
python3 JobScraper.py

echo "Importing csv to MongoDB..."
mongoimport --uri "mongodb+srv://JuneWay:$MONGO_PWD@ethanc.qgevd.mongodb.net/JobDB" \
    --collection jobs \
    --type csv \
    --file Data_Science_Internship_Full.csv \
    --headerline

echo "Import complete"