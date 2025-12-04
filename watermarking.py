from PIL import Image
import numpy



def get_even_image_array(image_array):
	return image_array - image_array % 2


def convert_text_to_binary(message):
	#return "".join([bin(ord(char))[2:].zfill(21) for char in message])
	
	list_of_bits = []
	for char in message:
		ordinal_char = ord(char)
		binary_char = bin(ordinal_char)[2:]
		binary_paded_char = binary_char.zfill(21)

		list_of_bits.append(binary_paded_char)
	
	return  "".join(list_of_bits)



def watermark_image(image_array, message):
	even_image_array = get_even_image_array(image_array)
	binary_message = convert_text_to_binary(message)

	number_rows, number_cols, number_canals = image_array.shape

	if len(binary_message) > number_rows * number_cols * number_canals:
		print("Attention le message est trop long !")

	index_bit = 0

	for row in range(0, number_rows):
		for col in range(0, number_cols):
			for canal in range(0, number_canals):
				if index_bit == len(binary_message):
					break
				else:
					even_image_array[row][col][canal] += int(binary_message[index_bit])
					index_bit += 1 


	Image.fromarray(even_image_array).save('image_watermarked.png')



def get_text_from_image(watermarked_image_array):
	binary_message = watermarked_image_array.flatten() % 2

	list_of_chars = []

	for index_bit in range(0, len(binary_message), 21):
		binary_char = "".join(str(bit) for bit in binary_message[index_bit: index_bit+21])
		if binary_char == "0"*21:
			break

		ordinal_char = int(binary_char, 2)
		char = chr(ordinal_char)
		
		list_of_chars.append(char)
		


	initial_message = "".join(list_of_chars)
	return initial_message



water_marked_image = Image.open("./image_watermarked.png").convert("RGB")
watermarked_image_array = numpy.array(water_marked_image)
initial_message = get_text_from_image(watermarked_image_array)
print(initial_message)



# image = Image.open("./image.png").convert("RGB")
# image_array = numpy.array(image)

# watermark_image(image_array, message="chocolat")

# number_rows, number_cols, number_canals = image_array.shape

# for row in range(number_rows):
# 	for col in range(number_cols):
# 		print(image_array[row][col])
