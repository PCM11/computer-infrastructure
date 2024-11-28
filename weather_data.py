# Weather data

#Dates and times
import datetime as dt

# Get the current date and time.
filename = dt.datetime.now()

# Create a string from the current date and time.
filename = filename.strftime("%Y-%m-%d_%H-%M-%S") +".json"

filename 
