import tkinter as tk
from tkinter import filedialog
import os
import subprocess

def analyze_log_file():
    input_file_path = input_field.get()
    output_file_path = output_field.get()

    if not os.path.isfile(input_file_path):
        output_label.config(text=f"Input file does not exist: {input_file_path}")
        return

    error_counts = {}

    with open(output_file_path, 'w') as error_file:
        with open(input_file_path, 'r') as f:
            for line in f:
                if "ERROR" in line or "WARN" in line:
                    error_file.write(line)

                    if line not in error_counts:
                        error_counts[line] = 1
                    else:
                        error_counts[line] += 1

    output_label.config(text=f"Analysis complete. View results in: {output_file_path}")

def browse_input():
    filename = filedialog.askopenfilename(filetypes=[('Log Files', '*.log')])
    input_field.delete(0, tk.END)  # Remove current text in input_field
    input_field.insert(0, filename)  # Insert the 'filename'

def browse_output():
    filename = filedialog.asksaveasfilename(initialfile='analysed_log_file.log', filetypes=[('Log Files', '*.log')])
    output_field.delete(0, tk.END)  # Remove current text in output_field
    output_field.insert(0, filename)  # Insert the 'filename'

def open_output():
    output_file_path = output_field.get()
    if not os.path.isfile(output_file_path):
        output_label.config(text=f"Output file does not exist: {output_file_path}")
        return

    # Open the file using the default program
    subprocess.call([output_file_path], shell=True)

def open_sod_config():
    sod_config_path = 'C:/Program Files (x86)/Nuance/Dragon Medical One/SoD.exe.config'
    if not os.path.isfile(sod_config_path):
        output_label.config(text="SoD.exe.config file not found.")
        return

    # Open the SoD.exe.config file using the default program
    subprocess.call([sod_config_path], shell=True)

def show_dmo_org_token():
    sod_config_path = 'C:/Program Files (x86)/Nuance/Dragon Medical One/SoD.exe.config'
    if not os.path.isfile(sod_config_path):
        output_label.config(text="SoD.exe.config file not found.")
        return

    token = None

    with open(sod_config_path, 'r') as sod_config_file:
        lines = sod_config_file.readlines()

    for i, line in enumerate(lines):
        if '<setting name="OrganizationToken" serializeAs="String">' in line:
            for j in range(i+1, len(lines)):
                if '<value>' in lines[j] and '</value>' in lines[j]:
                    token = lines[j].split('<value>')[1].split('</value>')[0].strip()
                    break
            break

    if token:
        org_token_field.delete(0, tk.END)  # Clear current text in org_token_field
        org_token_field.insert(0, token)  # Insert the organization token
    else:
        org_token_field.delete(0, tk.END)  # Clear current text in org_token_field
        org_token_field.insert(0, "Organization token not found")

def add_supported_languages():
    sod_config_path = 'C:/Program Files (x86)/Nuance/Dragon Medical One/SoD.exe.config'
    if not os.path.isfile(sod_config_path):
        output_label.config(text="SoD.exe.config file not found.")
        return

    languages = []
    if var_en_au.get():
        languages.append("en-AU")
    if var_en_gb.get():
        languages.append("en-GB")
    if var_en_us.get():
        languages.append("en-US")

    if not languages:
        output_label.config(text="Please select at least one language.")
        return

    with open(sod_config_path, 'r') as sod_config_file:
        lines = sod_config_file.readlines()

    for i, line in enumerate(lines):
        if '<setting name="SupportedLanguages" serializeAs="String">' in line:
            for j in range(i+1, len(lines)):
                if '<value>' in lines[j] and '</value>' in lines[j]:
                    old_value = lines[j].split('<value>')[1].split('</value>')[0]
                    new_value = "|".join(languages)
                    lines[j] = lines[j].replace(old_value, new_value)
                    break
            break

    with open(sod_config_path, 'w') as sod_config_file:
        sod_config_file.writelines(lines)

    output_label.config(text="Supported languages updated.")

root = tk.Tk()
root.title('Log Analyzer')

input_label = tk.Label(root, text="Enter log file location")
input_label.pack()

input_field = tk.Entry(root)
input_field.pack()

input_button = tk.Button(root, text='Browse', command=browse_input)
input_button.pack()

output_label = tk.Label(root, text="Enter output file location")
output_label.pack()

output_field = tk.Entry(root)
output_field.pack()

output_button = tk.Button(root, text='Browse', command=browse_output)
output_button.pack()

tk.Label(root, text="").pack()

button = tk.Button(root, text='Analyze Log File', command=analyze_log_file)
button.pack()

output_open_button = tk.Button(root, text='Open Output File', command=open_output)
output_open_button.pack()

tk.Label(root, text="").pack()

sod_config_button = tk.Button(root, text='Open SoD Config', command=open_sod_config)
sod_config_button.pack()

tk.Label(root, text="").pack()

dmo_token_button = tk.Button(root, text='Show DMO Org Token', command=show_dmo_org_token)
dmo_token_button.pack()

org_token_label = tk.Label(root, text="DMO Org Token:")
org_token_label.pack()

org_token_field = tk.Entry(root, width=40)  # Increase the width of the Entry field
org_token_field.pack()

output_label = tk.Label(root, text="")
output_label.pack()

var_en_au = tk.IntVar()
var_en_gb = tk.IntVar()
var_en_us = tk.IntVar()

check_en_au = tk.Checkbutton(root, text='en-AU', variable=var_en_au)
check_en_au.pack()

check_en_gb = tk.Checkbutton(root, text='en-GB', variable=var_en_gb)
check_en_gb.pack()

check_en_us = tk.Checkbutton(root, text='en-US', variable=var_en_us)
check_en_us.pack()

button_add_languages = tk.Button(root, text='Add Supported Languages', command=add_supported_languages)
button_add_languages.pack()

root.mainloop()
