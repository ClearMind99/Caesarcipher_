from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

def cipher_encrypt(plain_text, key):
    encrypted = ""
    for c in plain_text:
        if c.isupper(): 
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower(): 
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.isdigit():   
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)
        else:
            encrypted += c
    return encrypted

def cipher_decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)
        else:
            decrypted += c
    return decrypted


def select_fileEncr():
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    if filename != " ":
        with open(filename) as file:
            readfile = file.read()
            encrypted_message = cipher_encrypt(readfile, 4)
            new_file = open("encrypted.txt", "w")
            new_file.write(encrypted_message)
            new_file.close()
            
        

def select_fileDecr():
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    if filename != " ":
        with open(filename) as file:
            readfile = file.read()
            decrypted_message = cipher_decrypt(readfile, 4)
            new_file = open("decrypted.txt", "w")
            new_file.write(decrypted_message)
            new_file.close()
    

root = Tk()           

root['bg'] = "#fafafa"
root.title("crypting...")
root.geometry("300x250")
root.resizable(width=False, height=False)


openEncrButton = Button(text="Open file to encrypt", command=select_fileEncr)
openEncrButton.place(relx=0.5, rely=0.25, anchor=CENTER)
openEncrButton.pack(expand=True)

openDecrButton = Button(text="Open file to decrypt", command=select_fileDecr)
openDecrButton.place(relx=0.5, rely=0.25, anchor=NE)
openDecrButton.pack(expand=True)

root.mainloop()