def cesar_cipher(message, key):

	crypted_message = ""
	for char in message:
		crypted_char = chr((ord(char) + key) % 1_114_112)
		crypted_message += crypted_char

	return crypted_message


def cesar_uncipher(crypted_message, key):
	return cesar_cipher(crypted_message, -key)



crypted_message = cesar_cipher(message="lapin", key=3)
print(crypted_message)

initial_message = cesar_uncipher(crypted_message=crypted_message, key=3)
print(initial_message)