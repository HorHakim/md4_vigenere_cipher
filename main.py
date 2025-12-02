def cesar_cipher(message, key):

	crypted_message = ""
	for char in message:
		crypted_char = chr((ord(char) + key) % 1_114_112)
		crypted_message += crypted_char

	return crypted_message


crypted_message = cesar_cipher(message="lapin", key=3)
print(crypted_message)