#!/usr/bin/env python3

import os
import stat
import pwd
import grp

# --- Step 1: Define what's "correct" ---
# This is a simple list of rules. Each rule is a tuple containing:
# (path_to_check, expected_owner, expected_group, expected_directory_permission, expected_file_permission)
# We use 'None' if we don't want to check something.
# The '0o' prefix means the number is in octal, which is how permissions are written.
RULES_TO_CHECK = [
    # Rule for our web server files
    ("/var/www/html", "www-data", "www-data", 0o755, 0o644),
    
    # Rule for a sensitive config file (we don't check dir_mode here)
    ("/etc/myapp/config.conf", "root", "root", None, 0o600),

    # Rule for the /tmp directory
    ("/tmp", "root", "root", 0o1777, None),
]

print("--- Starting Basic Permission Audit ---")

# --- Step 2: Loop through each rule ---
for path_to_check, owner, group, dir_mode, file_mode in RULES_TO_CHECK:
    print(f"\nChecking policy for: {path_to_check}...")

    # Check if the path even exists before we start.
    if not os.path.exists(path_to_check):
        print(f"  [WARNING] Path does not exist: {path_to_check}")
        continue # Skip to the next rule in our list

    # os.walk is a powerful tool that "walks" through a directory tree.
    # For each directory it finds (including the top one), it gives us its path (root),
    # a list of its subdirectories (dirs), and a list of its files (files).
    for root, dirs, files in os.walk(path_to_check):
        
        # --- Step 3: Check all the directories found by os.walk ---
        if dir_mode is not None:
            try:
                # os.stat gets all the info about a file/dir
                s = os.stat(root) 
                # stat.S_IMODE gets just the permission part
                current_mode = stat.S_IMODE(s.st_mode) 
                
                if current_mode != dir_mode:
                    print(f"  [FAIL] Directory {root}: Mode is {oct(current_mode)}, should be {oct(dir_mode)}")

            except (FileNotFoundError, PermissionError) as e:
                print(f"  [ERROR] Could not check directory {root}: {e}")
        
        # --- Step 4: Check all the files in the current directory ---
        for filename in files:
            # Create the full path to the file
            filepath = os.path.join(root, filename)
            
            try:
                # Get the file's stats
                s = os.stat(filepath)
                current_mode = stat.S_IMODE(s.st_mode)
                current_uid = s.st_uid
                current_gid = s.st_gid

                # Convert user ID (uid) and group ID (gid) to human-readable names
                current_owner_name = pwd.getpwuid(current_uid).pw_name
                current_group_name = grp.getgrgid(current_gid).gr_name

                # Now, run our checks
                if owner is not None and current_owner_name != owner:
                    print(f"  [FAIL] File {filepath}: Owner is {current_owner_name}, should be {owner}")
                
                if group is not None and current_group_name != group:
                    print(f"  [FAIL] File {filepath}: Group is {current_group_name}, should be {group}")

                if file_mode is not None and current_mode != file_mode:
                    print(f"  [FAIL] File {filepath}: Mode is {oct(current_mode)}, should be {oct(file_mode)}")

            except (FileNotFoundError, PermissionError) as e:
                print(f"  [ERROR] Could not check file {filepath}: {e}")

    # If the path we are checking is a single file, os.walk won't run.
    # So we handle that case separately.
    if os.path.isfile(path_to_check):
        try:
            s = os.stat(path_to_check)
            current_mode = stat.S_IMODE(s.st_mode)
            if file_mode is not None and current_mode != file_mode:
                 print(f"  [FAIL] File {path_to_check}: Mode is {oct(current_mode)}, should be {oct(file_mode)}")
        except (FileNotFoundError, PermissionError) as e:
            print(f"  [ERROR] Could not check file {path_to_check}: {e}")


print("\n--- Audit Complete ---")

