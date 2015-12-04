alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = "~!@#$%^&*()_-+=`;1234567890{}|[]\:'<>?,./"

key = input("Please choose an encryption key. Key can only contain letters: ")

def has_num(inputString):
	return any(char.isdigit() for char in inputString)

def create_ciphertext_alphabet_from(key):
	ciphertext_alphabet = alphabet
	for i in range(0,len(key)):
		index = ciphertext_alphabet.index(key[i])
		ciphertext_alphabet.append(key[i])
		ciphertext_alphabet.pop(index)
	return ciphertext_alphabet

def valid_key(key):
	if any((c in symbols) for c in key):
    		print("Not a valid key, please try again. Key can only contain letters.")
	else:
     		print("Valid key: Please enter the phrase you would like to encrypt")
     		
def encrypt(word):
	newword = []
	for item in word:
		newword.append(ciphertext_alphabet[alphabet.index(item)])
	return "".join(newword)


##########################
###SOME DIFFERENT STUFF?###
##########################

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = "~!@#$%^&*()_-+=`;1234567890{}|[]\:'<>?,./"

def valid_key(key):
    if any((c in symbols) for c in key):
            print("Not a valid key, please try again. Key can only contain letters.")
    else:
            print("Valid key: Please enter the phrase you would like to encrypt")

def create_ciphertext_alphabet_from(key):
    ciphertext_alphabet = alphabet
    for item in key:
        ciphertext_alphabet.append(item)
        ciphertext_alphabet.remove(item)
    return ciphertext_alphabet

def list_to_string(lst):
    tempString = "["
    for item in lst:
        tempString = tempString + "'" + item + "'" + ", "
    tempString = tempString + "]"
    return tempString


key = input("Please choose an encryption key. Key can only contain letters: ")

ciphertext_alphabet = create_ciphertext_alphabet_from(key)

print ("Your key is" + list_to_string(ciphertext_alphabet))

word = input("Please enter a word you would like to encrypt: ")

def encrypt(word):
    newword = []
    for item in word:
        newword.append(ciphertext_alphabet[alphabet.index(item)])
    return "".join(newword)

encrypted = encrypt(word)
