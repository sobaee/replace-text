#!/bin/bash
# 
# Dependencies:
# python3, pyglossary, mdict-utils, which
# 
# Install all dependencies with:
# pip3 install mdict-utils python-lzo
# pyglossary better to be installed from a local folder with: python setup.py install (better to use my ready pyglossary zip file)
#
if command -v python3 >/dev/null 2>&1; then
    if command -v pyglossary >/dev/null 2>&1; then
        if command -v mdict >/dev/null 2>&1; then
            echo -e "All dependencies are ready!\n"
        else
            echo "ERROR: mdict not found! Run 'pip3 install mdict-utils'!"
            exit 1
        fi
    else
        echo "ERROR: pyglossary not installed! Run 'pip3 install pyglossary'"
        exit 1
    fi
else
    echo "ERROR: python not installed! Download and install from https://www.python.org/downloads"
    exit 1
fi

read -p "Enter input file name: " input_file
read -p "Enter output file name: " output_file

replacement_pairs=()
read -p "Enter the number of text replacements: " num_replacements

for ((i=0; i<num_replacements; i++)); do
    read -p "Enter text to replace: " text_to_replace
    read -p "Enter new text: " new_text
    replacement_pairs+=("$text_to_replace,$new_text")
done

while IFS= read -r line; do
    for pair in "${replacement_pairs[@]}"; do
        old_text="${pair%,*}"
        new_text="${pair#*,}"
        line=${line//$old_text/$new_text}
    done
    echo "$line" >> "$output_file"
done < "$input_file"

file="$output_file"

read -p "Do you want to convert the resulted file to MDX? (y/n) " answer
    case $answer in
    y|Y) # Use Word Title option
    
        echo 'Your file will be converted to MDX'
        ;;
    n|N) # Do not use Word Title option
       echo 'Thank you for using my tool!'
       exit 1
       
        ;;
    *) # Invalid choice
        echo "Invalid option. Please enter y or n."
        ;;
esac

printf ${file%.*} > description.html
printf ${file%.*} > title.html

if [ -f "${file%.*}.mtxt" ]; then
    mdict --title title.html --description description.html -a "${file%.*}.mtxt" "${file%.*}.mdx"
else
    db_file="${file%.*}.cache"

    pyglossary "$file" "$db_file" --write-format=OctopusMdictSource

    mdict --title title.html --description description.html -a "$db_file" "${file%.*}.mdx"

    echo "All done."
fi

