import string

def cesar_cipher(message, key):

	crypted_message = ""
	for char in message:
		crypted_char = chr((ord(char) + key) % 1_114_112)
		crypted_message += crypted_char

	return crypted_message


def cesar_uncipher(crypted_message, key):
	return cesar_cipher(crypted_message, -key)



def brute_force_cesar_cipher(crypted_message):
	for potential_key in range(1, 1_114_112):
		potential_message = cesar_uncipher(crypted_message, key=potential_key)
		if potential_message[0] in string.ascii_letters:
			print(potential_key)
			print(potential_message)
			print("----------------")



crypted_message = cesar_cipher(message="lapin", key=554)
print(crypted_message)

initial_message = cesar_uncipher(crypted_message=crypted_message, key=554)
print(initial_message)

brute_force_cesar_cipher(crypted_message)