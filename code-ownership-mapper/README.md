# Code Ownership Mapper

A simple Python script to check for essential project files like `README.md`, `.gitignore`, and `LICENSE` in your repository. It's a handy tool for making sure your projects are well-structured and follow best practices.


## Table of Contents

- [What It Does](#what-it-does)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Requirements](#requirements)
- [Example Output](#example-output)
- [Troubleshooting](#troubleshooting)
- [License](#license)


## What It Does

This script scans the directory it's run from to see if a standard set of project configuration and metadata files are present. It's great for open-source maintainers, DevOps teams, or anyone who wants to enforce a consistent structure across multiple repositories. It helps you quickly spot what's missing so you can maintain project hygiene.


## How It Works

The script contains a predefined list of common and important files (`README.md`, `LICENSE`, `CODEOWNERS`, etc.). It then uses Python's `os` module to check if each file exists in its current directory. Finally, it prints a simple report to your terminal, showing you which files were found and which were not.


## Getting Started

1.  **Get the script:**
    Clone this repository or just download the `code-ownership-mapper.py` file to your local machine.

2.  **Make it executable:**
    You'll need to give the script permission to run. Open your terminal and run the following command.

    ```bash
    # This command modifies the file's permissions.
    # 'chmod' stands for 'change mode'.
    # '+x' adds the 'execute' permission to the file for all users.
    chmod +x code-ownership-mapper.py
    ```


## Usage

To check a project, navigate to its root directory in your terminal and run the script.

You can run it in one of two ways:

```bash
# Directly execute the script (since you made it executable)
./code-ownership-mapper.py

# Or run it with the Python interpreter
python3 code-ownership-mapper.py
```

You can also automate this check. For example, to run it every day at midnight using a cron job, you could add this line to your crontab:

```bash
# This cron schedule runs the command at 00:00 (midnight) every day.
0 0 * * * /full/path/to/code-ownership-mapper.py
```


## Requirements

-   Python 3.6 or newer.
-   The script **must be run from the root directory** of the project you want to analyze.

## Example Output

Here is what the report looks like when you run the script:

```text
===========================================
 Code Ownership Mapper
==================================================
README.md        ->  Present
LICENSE          ->  Missing
.gitignore       ->  Missing
CODEOWNERS       ->  Missing
CONTRIBUTING.md  ->  Missing
.gitattributes   ->  Missing
.editorconfig    ->  Missing

===========================================
Scan Complete.
Missing files should be added for better project structure.
===========================================
```


## Troubleshooting

-   **All files show as "Missing":**
    You are likely running the script from the wrong directory. Make sure you have used `cd` to navigate into the root folder of your project before running the script.

-   **The script won't run or crashes:**
    First, confirm you are using Python 3. Second, double-check that you made the script executable with the `chmod +x` command.

-   **A file exists but is marked as "Missing":**
    Check for typos in the filename and make sure it's in the root directory, not a subfolder.


## License

This project is licensed under the [MIT License](LICENSE).
