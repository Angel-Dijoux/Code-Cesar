# --- Angel Dijoux - Manon Da-Rocha - Camille Deslis --- 
# --- Projet CESAR NSI --- 

from tkinter import *
import tkinter.messagebox

#-----------------------------------------------------------------------------------------------

def code_cesar_encryp(): #Code de chiffrement
    text = entry_user.get()
    shift = int(entry_shift.get())
    letter = [] #Crée un liste vide où seras stocké le texte
    if text >= chr(65) and text <= chr(90): #prends que les valeur ASCII entre 65 et 90
        if shift <= 0 or shift > 50:
            return tkinter.messagebox.showerror('Code de César', 'Veuillez saisir un décalage correct !' ) #Message d'erreur en cas de mauvais caractère
        else:
            for char_user in text:
                if char_user == " ":
                    letter.append(chr(32)) #Ajoute un espace, quand on en entre un
                else:
                    code_ascii = ord(char_user)+shift #Effectue un décallage inscrit par l'utilisateur
                    if code_ascii > 90: #retourne au débur de l'alphabet
                        code_ascii = code_ascii-26
                    char_user_result = chr(code_ascii) #transforme un caractère en entier pour pouvoir être calculer
                    letter.append(char_user_result)
                str = ''.join(letter) #transforme la liste en chaine de caractère
            return label_resul.configure(text=str)
    return tkinter.messagebox.showerror('Code de César', 'Veillez entrez une majuscule ! ' )#Message d'erreur en cas de mauvais caractère

#-----------------------------------------------------------------------------------------------

def code_cesar_unscramble(): #Code de déchiffrement
    text = entry_user.get()
    shift = int(entry_shift.get())
    letter = [] #Crée un liste vide où seras stocké le texte
    if text >= chr(65) and text <= chr(90): #prends que les valeur ASCII entre 65 et 90
        if shift <= 0 or shift > 50:
            return tkinter.messagebox.showerror('Code de César', 'Veuillez saisir un décalage correct !' )#Message d'erreur en cas de mauvais caractère
        else:
            for char_user in text:
                if char_user == " ":
                    letter.append(chr(32)) #Ajoute un espace, quand on en entre un
                else:
                    code_ascii = ord(char_user)-shift #Effectue un décallage inscrit par l'utilisateur
                    if code_ascii > 90: #retourne au débur de l'alphabet
                        code_ascii = code_ascii-26
                    char_user_result = chr(code_ascii) #transforme un caractère en entier pour pouvoir être calculer
                    letter.append(char_user_result)
                str = ''.join(letter) #transforme la liste en chaine de caractère
            return label_resul.configure(text=str)
    return tkinter.messagebox.showerror('Code de César', 'Veillez entrez une majuscule ! ' )#Message d'erreur en cas de mauvais caractère
    

#-----------------------------------------------------------------------------------------------

windows = Tk()

#Paramètres de base de la fenêtre
windows.title("Code de César") #Nom de la fenêtre
windows.geometry("1080x720") #Taille de base de la fenêtre
windows.minsize(480, 360) #Taille minimal de la fenêtre
windows.iconbitmap("logo.ico") #Icone de la fenêtre
windows.config(background='#2f3136') #Coueleur de font de la fenêtre

#Compartiment pour classer chaque éléments de la fenêtre
frame = Frame(windows, bg='#2f3136')
frame_entry = Frame(windows, bg='#2f3136')
frame_result = Frame(windows, bg='#2f3136')

#Premier texte
label_title = Label(windows, text="Code de César", font=("arial", 25), bg='#2f3136', fg='white')
label_title.pack()

#Zones d'entrées
entry_text = Label(frame_entry,text="Entrez du texte à crypté ou décrypté", font=("arial", 15), bg='#2f3136', fg='white')
entry_text.pack()
entry_user = Entry(frame_entry, font=("arial", 18), bg='#696969',fg='white')
entry_user.pack()
shift_text = Label(frame_entry,text="Saisissez un décallage", font=("arial", 15), bg='#2f3136', fg='white')
shift_text.pack()
entry_shift = Entry(frame_entry, font=("arial", 18), bg='#696969',fg='white')
entry_shift.pack()

#Zone d'affichage 
label_resul = Label(frame_result,font=("arial", 18), bg='#2f3136',fg='white',width=150, height=10 )
label_resul.pack()


#Boutons crypté et décrypté
button_encypt = Button(frame, text="Crypté", font=("arial",15), bg="#6A5ACD" ,fg='white', command=code_cesar_encryp )
button_encypt.grid(row=1, column=1, sticky=E)
button_unscramble = Button(frame, text="Décrypté", font=("arial", 15), bg="#6A5ACD", fg="white", command=code_cesar_unscramble )
button_unscramble.grid(row=1, column=2, sticky=E)

#Barre des menus
menu_bar = Menu(windows)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Quitter", command=windows.quit)
windows.config(menu=menu_bar)

frame_entry.pack(expand=YES)
frame_result.pack(expand=YES)
frame.pack(expand=YES)

windows.mainloop()

#-----------------------------------------------------------------------------------------------