#! /bin/bash
set -a
source .env
set +a

echo "Running cleanup script..."
python3 clear_jobs.py

echo "Running scraper..."
python3 JobScraper.py

echo "Importing csv to MongoDB..."
mongoimport --uri "mongodb+srv://JuneWay:$MONGO_PWD@ethanc.qgevd.mongodb.net/JobDB" \
    --collection jobs \
    --type csv \
    --file Data_Science_Internship_Full.csv \
    --headerline

echo "Running location encoder script..."
python3 latlong_US.py