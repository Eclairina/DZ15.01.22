import os
import pyAesCrypt

def crypter(_mode,_filename):
    password = input('Enter passord:')
    buffer = 512 * 1024
    ext = _filename.split('.')

    if(int(_mode)==0):
        pyAesCrypt.encryptFile(_filename,ext[0].lower() + '.ira', password, buffer )

    elif(int(_mode)==1):
        _type = input('Enter Type: ')
        pyAesCrypt.decryptFile(_filename,ext[0].lower() +'.'+ _type, password, buffer )

    os.remove(_filename)    



print(' --Шифрование--')
print('0 - crypt')
print('1 - decrypt')

mode = input('Enter mode: ')
filename=input('Enter file name: ')
crypter(mode, filename)

