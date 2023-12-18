#!/usr/bin/env python3
# 
# Dependencies:
# python3, pyglossary, mdict-utils, which
# 
# Install all dependencies with:
# pip3 install mdict-utils python-lzo
# pyglossary better to be installed from a local folder with: python setup.py install (better to use my ready pyglossary zip file)
#
# Import the modules

import os
import sys
import subprocess

def command_exists(command):
    # Check if a command exists in the system
    return subprocess.call(['which', command], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

if command_exists('python3'):
    print('Python3 is ready!')
else:
    print("ERROR: python not installed! Download and install from https://www.python.org/downloads")
    sys.exit(1)

if command_exists('pyglossary'):
    print('Pyglossary is ready!')
else:
    print("ERROR: pyglossary not installed! Run 'pip3 install pyglossary'")
    sys.exit(1)

if command_exists('mdict'):
    print('Mdict-utils is ready!')
else:
    print("ERROR: mdict not found! Run 'pip3 install mdict-utils'!")
    sys.exit(1)

input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

replacement_pairs = []
num_replacements = int(input("Enter the number of text replacements: "))

for i in range(num_replacements):
    text_to_replace = input("Enter text to replace: ")
    new_text = input("Enter new text: ")
    replacement_pairs.append((text_to_replace, new_text))

with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
    for line in in_file:
        for pair in replacement_pairs:
            old_text, new_text = pair
            line = line.replace(old_text, new_text)
        out_file.write(line)

file = output_file

answer = input("Do you want to convert the resulted file to MDX? (y/n) ")
if answer.lower() == 'y':
    print('Your file will be converted to MDX')
else:
    print('Thank you for using my tool!')
    exit(1)

subprocess.run(["printf", file.rsplit('.', 1)[0]], stdout=open("description.html", "w"))
subprocess.run(["printf", file.rsplit('.', 1)[0]], stdout=open("title.html", "w"))

if file.rsplit('.', 1)[1] == 'mtxt':
    subprocess.run(["mdict", "--title", "title.html", "--description", "description.html",
                    "-a", f"{file.rsplit('.', 1)[0]}.mtxt", f"{file.rsplit('.', 1)[0]}.mdx"])
else:
    db_file = f"{file.rsplit('.', 1)[0]}.cache"
    subprocess.run(["pyglossary", file, db_file, "--write-format=OctopusMdictSource"])

    subprocess.run(["mdict", "--title", "title.html", "--description", "description.html",
                    "-a", db_file, f"{file.rsplit('.', 1)[0]}.mdx"])

print("All done.")