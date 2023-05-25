# additional documentation at the bottom! scroll down IF YOU DARE

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caeser_algorithm(amount, text):
    cipher_text = ''
    for letter in text:
        if letter == " ":
            cipher_text += letter
        else:
            cipher_text += alphabet[(alphabet.index(letter) + amount) % len(alphabet)]
    return cipher_text
    # this is all there is to it: letter + shift amount, modulo alphabet size. deciphering just flips + to -

def run(): 
    print("Hello! Let's pretend we're back in 50 BCE and work with Caeser Ciphers!")
    encode_check = int(input("Before we start, I gotta know: are we encoding (1) or decoding (2) a cipher? \n"))
    if encode_check == 1:
        word = 'encode'
        direction = 1
        brute_check = 'n'
    elif encode_check == 2:
        word = 'decode'
        direction = -1
        brute_check = input('Deciphering, huh? Do I need to brute force this?\nYes or No: ').lower()
    text = input('Enter the message you want me to {0}.\n'.format(word)).lower()
    if 'y' in brute_check:
        print('Starting with {0}.'.format(text))
        for place, letter in enumerate(alphabet):
            print('Testing if a is shifted to {0}...'.format(letter))
            print('Result: {0}'.format(caeser_algorithm(place * direction, text)))
    else:
        amount = int(input('How many places should I move the letters? Enter a number between 1 and 25.\n'))
        print("Okay! Here's your result:")
        print('Original: {0}\nNew: {1}'.format(text, caeser_algorithm(amount * direction, text)))


if __name__ == "__main__":
    # this is boilerplate in case you try to throw this in other projects, don't worry about it
    run() 


"""
This is a simple implementation of a caeser cipher encryption/decryption algorithm.

The basic format is this: Take each letter in your original message, and replace it with the letter X places after it in the alphabet.

For example, if X is 2, the word "dog" would become the encdoded as "fqi": D -> E -> F, O -> P -> Q, G -> H -> I

To decrypt the cipher, just reverse the process. D <- E <- F, O <- P <- Q, G <- H <- I 

The script assumes the following:
    * input uses only letters from the english alphabet and spaces (" ")
    * case is not important (e.g A is the same as a)
    * the user will type/paste the cleartext or ciphertext into the command line when running the script

There are many ways to optimize, extend, and/or refactor this script, which will be left as an exercise for the reader. Here are a couple of examples:
    * instead of hardcoding the alphabet, take advantage of the ord(character) and chr(ordinal) functions in python to build up your character set at runtime (e.g. ord('a') == 97, and chr(97 + 10) == k. this can get you all the letters :D )
    * allow the user to choose a file for encryption/decryption rather than having to enter it at runtime. bonus points if they can pass it as an argument when calling the script!
    * properly handle edge cases involving more complex input. what happens if there are numbers? or grammatical marks like commas, quoation marks, periods, etc.  
    * think of ways to make the algorithm a little more secure! right now, our brute force solution will ALWAYS lead to a correct result. how would we make that fail?
"""
