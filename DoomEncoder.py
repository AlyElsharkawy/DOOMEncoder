import random as r
import EncryptionLib
from time import sleep
import readline
from pyperclip import copy as COPY
from os import get_terminal_size
import time as t

debugBool = False

standardCharacters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",",","!","+","=","/","_","<",">","[","]","@","#","$","%","^","&","*","(",")","-","'",'"',":",";","?","~","\\","|","{","}","`","."," "]

encryptionCharactersPool = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99"]

if debugBool == True:
    print("Len of characters: " + str(len(standardCharacters)))

doomLogo = """
                                                                                
    * ...    ....*#    *. .  ....,.,/   /  * ..,. ., /.**/,.    .  /, .,.  /    
    /... ,. . ,,,. /..#..., ,  . .,.,/./,   , ..*.,  .,../ ..*.  ,*/  .,..,(    
    /./../(((/.,,../*.#..,*/((#(.,.,*( /,**,,***/*.. ,*,.(  .   ..,(,.,* ,*/    
    /,*.*#.. / .*,,/,.#..*//.  (. .,.(.(..,, #...*.,.,*,.(. ./,** (....*.,*/    
    /,.,/#...(,**,*(*,%,/,((..,#.,..*#,(.,..,#..,/.*,.*,*(.,**,*,.,,./*/,./(    
    /,*./%/*,#.,..,(*,%,.*.#,*.#.,/,*#,(.,*,,%,.//,/. /*,(.  *(,,*.**,*,***(    
    (,*,/#/,,#,,,*.#*,%,,,.(#*,%./(#*%/#.**#.%*/#/,,,,**(#*,,,#...,.,.,,(.*(    
    (( / &*(/%*.**,%#/%,,,.(**/%(*#./&/&.**(,&,((/**///*(#***,%%,., ,/% ./((    
    #,.**&#//&**///&/(&////(%*/%,,*.*&*&#*..,&/(#(((((/*#&(//,%,/,/**(%,.&/%    
    %****&#%(*//,(#&((%(#*#(,&,%(,*,/&/&**///&,&((###/,*(&#/((&,&(**,%%/,.*%    
    %/*/**//(//(#(#&#(&#(#(##/%%#*#/%@/&,,***/**%*(/,%#//&//#(&,/%*#&,&/***&    
    &///(######(##@@#*/&@####(%#%@@%#*,(#(&*/(##///@%*./#(&,#(&,*&(&,/&(((,&    
    &*##/%%%%%%@&#(**(/  *(@#(@&*(,(/   /*(((&/*&(/      **/#%%*((%#/*&((((&    
    &###%%&*@((/(/*,        /((/(/         ,.//*            /  */*(/,*&(#(*&    
    &%&%/&/(/(*.*                                              .   *,*&%#%#&    
    &&@##//(/(                                                     #*#(@##(&    
    #(//(*,                                                          /,((#@#    
     (*                                                                 ,*(/    
                                                                                
"""
# Define the list of available commands
commands = ["generate key", "generate combination", "generate hash", "encode", "encrypt", "decode", "decrypt", "exit", "back", "quit"]

