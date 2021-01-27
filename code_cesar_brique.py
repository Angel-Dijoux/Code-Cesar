# --- Angel Dijoux - Manon Da-Rocha - Camille Deslis ---
# --- projet CESAR NSI ---

#PROGRAMME 1

"""def char_2(char_user):
    code_ascii = ord(char_user)+3 #on fait le décalage de 3
    if code_ascii > 90: #quand le caractère Z est dépassé, on revient au début de l'alphabet
        code_ascii = code_ascii-26
    char_user_result = chr(code_ascii) #transforme un caractère en entier pour pouvoir être calculer
    return char_user_result


entry_user = input("Caractère à chiffre : ")
print(char_2(entry_user))"""

#PROGRAMME 2

"""def char_3(message):
    letter=[]
    for char_user in message:
        code_ascii = ord(char_user)+3
        if code_ascii >90:
            code_ascii = code_ascii-26
        char_user_result = chr(code_ascii) #transforme un caractère en entier pour pouvoir être calculer
        letter.append(char_user_result)
        str = ''.join(letter)
    return str
entry_user = str(input("Caractère à chiffre : "))
print(char_3(entry_user))"""

#PROGRAMME 3

"""def char_4(message):
    letter=[]
    for char_user in message:
        code_ascii = ord(char_user)-3
        if code_ascii >90:
            code_ascii = code_ascii-26
        char_user_result = chr(code_ascii) #transforme un caractère en entier pour pouvoir être calculer
        letter.append(char_user_result)
        str = ''.join(letter)
    return str
entry_user = str(input("Caractère à chiffre : "))
print(char_4(entry_user))"""

#PROGRAMME 4
def char_5(message):
    letter=[]
    for char_user in message:
        if char_user==" ":
            letter.append(" ")
        else:
            code_ascii = ord(char_user)+3
            if code_ascii >90:
                code_ascii = code_ascii-26
            char_user_result = chr(code_ascii) #transforme un caractère en entier pour pouvoir être calculer
            letter.append(char_user_result)
        str = "".join(letter)
    return str

entry_user = str(input("Caractère à chiffre : "))
print(char_5(entry_user))