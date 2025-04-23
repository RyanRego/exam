import math
def gcd(a, h):
    while h != 0:
        a, h = h, a % h
    return a

# RSA key generation
p = 3
q = 7
n = p * q
e = 2

phi = (p - 1) * (q - 1)
# Find 'e' such that gcd(e, phi) = 1
while gcd(e, phi) != 1:
    e += 1

# Find 'd' such that (d * e) % phi = 1 using Extended Euclidean Algorithm
def mod_inverse(e, phi):
    # Extended Euclidean Algorithm to find modular inverse of e mod phi
    t, new_t = 0, 1
    r, new_r = phi, e
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        raise Exception('No modular inverse')
    if t < 0:
        t = t + phi
    return t

d = mod_inverse(e, phi)

# Encryption
msg = 12 # integer message
print("Message data =", msg)
c = pow(msg, e, n)  # c = (msg^e) % n
print("Encrypted data =", c)

# Decryption
m = pow(c, d, n)  # m = (c^d) % n
print("Original Message Sent =", m)








# ALGORITHM

Sure! Here's the *RSA algorithm explained in simple words as an algorithm* — easy to remember and write in your notebook or exam:

---

### 🔐 RSA Algorithm (In Words)

1. *Start* by selecting two prime numbers — let’s say p and q.

2. Multiply them to get n:
   - n = p × q
   - This n will be used as part of both the public and private keys.

3. Calculate *phi (φ)*, also called Euler's totient:
   - phi = (p - 1) × (q - 1)
   - This helps in generating the keys.

4. Choose a number e that is:
   - Greater than 1
   - Less than phi
   - And *does not divide* phi (i.e., GCD of e and phi is 1)
   - This e will be the public exponent.

5. Use the *Extended Euclidean Algorithm* to find d:
   - d is the *modular inverse* of e with respect to phi
   - Meaning: (d × e) mod phi = 1
   - This d is the private exponent.

6. Now you have:
   - *Public key*: (e, n)
   - *Private key*: (d, n)

7. To *encrypt* a message msg:
   - Use the public key formula:  
     Encrypted = (msg ^ e) mod n

8. To *decrypt* the message:
   - Use the private key formula:  
     Original = (Encrypted ^ d) mod n

9. At the end, the original message is successfully recovered.

---

Would you like this converted into a paragraph too for writing in your file as "working of RSA in brief"?