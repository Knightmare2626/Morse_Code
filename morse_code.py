# short mark, dot or dit ( . ): "dit duration" is one time unit long
# long mark, dash or dah ( - ): three time units long
# inter-element gap between the dits and dahs within a character: nothing
# short gap (between letters): " "
# medium gap (between words): /

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

letterSeparator = ' '

def findInDict(morseLetter, morse_dict):
    for letter, morse_code in morse_dict.items():
        if (morse_code == morseLetter):
            return letter
    return None

def convertToMorse(messageInEnglish)-> str:
    messageInMorseCode = ""
    for c in messageInEnglish:
        messageInMorseCode += morse_dict[c] + letterSeparator
    return messageInMorseCode


def convertToEnglish(messageInMorseCode)-> str:
        messageInEnglish = ""
        morseLetter = ""
        for c in messageInMorseCode:
            if (c == letterSeparator or c == '\n' or c == 'r'): 
                if findInDict(morseLetter, morse_dict) != None:
                    messageInEnglish += findInDict(morseLetter, morse_dict)
                    morseLetter = ""
                else:
                    print(morseLetter + "Error")
            else:
                morseLetter += c
        return messageInEnglish


print("Welcome to Morse-Code generator and translator")
my_input: str = input("\nIf you want to translate from morse code to english then enter T"
              "\nIf you want to generate morse code from english then enter G: ").upper()

if my_input == 'G':
    messageInEnglish: str = input("Enter the message to encode: ")
    print(convertToMorse(messageInEnglish.upper()))
elif my_input == 'T':
    messageInMorse:str = input("Enter the message to decode: ")
    print(convertToEnglish(messageInMorse.upper()))
else: print("Enter valid input :(")