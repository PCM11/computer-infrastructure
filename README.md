# Computer Infrastructure Repository
**by: Phumi Tshidi (phumitshidi@gmail.com)**

<img src="https://www.prompt-master.org/wp-content/uploads/2024/12/output1Nvidia-Predictions-for-2025-Quantum-Computing-AI-Agents-and-Infrastructure-Overhaul-1280x731.png" width="" height="300">

## Key Sections

- **Overview:** Summarises the notebook.
- **Contents:**  Describes the structure of the repository and where to find the tasks, scripts, and notebook.
- **Usage Instructions:** Explains what the notebook does and how to interact with it.
- **Requirements:** Lists dependencies required to run the notebook.
- **Running the Jupyter Notebook:** Provides instructions for running the notebook using Anaconda, Visual Studio Code or Codespaces. 
- **Conclusion:** Provides the reader with an outcome.

## Overview

This repository contains various tasks and scripts related to computer infrastructure management and automation. The focus is on creating, managing, and timestamping files and directories, downloading data, and performing basic scripting tasks. 

Additionally, the repository includes a **Weather Jupyter Notebook** that provides a summary of all tasks and weather data analysis.

## Contents

### 1. **Tasks**
   **Task 1:** Create Directory Structure

   - This task demonstrates how to create a `data` directory and its two subdirectories, `timestamps and weather` using the command line. It provides a basic example of how to organize directories for storing files and data.

   **Task 2:** Timestamps

   - This task explores the usage of the date command to generate timestamps appending the output into the `now.txt` file.

   **Task 3:** Formatting Timestamps 

   - This task involves formatting timestamps in a `YYYYmmdd_HHMMSS`  format and appending them to `formatted.txt` using date command.


   **Task 4:** Create Timestamped Files

   - In this task, you will use the `touch` command to create an empty file with timestamped names in the YYYYmmdd_HHMMSS.txt format. These files are created based on the current time and can be used to track data and activities with precise timestamps.

   **Task 5:** Download Today's Weather Data

   - This task demonstrates how to download latest Athenry's weather data using the `wget` command. It provides a basic example of how to download JSON data from a remote server using a simple command.

   **Task 6:** Timestamp the Data

   - Once the weather data is downloaded, this task shows how to timestamp the downloaded file in the YYYYmmdd_HHMMSS.json format. This allows for easy tracking and organization of downloaded files.

   **Task 7:** Write a Bash Script

   - This task creates a bash script in the root of the repository that automates some of the tasks listed above. The script will help in organizing, downloading, and timestamping files efficiently.


### 2. **Weather Jupyter Notebook**
   - A Jupyter notebook summarizing all the tasks, explaining their purpose, and demonstrating the code in action. It provides insights into how to integrate and visualize the results of the tasks.
   - It also contains the analysis of the dataframe for one of the weather files downloaded with bash script.

## How to Use

- **Load the dataset**: The notebook includes steps for loading weather data.
- **Data cleaning**: The notebook performs necessary cleaning operations, such as handling missing values or removing irrelevant columns.
- **Data analysis and visualization**: It processes the data using `pandas, numpy` and generates visualizations (using `matplotlib` or `seaborn`) to provide insights into wind speed trends.

## Requirements

Before running the notebook, ensure you have the following installed:
- [Python](https://www.python.org/downloads/) (version 3.12 or higher) also available through anaconda.
- Jupyter Notebook
- [Anaconda](https://www.anaconda.com/download) - recommended for managing environments
- [Visual Studio Code](https://code.visualstudio.com/) - for editing and running Jupyter notebooks

You can install all required dependencies by running:

## Running the Jupyter Notebook

There are three main ways to run the notebook: using **Anaconda**, **Visual Studio Code** or **Codespaces**.

### 1. Running with Anaconda

If you're using Anaconda, follow these steps:

1. **Clone this repository** to your local machine:

    ```bash
    git clone https://github.com/PCM11/computer-infrastructure
    ```

2. **Navigate to the repository directory**:

    ```bash
    cd computer-infrastructure
    ```

3. **Create a new Conda environment** (optional but recommended) with the necessary dependencies:

    ```bash
    conda create -n weather python=3.12
    ```

4. **Activate the environment**:

    ```bash
    conda activate weather
    ```

5. **Install dependencies** from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

6. **Launch Jupyter Notebook**:

    ```bash
    jupyter notebook
    ```

    This will open Jupyter in your web browser. Navigate to `weather.ipynb` and start working with the notebook.

### 2. Running with Visual Studio Code

If you prefer using Visual Studio Code:

1. **Clone the repository** to your local machine:

    ```bash
    git clone https://github.com/PCM11/computer-infrastructure
    ```

2. **Navigate to the project directory**:

    ```bash
    cd computer-infrastructure
    ```

3. **Open the folder** in Visual Studio Code:

    ```bash
    code .
    ```

4. **Install the Python extension** (if not already installed) in Visual Studio Code.

5. **Install the dependencies** by opening a terminal in Visual Studio Code and running:

    ```bash
    pip install -r requirements.txt
    ```

6. **Install the Jupyter extension** in Visual Studio Code.

7. **Open the Jupyter notebook** (`weather.ipynb`) in Visual Studio Code, and the notebook interface will be available to run cells interactively.

### 3. Running the Repository Using GitHub Codespaces

You can also run this repository in a GitHub Codespace, which provides a cloud-based development environment. Here's how:

1.**Open the Repository** in GitHub Codespaces
   - Go to the GitHub repository page.
   - Click on the green "Code" button.
   - Select **Open with Codespaces** and then **New codespace**.
   
This will launch a Codespace with the repository's code pre-loaded in a VS Code-like environment.

2.**Set Up the Environment** in Codespaces

Once your Codespace is ready, follow these steps:

- **Open the terminal** in Codespaces:

- In the bottom panel, click on the "Terminal" tab to open the terminal.
   
- **Run the Bash Script:**
      - Navigate to the `scripts/` directory (if applicable) and run the bash script:

      ```bash
      cd scripts
      bash script.sh
      ```
## Conclusion

In this notebook, we have successfully:

- Learned how to create directories and files with timestamps using the command line.
- Generated timestamps using the `date` command.
- Downloaded and timestamped weather data using `wget.`
- Wrote a bash script to automate these tasks.
- Loaded, summarized, and analyzed weather data using `pandas.`