# Function to provide autocompletion options
def completer(text, state):
    options = [command for command in commands if command.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

def logoPrinter(string):
    stringArray = string.splitlines()
    for i in stringArray:
        print(i.center(get_terminal_size().columns))
    t.sleep(0.5)

# Set the completer function
readline.set_completer(completer)
readline.parse_and_bind("tab: complete")


def Garble(inputText,encrpytionArray):
    outputText = ""
    for word in inputText:
        for letter in word:
            #finding the index of the letter
            indexNumber = standardCharacters.index(letter)
            outputText += encrpytionArray[indexNumber]
    return outputText

def DeGarble(inputText,encryptionArray):
    outputText = ""
    inputArray = CreateEncrpytionArrayFromString(inputText)
    #getting index number of encrypted input
    if debugBool == True:
        print(f"THIS IS THE INPUT ARRAY {inputArray}")
    for i in inputArray:
        indexNumber = encryptionArray.index(i)
        outputText += standardCharacters[indexNumber]
    return outputText

def CreateStringFromArray(inputArray):
    outputString = ""
    for i in inputArray:
        outputString += inputArray[inputArray.index(i)]
    return outputString

def CreateEncrpytionArrayFromString(inputString):
    stringToUse = str(inputString)
    outputArray = []
    count = len(str(stringToUse))
    iterations = 0
    while iterations < count:
        outputArray.append(stringToUse[iterations: iterations + 2])
        iterations += 2
    return outputArray

def HashMaker():
    numbersArray = encryptionCharactersPool.copy()
    generatedHash = []
    for i in range(95):
        randomNumber = r.randint(0,len(numbersArray) - 1)
        generatedHash.append(numbersArray[randomNumber])
        numbersArray.remove(numbersArray[randomNumber])
    hashString = CreateStringFromArray(generatedHash)
    hexString = hex(int(hashString))
    outputHexString = EncryptionLib.AlyFastEncode(hexString[2:])
    if debugBool == True:
        print(f"Orginal: {hashString}")
    return outputHexString

def UnicodePhaser(inputText):
    returnString = ""
    inputArray = [i for j in inputText.split() for i in (j, ' ')][:-1]
    for word in inputArray:
        if word.isascii() == True:
            returnString += word
        else:
            for letter in word:
                returnString += "|+" + str(ord(letter))
    return returnString

def UnicodeDephaser(inputText):
    returnString = ""
    inputArray =[i for j in inputText.split() for i in (j, ' ')][:-1]
    for word in inputArray:
        if word[:2] != "|+":
            returnString += word
        else:
            unicodeArray = word.split("|+")
            unicodeArray.remove("")
            for letter in unicodeArray:
                returnString += chr(int(letter))
    return returnString

print("\n\n")
print("D  O  O  M    E  N  C  O  D  E  R".center(get_terminal_size().columns))
print("\n")
logoPrinter(doomLogo)
sleep(1)
print("MADE ON 4/11/2022 BY ALY ELSHARKAWY".center(get_terminal_size().columns))
sleep(0.5)
print("THESE ARE THE COMMANDS".center(get_terminal_size().columns))
print("\n\n")
print("BACK ---> Goes back to previous menu".center(get_terminal_size().columns))
print("GENERATE KEY ---> Makes a unique key. The chance of having exact duplicates is 1 in 7.777E+155".center(get_terminal_size().columns))
print("ENCODE ---> Asks for key to encrypt text with.".center(get_terminal_size().columns))
print("DECODE ---> Asks for key to decrypt text with".center(get_terminal_size().columns))
print("QUIT ---> Closes the program".center(get_terminal_size().columns))
while True:
    print("\n")
    userInput = input("Enter command: ")
    if userInput[:12].lower() == "generate key" or userInput[:20].lower() == "generate combination" or userInput[:13].lower() == "generate hash":
        print("Key has been generated and copied to clipboard!")
        generatedKey = HashMaker()
        print(f"Key: {generatedKey}")
        COPY(generatedKey)
        continue
    elif userInput[:6].lower() == "encode" or userInput[:7].lower() == "encrypt":
        if debugBool == True:
            userInput[:7]
        while True:
            encryptionKey = input("Please enter key to encode with: ")
            if encryptionKey[:4].lower() == "back" and len(encryptionKey) == 4:
                print("Going back to main menu")
                break
            elif encryptionKey[:4].lower() == "quit" and len(encryptionKey) == 4:
                print("Closing program")
                quit
            try:
                usableEncryptionKey = EncryptionLib.AlyFastDecode(encryptionKey)
            except:
                print("ERROR: UNICODE values detected.Failed to convert the key into a usable decryption format.")
                continue
            try:
                numberEncryptionKey = int(usableEncryptionKey,16)
            except:
                print("Key is faulty. Could not convert key into a usable decryption format.")
                continue
            realNumberEncryptionKey = ""
            if len(str(numberEncryptionKey)) != 190:
                realNumberEncryptionKey = "0" + str(numberEncryptionKey)
                if len(str(numberEncryptionKey)) != 190:
                    realNumberEncryptionKey = "0" + str(numberEncryptionKey)
            else:
                realNumberEncryptionKey = str(numberEncryptionKey)
            if len(realNumberEncryptionKey) < 190:
                print(f"ERROR: Key is too short (Keys should be 157 or 158 characters long). Current length is {len(encryptionKey)}")
                continue
            elif len(realNumberEncryptionKey) > 190:
                print(f"ERORR: Key is too long (Keys should be 157 or 158 characters long). Current length is {len(encryptionKey)}")
                continue
            if debugBool == True:
                print(f"Original: {realNumberEncryptionKey}")
            try:
                encodingArray = CreateEncrpytionArrayFromString(realNumberEncryptionKey)
                if debugBool == True:
                    print(encodingArray)
                    print(f"Len: {len(encodingArray)}")
            except:
                print("ERROR: How the heck did you get here. You must be nothing but a dirty hacker because so much error handling code exists to prevent this.")
            while True:
                textToEncrypt = input("Please enter text to encrypt with the entered key: ")
                if textToEncrypt[:10].lower() == "change key" or textToEncrypt[:4].lower() == "back":
                    print("Going back to key menu")
                    break
                elif textToEncrypt[:4].lower() == "quit":
                    print("Closing program")
                    quit
                else:
                    garbledText = UnicodePhaser(textToEncrypt)
                    garbledText = Garble(garbledText,encodingArray)
                    if debugBool == True:
                        print(f"Original NonEncryptedText: {garbledText}")
                    #Currently The output is only numbers...we will now encode it with my garbler from Encryption library
                    encryptedGarbledText = EncryptionLib.AlyFastEncode(garbledText)
                    print(f"Output: {encryptedGarbledText}")
                    COPY(encryptedGarbledText)
                    continue

    elif userInput[:6].lower() == "decode" or userInput[:7].lower() == "decrypt":
        while True:
            encryptionKey = input("Please enter key to decode with: ")
            if encryptionKey[:4].lower() == "back" and len(encryptionKey) == 4:
                print("Going back to main menu")
                break
            elif encryptionKey[:4].lower() == "quit" and len(encryptionKey) == 4:
                print("Closing program")
                quit
            try:
                usableEncryptionKey = EncryptionLib.AlyFastDecode(encryptionKey)
            except:
                print("ERROR: UNICODE values detected. Failed to convert the key into a usable decryption format.")
                continue
            try:
                numberEncryptionKey = int(usableEncryptionKey,16)
            except:
                print("Key is faulty. Could not convert key into a usable decryption format.")
                continue
            realNumberEncryptionKey = ""
            if len(str(numberEncryptionKey)) != 190:
                realNumberEncryptionKey = "0" + str(numberEncryptionKey)
                if len(str(numberEncryptionKey)) != 190:
                    realNumberEncryptionKey = "0" + str(numberEncryptionKey)
            else:
                realNumberEncryptionKey = str(numberEncryptionKey)
            if debugBool == True:
                print(f"Original: {realNumberEncryptionKey}")
            if len(realNumberEncryptionKey) < 190:
                print(f"ERROR: Key is too short (Keys should be 157 or 158 characters long). Current length is {len(encryptionKey)}")
                continue
            elif len(realNumberEncryptionKey) > 190:
                print(f"ERORR: Key is too long (Keys should be 157 or 158 characters long). Current length is {len(encryptionKey)}")
                continue
            try:
                encodingArray = CreateEncrpytionArrayFromString(realNumberEncryptionKey)
                if debugBool == True:
                    print(encodingArray)
                    print(f"Len: {len(encodingArray)}")
            except:
                print("ERROR. How the heck did you get here. You must be nothing but a dirty hacker because so much error handling code exists to prevent this.")
            while True:
                textToEncrypt = input("Please enter text to decrypt with the entered key: ")
                if textToEncrypt[:10].lower() == "change key" or textToEncrypt[:4].lower() == "back":
                    print("Going back to key menu")
                    break
                elif textToEncrypt[:4].lower() == "quit":
                    print("Closing program")
                    quit
                else:
                    encryptedDeGarbledText = EncryptionLib.AlyFastDecode(textToEncrypt)
                    if debugBool == True:
                        print(f"The Decrypted but garbled text: {encryptedDeGarbledText}")
                    try:
                        degarbledText = DeGarble(encryptedDeGarbledText,encodingArray)
                        degarbledText = UnicodeDephaser(degarbledText)
                        print(f"Output: {degarbledText}")
                        COPY(degarbledText)
                    except:
                        #this happens because it is 100p95 (all possible key combinations)  we have 95 supported characters out of a possible pool of 100 characters. So, bascially this is a rare error message that means that you found you have an input message that needs an unused character in the key inorder for the message to be decrypted
                        #A fix for this would be to make it 95p95 but that would mean we only have 1.03E + 148 combinatiations instead of  7.777E + 155
                        print("ERROR. Could not decrypt entered message with key. Key or input is faulty. One of them is incompatible with the other.")
                        continue
    elif userInput[0:4].lower() == "back":
        print("Returning to main menu")
        sleep(0.2)
        continue
    elif userInput[0:4].lower() == "quit" or userInput[0:4] == "exit":
        print("Quitting...")
        quit()
    else:
        print("Couldnt understand user input. Continuing to next loop.")
        continue

