%pip install pyscript
from pyscript import document

def Crypter(texte,decaler):
    txt=''
    for lettre in texte:
        if lettre==' ':
            txt+=lettre
        else:
            lettre=ord(lettre.upper())
            lettre-=65
            lettre+=decaler
            lettre%=26
            lettre+=65
            txt+=chr(lettre)
    return txt

def translate(event):
    input_text = document.querySelector("#texte")
    decaler = document.querySelector("#decalage")
    english = input_text.value
    output_div = document.querySelector("#sortie")
    output_div.innerText = Crypter(input_text,decaler)