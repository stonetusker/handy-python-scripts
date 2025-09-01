# Basic File Permission Auditor

This is a straightforward Python script for auditing file and directory permissions on a Linux system. It checks specified paths against a predefined set of rules for ownership (user and group) and permissions, then reports any discrepancies it finds. It's a simple way to help ensure your system's security configuration is correct.


## Features

-   **Rule-Based Auditing**: Define a list of rules for paths, owners, groups, and permissions.
-   **Recursive Checking**: When given a directory, the script will walk through all of its subdirectories and files to check them against the rule.
-   **Specific File Checks**: Can also check the permissions and ownership of individual files.
-   **Clear Reporting**: Prints easy-to-read warnings and failures directly to your terminal.
-   **No Dependencies**: Runs using only standard Python libraries, so there's nothing extra to install.


## How It Works

The script operates on a simple principle: you tell it what the permissions *should* be, and it checks if that's how they actually are.

You define these expectations in the `RULES_TO_CHECK` list at the top of the script. The script then iterates through each rule, checks the specified path, and prints a `[FAIL]` message for any setting that doesn't match your rule.


## Configuration

All configuration is done by editing the `RULES_TO_CHECK` list inside the Python script. Each rule is a line in the list that defines what to check for a specific path.

Here is the format for a rule:
`(path_to_check, expected_owner, expected_group, expected_directory_permission, expected_file_permission)`

-   `path_to_check`: The absolute path to the file or directory you want to audit.
-   `expected_owner`: The username that should own the files/directories.
-   `expected_group`: The group name that should own the files/directories.
-   `expected_directory_permission`: The correct permission mode for directories, written in octal (e.g., `0o755`).
-   `expected_file_permission`: The correct permission mode for files, written in octal (e.g., `0o644`).

You can use `None` for any value you don't want to check. For example, if you only care about file permissions and not the owner, you can set the owner and group to `None`.

**Example Rules:**

```python
RULES_TO_CHECK = [
    # Rule for our web server files
    ("/var/www/html", "www-data", "www-data", 0o755, 0o644),
    
    # Rule for a sensitive config file (we only care about file permissions here)
    ("/etc/myapp/config.conf", "root", "root", None, 0o600),

    # Rule for the /tmp directory (we only care about the directory permission)
    ("/tmp", "root", "root", 0o1777, None),
]
```

## How to Use

1.  **Save the script**: Save the code to a file, for example, `audit_permissions.py`.
2.  **Customize the rules**: Open the file and edit the `RULES_TO_CHECK` list to match the paths and permissions you want to verify on your system.
3.  **Make it executable (Optional but Recommended)**:
    Since you're on Linux, you can make the script directly executable.

    ```bash
    chmod +x audit_permissions.py
    ```
    -   `chmod`: This command changes file modes or permissions.
    -   `+x`: This part adds the 'executable' permission for the user.
    -   `audit_permissions.py`: The name of your script.

4.  **Run the script**:
    Because the script needs to read information about system files, you will likely need to run it with `sudo`.

    If you made it executable:
    ```bash
    sudo ./audit_permissions.py
    ```

    If you did not make it executable:
    ```bash
    sudo python3 audit_permissions.py
    ```

The script will then print its findings to the terminal.

