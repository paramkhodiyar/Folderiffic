# Folderiffic : File Sorter

This Python script helps you easily sort files based on a keyword within your Downloads folder. It provides a user-friendly graphical interface (GUI) using tkinter and offers progress updates.

## Features:

- Sorts files containing a specified keyword in their filenames.
- User-selectable destination folder for the sorted files.
- Progress bar displays the sorting progress.
- Status label provides feedback on the sorting process.

## Installation:

1. **Prerequisites:** Ensure you have Python (version 3 recommended) installed on your system. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. **Clone the repository:** Open your terminal or command prompt and navigate to the desired directory. Then, run the following command to clone this repository:

   ```bash
   git clone https://github.com/your-username/file-sorter.git
   ```

   Replace `your-username` with your actual GitHub username.

3. **Install dependencies:** Navigate to the cloned repository directory using `cd file-sorter` and install the required Python library using pip:

   ```bash
   pip install tkinter
   ```

## Usage:

1. **Run the script:** Execute the main Python script using the following command:

   ```bash
   python Folderrific.py
   ```

2. **Enter keyword:** In the GUI window, type the keyword you want to use for sorting in the "Enter keyword" field.
3. **Choose destination:** Click the "Choose the destination Folder" button to select the directory where you want to move the sorted files.
4. **Start sorting:** Click the "Choose the destination Folder" button again (the button doubles as the sort button in this case). The script will start sorting files and provide progress updates in the status label and progress bar.

## Notes:

- The script currently sorts files based on the keyword existing anywhere in the filename (not case-sensitive). You can modify the code within the `sort_files` function to customize the matching behavior if needed.
- The script moves files to the selected destination folder. If a file with the same name already exists in the destination, the existing file will be overwritten. 

## Contribution:

Feel free to fork this repository, make improvements, and submit pull requests to enhance the script's functionality. 

