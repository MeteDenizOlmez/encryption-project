from cryptography.fernet import Fernet
import os

print("***************************************************************************************************************************************************")
print("CRYPTOGRAPHY TOOL v0.0.1 - (c) 2024")
print("-> Mete Deniz Olmez")
print("***************************************************************************************************************************************************")


def encrypter():
    file_path = input("Enter the file directory (in the format e.g. --> C:\\Users\\Username\\Path\\To\\File.txt): ")
    os.path.normpath(file_path)
    temp_tuple = os.path.split(os.path.abspath(file_path))
    file_name = temp_tuple[1]

    with open(file_path, "rb") as f:
        data = f.read()
        f.close()
    print("File successfully read!")
    new_file_name = input("What would you like your file to be named: ")
    print("Starting Encryption process... (Do not close this window!)")
    new_file_path = os.path.dirname(os.path.abspath(file_path))
    new_file_path = os.path.join(new_file_path, f"{new_file_name}.encrypted")
    print("[INFO] empty file generated...")
    print("[INFO] encryption process begun...")
    key = Fernet.generate_key()
    
    f_key = Fernet(key)
    encrypted_data = f_key.encrypt(data)

    with open(new_file_path, "wb") as f:
        decoded_data_encrypted = encrypted_data.decode()
        tbw = f"{file_name}\n{decoded_data_encrypted}"
        f.write(str.encode(tbw))
        f.close()
    
    print("Complete!")
    print(f"Here is your key, (/password) NOTE IT DOWN: {key.decode()}")
    input("Press any key to exit...")

def decrypter():
    file_path = input("Enter the file directory (in the format e.g. --> C:\\Users\\Username\\Path\\To\\File.txt): ")

    #get og file name back
    with open(file_path, "r") as f:
        line1 = f.readline()
        og_file_name = f"DECRYPTED.{line1}"
        f.close()

    with open(file_path, "rb") as f:
        data = f.readlines()[1:]
        #print(data)
        f.close()
    print("File successfully read!")
    new_file_name = og_file_name
    print("Starting Decryption process... (Do not close this window!)")
    new_file_path = os.path.dirname(os.path.abspath(file_path))
    new_file_path = os.path.join(new_file_path, f"{new_file_name}")
    print("[INFO] empty file generated...")
    
    user_key = input("PLEASE ENTER YOUR ENCRYPTION KEY: ")

    print("[INFO] if key is correct, decryption process has begun...")

    str.encode(user_key)
    f_key = Fernet(user_key)

    #print(data)
    #print("\n")
    data = b"".join(data)
    #print(data)
    #print("\n")
    data = data.decode()
    #print(data)
    #print("\n")
    #data = bytes(data)
    #data = data.decode()

    decrypted_data = f_key.decrypt(str.encode(data))
    
    new_file_path = new_file_path.rstrip(new_file_path[-1])

    with open(new_file_path, "wb") as f:
        decoded_data_decrypted = decrypted_data
        #str.encode(decoded_data_decrypted)
        f.write(decoded_data_decrypted)
        f.close()
    
    print("Complete!")
    input("Press any key to exit...")

choice = input("1 - Encrypter, 2 - Decrypter : ")
if choice == "1":
    encrypter()
elif choice == "2":
    decrypter()
else:
    print("Ensure you select the correct option!")
    input("Press any key to exit...")