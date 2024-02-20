from flask import Flask, render_template_string
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def show_time():
    # Get the current time in UTC
    utc_now = datetime.now(pytz.utc)
    # Convert the current time to EST
    est_now = utc_now.astimezone(pytz.timezone('US/Eastern'))
    # Format the time string
    time_str = est_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    # Render a simple template displaying the time
    return render_template_string('<h1>Current Time in EST: {{ time }}</h1>', time=time_str)
