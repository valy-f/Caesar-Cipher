import string
# ENCRYPTION -------------------------------------
def Encryption(txt, key):
    encrypted = ""
    
    for ch in txt:
        #dla wielkich
        if ch.isupper():
            ch_index = ord(ch) - ord('A')
            ch_shifted = (ch_index+key) % 26 + ord ('A')
            ch_moved = chr(ch_shifted)
            encrypted += ch_moved
        #dla malych
        elif ch.islower():
            ch_index = ord(ch) - ord('a')
            ch_shifted = (ch_index+key) % 26 + ord ('a')
            ch_moved = chr(ch_shifted)
            encrypted += ch_moved
        #inne
        elif ch.isidentifier():
            ch_moved = (int(ch)+key) % 10
            encrypted += str(ch_moved)
        else:
            encrypted += ch
    return encrypted

#DECRYPTION --------------------------------------
def Decryption(cipher, key):
    decrypted = ""
    for ch in cipher:
        #dla wielkich
        if ch.isupper():
            ch_index = ord(ch)- ord('A')
            ch_original = (ch_index - key) %26 + ord('A')
            ch_or = chr(ch_original)
            decrypted += ch_or
        #dla malych
        elif ch.islower():
            ch_index = ord(ch) - ord('a')
            ch_original = (ch_index - key) %26 + ord('a')
            ch_or = chr(ch_original)
            decrypted += ch_or
        #inne
        elif ch.isdigit():
            ch_or = (int(ch)-key) %10
            decrypted += str(ch_or)
        else:
            decrypted += ch
    return decrypted

# MENU -----------------------------------------------------------------------------------------------------------
def Menu():
    print("---------------------------------------------------")
    choice = input('|  Hello, welcome to Caesar Encrypter/Decrypter!  |\n|  Tell us what do you want to do:                |\n---------------------------------------------------\n0 - Encrypt my text\n1 - Decrypt my caesar cipher\n[0/1] ? :')
     # ecncryption
    if choice == "0":
       txt = input("Submit your text you want to encrypt: ")
       key = int(input('Set a number of shift key of encryption: '))
       encrypted_text = Encryption(txt, key)
       print("Original text:\n", txt)
       print("Shift pattern: ", int(key))
       print("Ciphered text:\n", encrypted_text)
       Exit() 
     # decryption
    elif choice == "1": 
        cipher = input("Submit your caesar chipher you want to decrypt: ")
        key = int(input('Set a pattern your cipher is schifted with: '))
        decrypted_text = Decryption(cipher, key)
        print("Original cipher:\n", cipher)
        print("Shift pattern: ", key)
        print("Decrypted text:\n", decrypted_text)
        Exit()
    else:
        print("- Try again -")
        Menu()

# EXIT -----------------------------------------------------------------
def Exit():
    exit = input("---------------------------------------------------\n|  1 - Menu\n|  0 - Exit [0/1]: ")
    if exit == "0":
        print("Thanks for using our services, byeee")
        quit()
    elif exit == "1":
        Menu()
    else:
        print("- Try again -\n")
        Exit()

# MAIN ----------------------------------------------------------------------------------------------------------
Exit()



    
    
    
     



   

    






