from cryptography.fernet import Fernet
key = Fernet.generate_key() #this is your "password"
cipher_suite = Fernet(key)
clearstring = "this is a string in cleartext!!"
encoded_text = cipher_suite.encrypt(clearstring)
decoded_text = cipher_suite.decrypt(encoded_text)
print("here it is unencrypted (before encrypt" + clearstring)
print("here is the encrypted string " + encoded_text)
print("here it is after decryption " + decoded_text)
