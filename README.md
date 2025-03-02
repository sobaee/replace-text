# replace-text


This is a python script to automatically replace any number of texts with other texts from the big text files without the need to open the file and do it manually; then will save it to a new file.


<br />
<br />


## DEPENDENCIES:


python3, pyglossary, mdict-utils, python-lzo

You don't need them for the basic function,  you just need them for the extra move that convert the resulted file to .mdx mdict dictionaries


<br />
<br />


## USAGE:


- Navigate to the directory that contains this script and copy the dictionary file (or any other text file) to the same directory, and  run the command: `python replace-text.py`  

- Before replacement the script will ask you to define the number of the text lines that you want to replace, then after replacement it will optionally convert the resulted file to MDICT MDX dictionary.



Thanks to the owners of Pyglossary, mdict-utils.

Download the modified version of Pyglossary from my fork, with octopus_mdict_source.py plugin added and setup.py file fixed; after decompression of the downloaded file, you can do: `python setup.py install` from inside the decompressed folder to install pyglossay and it will work perfectly: [LINK](https://codeload.github.com/sobaee/pyglossaryfork/zip/refs/tags/5.0.0)
