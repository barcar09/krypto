import os, random, struct
from Crypto.Cipher import AES
from Crypto import Random
import sys 

def encrypt_file(key, in_filename, out_filename=None, mode = AES.MODE_CBC, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'
    IV = 16 * '\x00'   
    encryptor = AES.new(key, mode, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)
    while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))
def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
     if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

     with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

if sys.argv[5] == "encrypt":
    encrypt_file(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] )
elif sys.argv[5] == "decrypt":
    decrypt_file(sys.argv[1],  sys.argv[2], sys.argv[3], sys.argv[4])
