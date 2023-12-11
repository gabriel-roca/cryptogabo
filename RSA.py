from sympy import isprime, mod_inverse
import random
import math

#This is a basic RSA program, i.e. the numbers aren't TOO big

#Generate big primes P, Q, and create N
def generatePRIME(bits=1024):
    lowerBound = 2**(bits-1)
    upperBound = 2**bits-1

    while True:
        maybePrime = random.randint(lowerBound, upperBound)
        if isprime(maybePrime):
            return maybePrime

P = generatePRIME(1024)
Q = generatePRIME(1024)
N = P*Q

#This is the code that only the creator of N knows
code = (P-1)*(Q-1)

#Make a number "e" coprime to the "code": (P-1)(Q-1)
def generateRelativelyPrimE():
    lowerBound = 100
    upperBound = 200

    while True:
        e = random.randint(lowerBound, upperBound)
        if math.gcd(e, code) == 1:
            return e
        
e = generateRelativelyPrimE()
        
print(f'N = {N}')
print(f'e = {e}')

#Message you want to send, say m
message = input("Input the message you want to send: ")
try:
    m = int(message)
except ValueError:
    print("Please input an integer.")
    exit()

if m >= N:
    print("m needs to be less than N.")
    exit()

print(f'(the message is m = {m})')

print('So realistically, you will send "c", which is equal to m^e (mod N)')

#Creating the "password"
#we set ye = 1 mod(code), and solve for y
y = mod_inverse(e, code)

#Create c
c = pow(m,e,N)
print(f'Thus, the encoded number "I" will receive is: c = {c}')

#Decrypt c into the original message, m
print('Now, decrypting c...')
d = pow(c,y,N)

#print('Hopefully m = d.') lol

print(f'Output: The encrypted message, m = {m}, and the decrypted message, d = {d}')