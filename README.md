# encryption-project
This is a small python program I made to test out cryptography.fernet as well as writing to, reading and editing data on files to create a program that can encrypt and decrpyt your files

(View the full source code for a more detailed look)
The fernet python module is an example of a "secret key" authenticated cryptography, it uses a 128-bit AES (faster than 256 bit as AES so far has not yet been able to be cracked...) and SHA256 hashing

# How it works:
1) Firstly, the user is met with an option at startup to either encrypt or decrypt

![image](https://github.com/user-attachments/assets/925668cc-4196-46fa-b3b2-bd5ad610f278)

2) After selecting "Encrypter", you must enter the full directory of the file you are working on, for example...

![image](https://github.com/user-attachments/assets/09bcbc6a-55c3-48b1-9571-c4972772b10a)
![image](https://github.com/user-attachments/assets/ba82fe3b-63e2-4630-9855-876314b20439)

4) Then, proceed by typing in the name you would like your encrypted file to take in the command prompt and press enter
5) Lastly, you will get your encryption key / password in this case, to decrypt your files later on:

![image](https://github.com/user-attachments/assets/711a7605-7463-4218-9926-0b5d1927da04)

6) Finally, you have your encrypted file, saved in the same directory! (the .encrypted extension is there purely for decorative purposes and even without the file type, the contents of the file will not be able to be read)

![image](https://github.com/user-attachments/assets/e72369b1-7ee1-4467-8bab-f8bf79b37c07)

7) Upon restarting, and selecting this time, 2-Decrypter, you will be prompted once again to enter the directory of your encrypted file

![image](https://github.com/user-attachments/assets/01ba117c-89f5-46f8-9187-9abe54276849)

8) After entering your decryption key, the program will go on-to decrypt your files and you will once again be back to your original file!

![image](https://github.com/user-attachments/assets/e4bb95b9-31dc-4ddd-86dc-438ad834d939)
![image](https://github.com/user-attachments/assets/7b22c29a-dbda-4a16-9f6b-a5c7392554c6)

# How it could be improved
Currently, all the contents of the file to be read, before being encrypted are stored in a single temporary variable which then gets encrypted and written over a new file. However, with larger file sizes such as for those >500MBs, this may make the program heavily reliant on memory/ram and putting this encryption step in a loop where by, each part of the file is read in small chunks, no matter how large or small the file is would limit the memory usage that may be seen on large files, but at the same time having no impact on the way smaller files are handled, as the temporary variable holding this information will only hold so much data at a given time.
