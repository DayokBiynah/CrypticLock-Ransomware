#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Find files
files = []

# Read all files except ransomware and directories
for file in os.listdir():
    if file == "Cryptolock.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# Print the files we have read
print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

# Open all necessary files and read them to the contents variable, then decrypt them
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)