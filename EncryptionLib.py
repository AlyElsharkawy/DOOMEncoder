import base64
available_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "X", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "=", "&"]

lang_characters = ["u", "g", "r", "e", "D", "9", "c", "n", "=", "h", "j", "7", "2", "k", "0", "B", "y", "b", "x", "s", "a", "K", "3", "t", "q", "R", "Z", "A", "p", "H", "P", "v", "V", "Y", "C", "1", "J", "N", "L", "O", "X", "M", "d", "f", "z", "U", "S", "F", "T", "W", "G", "E", "X", "&", "o", "I", "m", "w", "4", "5", "6", "l", "8", "Q", "i", " "]
standardCharactersAly = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",",","!","+","=","/","_","<",">","[","]","@","#","$","%","^","&","*","(",")","-","'",'"',":",";","?","~","\\","|","{","}","`"," ","."]
garbledCharactersAly = ["%","D","v","2","/","x","L","&","a","K","X",",","!","#","l","=","5","C","*","W","\\","Y","(","z","4","U","^","f","]","I","7","j","6","+","J","[","F","$","B","m","n","i",")","H","M","Z","<",".","e","V","E","w","`","g","-","o","8",'"',"1",";","3","d","0","c","9","T","@","h","b","t","_","u",":","k","p","|","s","G","'","r","{","A","q","~","N",">","O","?","P","y","}","S","Q","R"," "]
from textwrap import wrap
def KassemFastEncode(message):
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')
	return str(base64_message)

def KassemFastDecode(message):
	base64_message = message
	base64_bytes = base64_message.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	return message_bytes.decode('ascii')

def KassemSemiEncode(text):
	new_text = ""
	for i in text:
		found = False
		for i2 in range(len(available_characters)):
			if (available_characters[i2] == i):
				new_text += lang_characters[i2]
				found = True
				break
		if (found == False): new_text += i
	return new_text

def KassemSemiDecode(text):
	new_text = ""
	for i in text:
		found = False
		for i2 in range(len(lang_characters)):
			if (lang_characters[i2] == i):
				new_text += available_characters[i2]
				found = True
				break
		if (found == False): new_text += i
	return new_text

def AlyFastEncode(inputText):
    outputText = ""
    for word in inputText:
        for letter in word:
            #finding the index of the letter
            indexNumber = standardCharactersAly.index(letter)
            outputText += garbledCharactersAly[indexNumber]
    return outputText

def AlyFastDecode(inputText):
    outputText = ""
    for word in inputText:
        for letter in word:
            #finding the index of the letter
            indexNumber = garbledCharactersAly.index(letter)
            outputText += standardCharactersAly[indexNumber]
    return outputText

def AlyFullEncode(usableInput):
	binaryString = " ".join(format(ord(i), "b") for i in usableInput)
	#making a list of binary letters that will be treated as numbers
	binaryList = binaryString.split()
	hexadecimalString = ""
	#Converting list to hexadecimal
	for i in range(len(binaryList)):
		number = int(binaryList[i],2)
		hexadecimalNumber = hex(number)
		hexadecimalString += str(hexadecimalNumber)
	#removing the 0x part
	hexaPartsList = hexadecimalString.split("0x")
	#final output
	finalHexadecimalString = ""
	for i in hexaPartsList:
		finalHexadecimalString += str(i)
	garbledhexString = AlyFastEncode(AlyFastEncode(AlyFastEncode(AlyFastEncode(AlyFastEncode(AlyFastEncode(AlyFastEncode(finalHexadecimalString)))))))
	return garbledhexString

def AlyFullDecode(usableInput):
	usableInput = AlyFastDecode(AlyFastDecode(AlyFastDecode(AlyFastDecode(AlyFastDecode(AlyFastDecode(AlyFastDecode(usableInput)))))))
	#packing the hexadecimal value into a list of 2 whose elements are 2 chars
	usableInput = wrap(usableInput,2)
	#converting hexadecimal list into binary list
	binaryList = []
	for i in range(len(usableInput)):
		binaryNumber = bin(int(usableInput[i],16))
		binaryNumber = binaryNumber[2:]
		binaryList.append(binaryNumber)
	#converting binaryList to human readable string
	outputString = ""
	for i in range(len(binaryList)):
		number = int(binaryList[i],2)
		character = chr(number)
		outputString += character
	return outputString
