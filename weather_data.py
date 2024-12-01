# Libraries
import pandas as pd
#Dates and times
import datetime as dt

# Load data
df = pd.read_json('https://prodapi.metweb.ie/observations/athenry/today')
# Get the current date and time.
filename = dt.datetime.now()

# Create a string from the current date and time.
filename = filename.strftime("%Y%m%d_%H%M%S") +".json"
filename = 'data/' + filename

# Save data to json file
df.to_json(filename)
