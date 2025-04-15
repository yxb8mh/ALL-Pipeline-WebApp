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
**04/16**
- Automate the web-scrape task and connect it with MongoDB via Shell 
- initialize the pipeline and create a fastapi end point up running in the cloud (so that the website can always access it)
- consider whether a paid tier is required fro Render's cloud api services
**04/22**
- Connect to Front-end (HTML & JavaScript architecture) via Render's cloud hosted FastAPI
- Establishment of analytical visualizations via D3 or Python
- Connect an AI summarizer agent to the workflow to summarize lengthy job descriptions to 2-3 sentences
- Write a script that either uses mechanical key word extraction methods, or using natural langugae processing to extract keywords such as skillset requirements from the job database
- Testing of scheduled task and whether website updates in real time
**04/30**
- Have a fully functioning real-time updated dashboard and geo-mapped job visualization website
