from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/US_map')
def map():
    return render_template('US_job_map.html')

@app.route('/cavhires')
def cavhires():
    return render_template('cavhire_landing_page.html')

