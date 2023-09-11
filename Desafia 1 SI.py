# Fernanda Ruiz y Rayén Lara
import requests
import json


def rot15(mensaje):
    diccionario = "abcdefghijklmnopqrstuvwxyz"
    auxiliar = ""
    for i in mensaje:
        auxiliar = auxiliar + diccionario[(diccionario.find(i) + 15) % 26]
    return auxiliar

def rot7(mensaje):
    diccionario = "abcdefghijklmnopqrstuvwxyz"
    auxiliar = ""
    for i in mensaje:
        auxiliar = auxiliar + diccionario[(diccionario.find(i) + 7) % 26]
    mensaje = auxiliar
    return mensaje

letras = "abcdefghijklmnopqrstuvwxyz"

A = dict(zip(letras, range(len(letras))))
B = dict(zip(range(len(letras)), letras))

def vigenere(mensaje, contrasena):
    cifrado = ""
    i = 0
    for letra in mensaje:
        numero = (A[letra] + A[contrasena[i % len(contrasena)]]) % len(letras)
        cifrado += B[numero]
        i += 1
    return cifrado

def cifrar_mensaje(mensaje):
    mensaje_rot7 = rot7(mensaje)
    print("Cifrado Rot(7): ", mensaje_rot7)
    contraseña = "cvqnoteshrwnszhhksorbqcoas"
    mensaje_cifrado_vigenere = vigenere(mensaje_rot7, contraseña)
    print("cifrado Vigenere: ", mensaje_cifrado_vigenere )
    mensaje_cifrado_rot15 = rot15(mensaje_cifrado_vigenere)
    return  mensaje_cifrado_rot15

mensaje_cifrado = cifrar_mensaje("descifrado")
print(mensaje_cifrado)

url = 'http://finis.malba.cl/SendMsg'
headers = {'Content-Type': 'text/plain'}
data = {'msg': mensaje_cifrado}
data_json = json.dumps(data)

response = requests.post(url, headers=headers, data=data_json)
print(response.text)
