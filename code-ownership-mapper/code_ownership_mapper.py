#!/usr/bin/env python3

# Infrastructure Cost Optimization Advisor
# Analyzes cloud usage and cost data to detect underutilized or oversized resources
# and recommends or applies cost-saving actions.

# Code Ownership Mapper
# Scans a GitHub repository for important standard project files like CODEOWNERS, .gitignore, README.md, etc.,
# and reports which ones are present or missing.

import os

# Define expected special files and their typical paths
special_files = {
    "README.md": "README.md",
    "LICENSE": "LICENSE",
    ".gitignore": ".gitignore",
    "CODEOWNERS": ".github/CODEOWNERS",
    "CONTRIBUTING.md": "CONTRIBUTING.md",
    ".gitattributes": ".gitattributes",
    ".editorconfig": ".editorconfig"
}

print(" Code Ownership Mapper")
print("=" * 50)

# Check for presence or absence of each file
for name, path in special_files.items():
    if os.path.exists(path):
        status = " Present"
    else:
        status = " Missing"
    print(f"{name:20} -> {status}")


