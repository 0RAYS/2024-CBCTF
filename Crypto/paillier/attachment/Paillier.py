from Crypto.Util.number import *
from random import *
from gmpy2 import *
import os
from flag import flag

def generate(length):    
    while 1:
        p = getPrime(length)
        q = getPrime(length)
        if p % 4 == 3 and q % 4 == 3:
            n = p*q
            lemda = (p-1)*(q-1) //2
            break

    while 1:
        x = randint(n//2,n)
        if gcd(x,n) == 1:
            h = -x**2
            h_s = pow(h,n,n**2)
            break
    
    pk = (n,h_s)
    sk = (p,q)
    return pk,sk

def pad(s,l):
    
    d = l-len(s)
    
    return s+os.urandom(d)

def encrypt(m,pk,sk):
    n,h_s = pk
    p,q = sk
    a = randint(1,n//2)
    cp = ((m*n+1)*pow(h_s,a,p**2)) % (p**2)
    cq = ((m*n+1)*pow(h_s,a,q**2)) % (q**2)
    
    return cp,cq


flag = pad(flag,40)
m = bytes_to_long(flag)  

pk,sk = generate(256)
c = encrypt(m,pk,sk)

with open('cipher.txt', 'w') as w:
    w.write(f"pk = {pk}\n")
    w.write(f"sk = {sk}\n")
    w.write(f"c = {c}\n")
            
        
        
        
    