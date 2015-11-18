alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

key = input("Please choose an encryption key. Key can only contain letters: ")
print ("Your key is" + key)

def has_num(inputString):
	return any(char.isdigit() for char in inputString)

def create_ciphertext_alphabet_from(key):
	ciphertext_alphabet = alphabet
	for item in range(0,len(key)):
		key.append(ciphertext_alphabet[i])
		key.pop(key[i])
	return ciphertext_alphabet


def valid_key(key)
	if has_num(key) == True:
		return True
	else: 
		return False

def func_a(string):
	reverse_text = ''
	index = len(string) - 1

	while index >=0:
    	reverse_text += string[index]
    	index -= 1
    	
	return reverse_text


def func_b(string):
if len(string) <= 1:
    return True
else:
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

if type == "a":
	func_a(hello)
elif type == "b":
	func_b(hello)
else:
	print("invalid option")


type = input("Would you like to do A or B: ")
