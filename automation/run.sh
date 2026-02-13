#!/bin/bash
#
# Shoe Scanner Automation Runner
#
# Simple wrapper script for running automation via cron.
# Ensures proper environment and paths are set.
#

# Set script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Change to script directory
cd "$SCRIPT_DIR"

# Run with Python 3
python3 shoescanner_automation.py

# Exit with same code as Python script
exit $?
