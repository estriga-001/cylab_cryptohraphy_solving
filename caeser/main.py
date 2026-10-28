	#                                                                                                                ▄▄░▀▀▄               ▄▄▄▀▀▀█                                   
	#                                                                                                                █  ▓█                 █   █                                    
	#  ▀▄▄▄▀▀▀▄▄▄▄▄    ▄▀▀▒▀▀▄█▄▄▄▄▄   ▄▀▀█▀▀█▀▄▄     ▄▀▀█▀▀█▀▄▄     ▄▀▀▒▀▀▄█▄▄▄▄▄   ▀▄▄▄▄▄▄▄▀        ▀▄▄▄▀▀▀▄▄▄▄▄   █░░▀█    ▀▄▄▄▄▄▄▄▀    █ ░ █            ▄▀▀█▀▀█▀▄▄     ▀▄▄▄▄▄▄▄▀
	# ██▓██    █▀▓▀▌  █ ░ █   ░█▓██   █ ░▒█  ▒█▓█░   █ ░▒█  ▒█▓█░   █ ░ █   ░█▓██   ██▓██▀██▓█       ██▓██    █▀▓▀▌   ▀▀▀    ██▓██▀██▓██   █░▒░█           █ ░▒█  ▒█▓█░   ██▓██▀██▓█
	#█▓▒▓       ▀▀▀  █░▒░█    █▓▒▓█  █▒░▒░   ░▓▀▀▀  █▒░▒░░  ▀░▀▀▀  █░▒░█    █▓▒▓█  █▓▒▓ ▌ ▐ ▓▒      █▓▒▓       ▀▀▀  ▀█▒▓▒█▀ █▓▒▓     ▓▒▓█  █▒▓▒▄▀▀▓▄▄▄■▄  █▒░▒░   ░▓▀▀▀  █▓▒▓ ▌ ▐ ▓▒
	#█▒░▒▓           █▒▓▒█    █▒░▒░  █▒▓▒█▀■▀▀▀       ▀▀▀▀▀▄▄▄▄▄   █▒▓▒█    █▒░▒░  █▒░▒▓            █▒░▒▓            █▓█▓░  █▒░▒▓   ▓▒░▒█  █▓█▓░  ▐▐░▓█▌▌ █▒▓▒█▀■▀▀▀     █▒░▒▓      
	#█░ ░▓    █░██▄  █▓█▓█    █░ ░▒  █▓█▓░    ▄▄■▄   ▄▄▄▄▄  ▐░▓█▓█ █▓█▓█    █░ ░▒  █░ ░▓            █░ ░▓    █░██▄   █ ░ ▒  █░ ░▓   ▓░ ░█  █ ░ ▒   █▓▒▓█░ █▓█▓░    ▄▄■▄  █░ ░▓      
	# █ ░▒ ▄▄░░▒░▓■   █░▒░ ▄ ▄█ ░ ▓   █ ░▒▄ ▄▒░░▒▓▌ ▐▓▒░░▒▄ ▄▒░ █▀  █░▒░ ▄ ▄█ ░ ▓  ██ ░░             █ ░▒ ▄▄░░▒░▓■   █░▒░▓  ██ ░▒ ▄ ▒░ █   █░▒░▓   █▒░░▒▒  █ ░▒▄ ▄▒░░▒▓▌ ██ ░░      
	#   ▀▀▀■▀▀▀▀▀       ▀▀▀▀▀  ▀■▄█▄    ▀▄▄▄▄▀▀▀▀     ▀▀▀▀▄▄▄▄▀       ▀▀▀▀▀  ▀■▄█▄ ▄▄▀▄▄               ▀▀▀■▀▀▀▀▀    ▄█■▀▀ ▄ █░█░■▄■▄▄▄▀    █▀▀▀    █░▄▄▄▓    ▀▄▄▄▄▀▀▀▀   ▄▄▀▄▄      
	#                                                                                                                       █▒█▒█         ▀▀     ■▀▀▀                               
	#                                                                                                                       █▓▄▓█                                                   
	#                                                                                                                       ▀▀▀▀▀                                                   

	# Made by estriga001 
	# cylab challenge


def caeser_encrypt(text):
	result = ""
	
	for i in range(len(text)):
		# obtain the ascii value using ord, exemplo: h -> 104
		char_position = ord(text[i])
		
		# subtract 97 to have a character from 1 to 26, exemplo: 104(h) - 97 = 7, o h fica na posição 7 do abecedario.
		char_position = char_position - 97 

		# add 3 to the position, as caeser does. h(7) -> k(10)
		new_char_position = char_position + 3

		# make sure that the position does not surpass 26
		new_char_position = new_char_position % 26

		# For example if we got letter "z":
		# ord("z") = 122
		# 122 - 97 = 25
		# 25 + 3 = 28, which passes the limit (0-25) so we want the rest of the division
		# 28 % 26 = 26 + 2 so 26 fits 1 time in 28 + 2 which is our rest. 
		# 2 + 97 = 99 which is 99 in ASCII

		# convet back to ascii values
		new_char_position = new_char_position + 97
		
		# convert ascii value to character and concatenate it to final result
		result = result + chr(new_char_position)
		
	return result

def caeser_decrypt(cipher_text, key=1):
	result = ""
	
	# go through each character of the text in this for loop
	for i in range(len(cipher_text)):

		# Obtain the ascii value using ord
		char_position = ord(cipher_text[i])

		# Subtract 97 to have a character from 1 to 26
		char_position = char_position - 97

		# subtract 3 to the position, as caeser does.
		new_char_position = char_position - key

		# make sure that the position does not surpass 26
		new_char_position = new_char_position % 26

		# convert back to ascii values
		new_char_position = new_char_position + 97

		result = result + chr(new_char_position)

	return result


def brutefore_shift(cipher_text):
	print("Bruteforce table")
	for k in range(1, 26):
		attempt = caeser_decrypt(cipher_text, key=k)
		print(f"Key: {k} -> {attempt}")


def main():
	print("Caesar cipher\n")
	print("(1) Encrypt message")
	print("(2) Decrypt message")

	choice = input("> ").strip()

	if choice == "1":
		text = input("Enter text to encrypt (lowercase only): ").lower().strip()
		encrypted = caeser_encrypt(text)
		print(f"\nFinal Ciphertext: {encrypted}")
	elif choice == "2":
		cipher = input("Enter text to decrypt (lowercase only): ").lower().strip()
		decrypted = brutefore_shift(cipher)
	else:
		print("Invalid option.")

main()