""" ====== About Me ======
Name: ShiftBruteForce
Author: Keith Martin
Version: 1.02
Description: Shifts a string n times through the alphabet
             produces 25 result sets. One for each shift
             in the english alphabet.
"""

enPhabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']
newPhabet = []
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print('Shift Cipher Brute Force\n====By: Keith Martin====\n')
sCipherText = input("Enter ciphertext:")


for h in range(0, 26): #Loop for 25 shifts
    char = ''
    newPhabet.clear()
    for i in range(0, len(sCipherText)): #Loop to detect string match
        for j in range(0, 26): #Loop to compare string variable i
            if enPhabet[j] == sCipherText[i] and h != 0:
                if j + h <= len(enPhabet) - 1:
                    char = enPhabet[j + h]
                    newPhabet.append(char)
                else:
                    k = ((j + h) % 26)
                    char = enPhabet[k]
                    newPhabet.append(char)

    # Print Each Subset (Should be 25 for 25 shifts 'h')
    if not len(newPhabet) == 0:
        sResult = ''.join(newPhabet)
        sPost = str(h)
        print(sPost + ' - ' + sResult)
