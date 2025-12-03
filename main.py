import string

def cesar_cipher(message, key, cipher=True):

	key = key if cipher else -key
	
	crypted_message = ""
	for char in message:
		crypted_char = chr((ord(char) + key) % 1_114_112)
		crypted_message += crypted_char

	return crypted_message


def brute_force_cesar_cipher(crypted_message):
	for potential_key in range(1, 1_114_112):
		potential_message = cesar_cipher(crypted_message, key=potential_key, cipher=False)
		if potential_message[0] in string.ascii_letters:
			print(potential_key)
			print(potential_message)
			print("----------------")


def vigenere_cipher(message, password, cipher=True):

	list_of_keys = [ord(char) for char in password]
	crypted_message = ""

	for index, char in enumerate(message):

		current_key = list_of_keys[index % len(list_of_keys)]
		crypted_char = cesar_cipher(message=char, key=current_key, cipher=cipher)

		crypted_message += crypted_char

	return crypted_message



# crypted_message = cesar_cipher(message="lapin", key=554)
# print(crypted_message)

# initial_message = cesar_cipher(message=crypted_message, key=554, cipher=False)
# print(initial_message)

# brute_force_cesar_cipher(crypted_message)


crypted_message = vigenere_cipher(message="Bonjour, comment ça va ?", password="chocolat123!")
print(crypted_message)

initial_message = vigenere_cipher(message=crypted_message, password="chocolat123!", cipher=False)
print(initial_message)