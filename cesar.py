# --- Angel Dijoux - Manon Da-Racha - Camille "..." --- 
# --- projet CESAR NSI ---

#def char_1(char):
#    char_user = chr(ord(char) +3)
#    if char_user > chr(90):
#       char_user_return  = chr(65 + 2)
#       return char_user_return
#   return char_user

#char_user = str(input("Caractère à chiffrer : "))
#print(char_1(char_user))

def char_2(a):
    char_user = a
    if char_user >= chr(65) and char_user <= chr(90): #prends que les valeur ASCII entre 65 et 90
        space_btw_values = ord(char_user)-87 #calcule l'écart pour les caractères X,Y,Z
        char_user_result = chr(ord(char_user)+3) #transforme un caractère en entier pour pouvoir être calculer
        if chr(ord(char_user_result)) > chr(90):
            char_user_result = chr((90-26)+space_btw_values) #utilise l'écart caluculer pour tomber sur la juste valeur
        return char_user_result
    else: 
        return "Veillez choisir une lettre de l'alphabet en majuscule"

entry_user = input("Caractère à chiffre : ")
print(char_2(entry_user))

def char_3(a):
    char_user = [a]
    for i in char_user:
        espace_entre_valeurs = ord(char_user)-87
        char_user_result = chr(ord(char_user)+3)
        if chr(ord(char_user_result)) > chr(90):
            char_user_result = chr((90-26)+espace_entre_valeurs)
        return char_user_result
    return char_user

#a = input("Caract : ")
#print(char_3(a))
