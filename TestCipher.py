#  File: TestCipher.py

#  Description: This program encodes and decodes given text using either substitution cipher or a vignere cipher
# methods.

#  Student Name: Basilio Bazan

#  Student UT EID:bb36366

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 09/09/2018

#  Date Last Modified: 09/10/2018

# takes a single string as input parameter and returns a string
def substitution_encode ( strng ):
    string = list(strng)
    cipher = ['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u',
              'j', 'm', 'i', 'k', 'o', 'l', 'p']
    newstring = ""
    for x in range(len(string)):
        if ord(string[x]) >= ord('a') and ord(string[x]) <= ord('z'): #Checks is character falls within a-z
            ind = ord(string[x]) - ord('a')
            newstring += cipher[ind]
        else:  #Passes non a-z characters through to the encoded string
            newstring += string[x]
    return newstring

# takes a single string as input parameter and returns a string
def substitution_decode(strng):
    string = list(strng)
    cipher = ['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u',
              'j', 'm', 'i', 'k', 'o', 'l', 'p']
    decodestring = ""
    for x in range(len(string)):
        if ord(string[x]) >= ord('a') and ord(string[x]) <= ord('z'): #Checks is character falls within a-z
            ind = cipher.index(string[x])
            decodestring += chr(ord('a')+ ind)
        else:  #Passes non a-z characters through to the encoded string
            decodestring += string[x]
    return decodestring

#rotates the Vignere Chipher when new passphrase index
def rotate(letter, rot):
    shift = 97 if letter.islower() else 65
    return chr((ord(letter) + rot - shift) % 26 + shift)

# takes two strings as input parameter and returns a string
def vigenere_encode(strng, passwd):
    string = strng
    passp = passwd
    start = 0
    coded = ""
    for let in string:
        rot = ord(passp[start]) - ord('a')
        if ord(let) >= ord('a') and ord(let) <= ord('z') and ord(passp[start]) >= ord('a') \
                and ord(passp[start])<= ord('z'):
            coded += rotate(let, rot)
            if start == (len(passp) - 1):
                start = 0
            else:
                start += 1
        else:
            coded += let

    return coded

#rotates the Vignere Chipher when new passphrase index
def unrotate(letter, rot):
    shift = 97 if letter.islower() else 65
    return chr((ord(letter) - rot - shift) % 26 + shift)

# takes two strings as input parameter and returns a string
def vigenere_decode(strng, passwd):
    string = strng
    passp = passwd
    start = 0
    coded = ""
    for let in string:
        rot = ord(passp[start]) - ord('a')
        if ord(let) >= ord('a') and ord(let) <= ord('z') and ord(passp[start]) >= ord('a') \
                and ord(passp[start]) <= ord('z'):
            coded += unrotate(let, rot)
            if start == (len(passp) - 1):
                start = 0
            else:
                start += 1
        else:
            coded += let
    return coded

def main():
    # open file for reading
    in_file = open("./cipher.txt", "r")

    # print header for substitution cipher
    print ("Substitution Cipher")
    print ()

    # read line to be encoded
    line = in_file.readline()
    line = line.strip()
    line = line.lower()

    # encode using substitution cipher
    encoded_str = substitution_encode(line)

    # print result
    print("Plain Text to be Encoded: " + line)
    print("Encoded Text: " + encoded_str)
    print()

    # read line to be decoded
    line = in_file.readline()
    line = line.strip()
    line = line.lower()

    # decode using substitution cipher
    decoded_str = substitution_decode(line)

    # print result
    print("Encoded Text to be Decoded: " + line)
    print("Decoded Plain Text: " + decoded_str)
    print()

    # print header for vigenere cipher
    print("Vigenere Cipher")
    print()

    # read line to be encoded and pass phrase
    line = in_file.readline()
    line = line.strip()
    line = line.lower()

    passwd = in_file.readline()
    passwd = passwd.strip()
    passwd = passwd.lower()

    # encode using vigenere cipher
    encoded_str = vigenere_encode(line, passwd)

    # print result
    print("Plain Text to be Encoded: " + line)
    print("Pass Phrase (no spaces allowed): " + passwd)
    print("Encoded Text: " + encoded_str)
    print()

    # read line to be decoded and pass phrase
    line = in_file.readline()
    line = line.strip()
    line = line.lower()

    passwd = in_file.readline()
    passwd = passwd.strip()
    passwd = passwd.lower()

    # decode using vigenere cipher
    decoded_str = vigenere_decode(line, passwd)

    # print result
    print("Encoded Text to be Decoded: " + line)
    print("Pass Phrase (no spaces allowed): " + passwd)
    print("Decoded Plain Text: " + decoded_str)
    print()

    # close file
    in_file.close()

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
