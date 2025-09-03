# File Sorter

This is a simple and customizable Python script to organize files in a directory into categorized folders based on their file extensions.

## Features

* **Categorizes Files:** Automatically sorts files into folders like `Image`, `Video`, and `Audio`.
* **Handles Edge Cases:** Gracefully handles files with no recognized extension by placing them in an `'Other'` folder.
* **User-Friendly:** Prompts the user for the directory path to sort.
* **Customizable:** Categories and file extensions can be easily customized by editing a separate `config.json` file.
* **Safe:** Will not overwrite existing folders.

## How to Use

1.  Save the Python code in a file named `sorter.py`.
2.  Create a separate file named `config.json` in the same directory and add your categories to it.
3.  Run the script from your terminal:
    ```bash
    python sorter.py
    ```
4.  Follow the prompts to enter the path of the directory you want to organize.

## Requirements

The script requires the following standard Python libraries:

* `os`
* `shutil`
* `json`

## Customization

You can easily add new categories or file extensions by editing the `config.json` file. The format is a dictionary where the keys are the folder names and the values are a list of file extensions.

**Example `config.json`:**
```json
{
  "Image": [
    ".png",
    ".jpg",
    ".jpeg",
    ".bmp",
    ".webp"
  ],
  "Video": [
    ".mp4",
    ".mkv",
    ".mov"
  ],
  "Documents": [
    ".pdf",
    ".docx",
    ".txt"
  ],
  "Code": [
    ".py",
    ".js",
    ".html",
    ".css"
  ]
}
