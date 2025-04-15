# Active Learning Lab DScareers Website Pipeline 
<table>
<tr>
<td>
  A dynamic web application that showcases real-time job postings and interactive analytical visualizations. It features an automated data pipeline with scheduled scraping tasks, seamless ingestion into MongoDB, integration with FastAPI deployed via Render, and real-time data rendering through auto-fetched API endpoints via JavaScript.
</td>
</tr>
</table>


## Demo
Here is a working live demo : https://dscareers-ethancao.pythonanywhere.com

## Built with 

- Front End: HTML, CSS, JavaScript
- Back End: Flask, Shell, FastAPI, MongoDB, CORSMiddleware
- Web-scrape & Data Processing: BeautifulSoup4, Requests, Pandas, Numpy
- API: Job-board specific guest API, openstreetmap.org API

## Update Log:
**03/05**
- Optimize webscraping scripts to fully utilize the given guest-api
- Extract as much valuable components from the api as possible
- automate the data pre-processing stage, and export as a csv file
  
**03/19**
- Establish the basic architecture of the website landing page via HTML + CSS
- Write sample article title pages to simulate that of a real website
  
**04/02**
- Establish a basic HTML + CSS structure of the visualization pages, create new endpoints for users to access
- Design the interactive components (via JavaScript) on the visual map that connects to the csv data tables scraped from webscraper
- Create a script that auto-encodes location names from the dataset into geo LAT LONG coordinates
  
**04/16**
- Automate the web-scrape task and connect it with MongoDB via Shell 
- initialize the pipeline and create a fastapi end point up running in the cloud (so that the website can always access it)
- consider whether a paid tier is required fro Render's cloud api services
  
**04/22**
- Connect to Front-end (HTML & JavaScript architecture) via Render's cloud hosted FastAPI
- Create an analytical dashboard of visualizations via D3 or Python
- Connect an AI summarizer agent to the workflow to summarize lengthy job descriptions to 2-3 sentences
- Write a script that either uses mechanical key word extraction methods, or uses natural langugae processing to extract keywords such as skillset requirements from the job database
- Testing of scheduled task and whether website updates in real time
  
**04/30**
- Have a fully functioning real-time updated dashboard and geo-mapped job visualization website
