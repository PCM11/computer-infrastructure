## My Computer-Infrastructure Repository

**by Phumi Tshidi (phumitshidi@gmail.com)**

This repository contains my assessment submission for 24-25:8645 - COMPUTER INFRASTRUCTURE module.

### Task 1: Create Directory Structure

Using the command line, create a directory (that is, a folder) named data at the root of your repository. Inside data, create two subdirectories: timestamps and weather.

### Task 2: Timestamps

Navigate to the data/timestamps directory. Use the date command to output the current date and time, appending the output to a file named now.txt. Make sure to use the >> operator to append (not overwrite) the file. Repeat this step ten times, then use the more command to verify that now.txt has the expected content.

### Task 3: Formatting Timestamps

Run the date command again, but this time format the output using YYYYmmdd_HHMMSS (e.g., 20261114_130003 for 1:00:03 PM on November 14, 2026). Refer to the date man page (using man date) for more formatting options. (Press q to exit the man page). Append the formatted output to a file named formatted.txt.

### Task 4: Create Timestamped Files
Use the touch command to create an empty file with a name in the YYYYmmdd_HHMMSS.txt format. You can achieve this by embedding your date command in backticks ` into the touch command. You should no longer use redirection (>>) in this step.


