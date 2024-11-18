# My Computer-Infrastructure Repository

**by Phumi Tshidi (phumitshidi@gmail.com)**

## About the repository

This repository contains my assessment submission for 24-25: 8645 - COMPUTER INFRASTRUCTURE module.
It consists of 9 tasks and one project.

## Tasks

**1. Create Directory Structure**

Create a directory (that is, a folder) named data at the root of your repository. Inside data, create two subdirectories: timestamps and weather.

**2. Timestamps**

Navigate to the data/timestamps directory. Use the date command to output the current date and time, appending the output to a file named now.txt. Make sure to use the >> operator to append (not overwrite) the file. Repeat this step ten times, then use the more command to verify that now.txt has the expected content.

**3. Formatting Timestamps**

Run the date command again, but this time format the output using YYYYmmdd_HHMMSS (e.g., 20261114_130003 for 1:00:03 PM on November 14, 2026). Append the formatted output to a file named formatted.txt.

**4. Create Timestamped Files**
Use the touch command to create an empty file with a name in the YYYYmmdd_HHMMSS.txt format. You can achieve this by embedding your date command in backticks ` into the touch command.


**5. Download Today's Weather Data**

Change to the data/weather directory. Download the latest weather data for the Athenry weather station from Met Eireann using wget. Use the -O <filename> option to save the file as weather.json. The data can be found at this URL:
https://prodapi.metweb.ie/observations/athenry/today.

**6. Timestamp the Data**

Modify the command from Task 5 to save the downloaded file with a timestamped name in the format YYYYmmdd_HHMMSS.json.

**7. Write the Script**

Write a bash script called weather.sh in the root of your repository. This script should automate the process from Task 6, saving the weather data to the data/weather directory. Make the script executable and test it by running it.

**8. Notebook**

Create a notebook called weather.ipynb at the root of your repository. In this notebook, write a brief report explaining how you completed Tasks 1 to 7. Provide short descriptions of the commands used in each task and explain their role in completing the tasks.

**9. Pandas**

In your weather.ipynb notebook, use the pandas function read_json() to load in any one of the weather data files you have downloaded with your script. Examine and summarize the data. Use the information provided data.gov.ie to write a short explanation of what the data set contains.

## Project

In this project, you will automate your weather.sh script to run daily and push the new data to your repository. The following steps will create the necessary GitHub Actions workflow.

1. Create a GitHub Actions Workflow: In your repository, create a folder called .github/workflows/ (if it doesn't already exist). Inside this folder, create a file called weather-data.yml. This file will define the GitHub Actions workflow.

2. Run Daily at 10am: Use the schedule event with cron to set the script to run once a day at 10am. Include also the workflow_dispatch event so you can test the workflow.

3. Use a Linux Virtual Machine In the workflow file, specify that a Ubuntu virtual machine should be used to run the action.

4. Clone the Repository Have the workflow clone your repository.

5. Execute the weather.sh Script Add a step that runs your weather.sh script.

6. Commit and Push Changes Back to the Repository Finally, configure the workflow to commit the new weather data and push those changes back to your repository.

7. Test the Workflow Commit and push the workflow to your repository. Check the logs in GitHub to ensure that the weather.sh script runs correctly, that new data is being committed.

## Installations

To further explore this dataset you need 
to download python, which can be 
installed through [anaconda](https://www.
anaconda.com
download), and notebook editor, which can 
be found in [Visual Studio Code](https://
code.visualstudio.com/)