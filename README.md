# Computer Infrastructure Repository
**by: Phumi Tshidi (phumitshidi@gmail.com)**

## About the repository

This repository contains various tasks and scripts related to computer infrastructure management and automation. The focus is on creating, managing, and timestamping files and directories, downloading data, and performing basic scripting tasks. 

Additionally, the repository includes a **Weather Jupyter Notebook** that provides a summary of all tasks.

## Repository Contents

### 1. **Tasks**
   **Task 1:** Create Directory Structure

   - This task demonstrates how to create a directory structure using the command line. It provides a basic example of how to organize directories for storing files and data.

   **Task 2:** Timestamps Using 

   - This task explores the usage of the `date` command to generate timestamps in a variety of formats.

   **Task 3:** Formatting Timestamps 

   - This task involves formatting timestamps to a specific pattern and appending them to a text file, using `date` command.


   **Task 4:** Create Timestamped Files

   - In this task, you will use the `touch` command to create files with timestamped names. These files are created based on the current time and can be used to track data and activities with precise timestamps.

   **Task 5:** Download Today's Weather Data

   - This task demonstrates how to download today's weather data using the `wget` command. It provides a basic example of how to download JSON data from a remote server using a simple command.

   **Task 6:** Timestamp the Data

   - Once the weather data is downloaded, this task shows how to timestamp the downloaded file in the YYYYmmdd_HHMMSS.json format. This allows for easy tracking and organization of downloaded files.

   **Task 7:** Write a Bash Script

   - This task includes a bash script that automates some of the tasks listed above. The script will help in organizing, downloading, and timestamping files efficiently.


### 2. **Weather Jupyter Notebook**
   - A Jupyter notebook summarizing all the tasks, explaining their purpose, and demonstrating the code in action. It provides insights into how to integrate and visualize the results of the tasks.

### 3. **Scripts**
   - Bash scripts that automate some of the tasks, such as creating directories, downloading weather data, and timestamping files.

### 4. **Documentation**
   - This README provides an overview of the tasks and steps to run the repository.
   - The **weather_summary.ipynb** notebook contains a detailed summary and code explanations.

## Navigating the Repository

Here is a breakdown of the important files and directories in the repository:

- **tasks/**: Contains scripts and commands for each task listed above.
- **scripts/**: Includes a bash script (`script.sh`) that automates several tasks (like downloading weather data and timestamping).
- **notebooks/**: Contains the Jupyter notebook (`weather_summary.ipynb`) that summarizes all tasks.
- **README.md**: This file contains an overview of the repository and instructions.
- **LICENSE**: The repository's license information (MIT License).

## Running the Repository Using GitHub Codespaces

You can easily run this repository in a GitHub Codespace, which provides a cloud-based development environment. Here's how:

### 1. Open the Repository in GitHub Codespaces
   - Go to the GitHub repository page.
   - Click on the green "Code" button.
   - Select **Open with Codespaces** and then **New codespace**.
   
   This will launch a Codespace with the repository's code pre-loaded in a VS Code-like environment.

### 2. Set Up the Environment in Codespaces

Once your Codespace is ready, follow these steps:

   1. **Open the terminal in Codespaces:**
      - In the bottom panel, click on the "Terminal" tab to open the terminal.
   
   2. **Run the Bash Script:**
      - Navigate to the `scripts/` directory (if applicable) and run the bash script:
      ```bash
      cd scripts
      bash script.sh
      ```

   3. **Running the Jupyter Notebook:**
      - To run the Jupyter Notebook, open the `weather_summary.ipynb` file under the `notebooks/` directory.
      - Click on the **Run** button or use the command palette to run the cells and see the output.

### 3. Execute Individual Tasks

You can also run individual tasks manually from the terminal or through scripts:

   - **Task 1:** Create Directory Structure using Command Line:
     ```bash
     mkdir -p dir1/subdir1
     ```
   
   - **Task 2:** Generate Timestamps:
     ```bash
     date '+%Y-%m-%d %H:%M:%S'
     ```
   
   - **Task 5:** Download Today's Weather Data using `wget`:
     ```bash
     wget http://example.com/weather_data.json -O weather_$(date +%Y%m%d_%H%M%S).json
     ```

Each task can be executed independently, or you can automate the entire process using the provided bash script.

## Dependencies

- **Bash shell** (Linux/macOS or Windows Subsystem for Linux)
- **`wget`** (for downloading weather data)
- **Jupyter Notebook** (for viewing the weather summary)
- **GitHub Codespaces** (optional, for cloud-based environment)

If you're running the repository locally (outside Codespaces), make sure to install Jupyter and any other dependencies using `pip` or your preferred method.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.


