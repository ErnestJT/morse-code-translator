from morse_alphabet import retrieve_morse_alphabet


MORSE_CODE_ENCODING: dict[str, str] = {char.lower():morse for char, morse in retrieve_morse_alphabet()}
MORSE_CODE_DECODING: dict[str, str] = {morse:char for char, morse in MORSE_CODE_ENCODING.items()}

def encode_to_morse(statement: str) -> str:
    encoded_sentence: list[str] = []
    
    for letter in statement:
        letter = MORSE_CODE_ENCODING.get(letter, letter)
        encoded_sentence.append(letter)
        
    return " ".join(encoded_sentence)

def decode_to_morse(statement: str)-> str:
    words: list[str] = statement.split(" ")
    decoded_sentence: list[str] = []
    
    for word in words:
        letter = MORSE_CODE_DECODING.get(word, word)
        decoded_sentence.append(letter)
        
    return "".join(decoded_sentence)

def main():
    while True:
        encode_or_decode = input('\nInput your method of translation (Encode/Decode): ').upper()
        
        if encode_or_decode == 'EXIT':
            break
        
        if encode_or_decode not in ['ENCODE','DECODE']:
            print('\nInvalid method of translation. Try again!')
            continue
        
        
        user_input = input('\nEnter your input: ')
        
        if encode_or_decode == 'ENCODE':
            result = encode_to_morse(user_input)
        else:
            result = decode_to_morse(user_input)
    
        print(f'Result: {result}')

if __name__ == '__main__':
    main()