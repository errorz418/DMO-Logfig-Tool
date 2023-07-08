# Log Analyzer

This Python script provides a simple graphical user interface to analyze log files and interact with the SoD.exe.config file. It leverages the widely-used Tkinter library for creating desktop applications.

## Features

The Log Analyzer script supports several functionalities:

1. **Browse and Select a Log File**: This feature allows users to navigate through the file system and select a specific log file for analysis.

2. **Analyze Log File**: This feature enables the script to read the selected log file, identify lines containing "ERROR" or "WARN", and write these lines to an output file. Users can specify the location of this output file.

3. **Open Output File**: After the log file analysis, users have the option to open the analyzed output file using the default program configured on their system.

4. **Interact with SoD.exe.config File**: The script has the capability to read the SoD.exe.config file and perform several actions:
    - **Display Organization Token**: Retrieves and displays the 'OrganizationToken' value present in the file.
    - **Add or Update Supported Languages**: This feature can add or update the 'SupportedLanguages' based on user selections.

## Getting Started

To run the script, ensure that Python and Tkinter are installed on your system. Simply download the script, navigate to its location in your terminal, and execute it with Python.
