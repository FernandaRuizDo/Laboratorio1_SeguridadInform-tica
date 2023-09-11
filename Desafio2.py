# Fernanda Ruiz y Rayén Lara
import requests

def desrot15(mensaje):
    diccionario = "abcdefghijklmnopqrstuvwxyz"
    auxiliar = ""
    for i in mensaje:
        auxiliar = auxiliar + diccionario[(diccionario.find(i) - 15) % 26]
    return auxiliar

def desrot7(mensaje):
    diccionario = "abcdefghijklmnopqrstuvwxyz"
    auxiliar = ""
    for i in mensaje:
        auxiliar = auxiliar + diccionario[(diccionario.find(i) - 7) % 26]
    mensaje = auxiliar
    return mensaje


letras = "abcdefghijklmnopqrstuvwxyz"
A = dict(zip(letras, range(len(letras))))
B = dict(zip(range(len(letras)), letras))


def desvig(cifra, contrasena):
    decifrado = ""
    i = 0
    for letra in cifra:
        numero = (A[letra] - A[contrasena[i % len(contrasena)]]) % len(letras)
        decifrado += B[numero]
        i += 1
    return decifrado


url = 'http://finis.malba.cl/GetMsg'
headers = {'Content-Type': 'dppmupsmtqzgbofptafvvtwpgyklheosawwxbkcpqt'}

response = requests.get(url, headers=headers)
mensaje_cifrado = "oemkd lyzqgvqxgptuuinqy nrkkfmnv"


def descifrar_mensaje(mensaje_cifrado):
    mensaje_rot7 = desrot7(mensaje_cifrado)
    
    nueva_contraseña = "aobkqolrzsrigpknkufezioer"
    mensaje_descifrado_vigenere = desvig(mensaje_rot7, nueva_contraseña)
    
    mensaje_descifrado_rot15 = desrot15(mensaje_descifrado_vigenere)
    
    return mensaje_descifrado_rot15


mensaje_descifrado = descifrar_mensaje(mensaje_cifrado)
print("Mensaje Descifrado:", mensaje_descifrado)
