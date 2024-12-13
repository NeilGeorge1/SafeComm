import math
import sys
import random
from sympy import mod_inverse

class RSA:
    def __init__(self, message=None):
        self.plain_text = message
        pass

    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def primeGenerator(self):
        while(True):
            num = random.randint(1, 999)
            if self.isPrime(num):
                return num

    def encrypt(self, e, n):
        cipher_text = ''
        for c in self.plain_text:
            plain_num = ord(c)
            cipher_num = pow(plain_num, e, n)
            cipher_c = chr(cipher_num)
            cipher_text += cipher_c

        return cipher_text 

    def decrypt(self, cipher_text, d, n):
        plain_text = ''
        for c in cipher_text:
            cipher_num = ord(c)
            plain_num = pow(cipher_num, d, n)
            plain_c = chr(plain_num)
            plain_text += plain_c

        return plain_text
    
    def generate_keys(self):
        p = self.primeGenerator() # first prime number
        q = self.primeGenerator() # second prime number
        #print(p)
        #print(q)
        e = 65537 # public exponent(key)

        n = p * q # used for encrypting and decrypting
        phi_n = (p - 1) * (q - 1) # totient used for finding private exponent(key)

        d = mod_inverse(e, phi_n)

        """cipher_text = self.encrypt(e, n)
        print(f'Cipher Text-> {cipher_text}')

        plain_text = self.decrypt(cipher_text, d, n)
        print(f'Plain Text-> {plain_text}')"""

        return (e, d)