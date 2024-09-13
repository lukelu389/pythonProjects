# shift cipher
# how to do a signature,
# hot to improve
import random
import hashlib

# this number must be a prime number
mod = 10007


# only works if < 1,114,111, the bound of the chr()

# def generate_key(mod):
#     return random.randint(1, mod - 1)
#
#
# # < 9000
#
#
# def mod_inverse(a, m):
#     m0, x0, x1 = m, 0, 1
#     if m == 1:
#         return 0
#     while a > 1:
#         q = a // m
#         m, a = a % m, m
#         x0, x1 = x1 - q * x0, x0
#     if x1 < 0:
#         x1 += m0
#     return x1


# def generate_valid_key(mod):
#     while True:
#         key = random.randint(1, mod - 1)
#         if gcd(key, mod) == 1:
#             return key
#
#


# def hash_signature(data):
#     return int(hashlib.sha256(data.encode('utf-8')).hexdigest(), 16) % mod
#
#
# def encryption(msg, key):
#     signature = 0
#     encrypted_msg = []
#     for char in msg:
#         shifted_value = (ord(char) + key) % mod
#         encrypted_value = (shifted_value * key) % mod
#         encrypted_msg.append(chr(encrypted_value))
#
#         # signature = (signature + encrypted_value) % mod
#         signature = hash_signature(''.join(encrypted_msg))
#     return ''.join(encrypted_msg) + chr(signature)
#
#
# def decryption(ciphertext, key):
#     signature = ord(ciphertext[-1])
#     encrypted_msg = ciphertext[:-1]
#     decrypted_msg = []
#     try:
#         inv_key = mod_inverse(key, mod)
#     except ZeroDivisionError:
#         raise ValueError("Invalid key: Key must be coprime with the modulus.")
#
#     for char in encrypted_msg:
#         encrypted_value = ord(char)
#         shifted_value = (encrypted_value * inv_key) % mod
#         decrypted_value = (shifted_value - key) % mod
#         decrypted_msg.append(chr(decrypted_value))
#
#     # expected_signature = sum(ord(c) for c in encrypted_msg) % mod
#     expected_signature = hash_signature(encrypted_msg)
#     if expected_signature == signature:
#         return ''.join(decrypted_msg)
#     else:
#         return "Signature verification failed"
#
#     # simpler decryption method
#     # for char in encrypted_msg:
#     #     shifted_value = (ord(char) - key) % mod
#     #     decrypted_msg.append(chr(shifted_value))
#     # expected_signature = sum(ord(c) for c in encrypted_msg) % mod
#     # if expected_signature == signature:
#     #     return ''.join(decrypted_msg)
#     # else:
#     #     return "Signature verification failed"
#
#
# # key = generate_valid_key(256)
# #
# #
# # message = "Hello, World! @123"
# # print(f"Original message: {message}")
# #
# # encrypted_message = encryption(message, key)
# # print(f"Encrypted message: {encrypted_message}")
# #
# # decrypted_message = decryption(encrypted_message, key)
# # print(f"Decrypted message: {decrypted_message}")
#
#
# # make more keys one modular scheme, these keys follows one modular scheme
# # try to break scheme knowing keys from cipher text
# # generate 10 cipher text and find out the key and scheme
# # generate_valid_key() parameter taken must be < 1,114,111
# num_keys = 10
# keys = [generate_key(mod) for _ in range(num_keys)]
#
# message = "Hello, World! @123"
# print(f"Original message: {message}")
#
# ciphertexts = []
# for key in keys:
#     encrypted_message = encryption(message, key)
#     ciphertexts.append((key, encrypted_message))
#     print(f"Encrypted message with key {key}: {encrypted_message}")
#
#
# def break_scheme(ciphertexts, original_message):
#     for key, ciphertext in ciphertexts:
#         decrypted_message = decryption(ciphertext, key)
#         if decrypted_message == original_message:
#             print(f"Key {key} successfully decrypted the message: {decrypted_message}")
#         else:
#             print(f"Key {key} failed to decrypt the message correctly.")
#
#
# break_scheme(ciphertexts, message)
#

# math + project
# implement matrix multiplication on the project and try to do the inverse, multiply with the multiplicative inverse

# code:
# making encryption schemes with hash functions
# public key, private key, rsa scheme

# RSA
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
#
# def mod_inverse(e, phi):
#     m0, y, x = phi, 0, 1
#     while e > 1:
#         q = e // phi
#         phi, e = e % phi, phi
#         y, x = x - q * y, y
#     if x < 0:
#         x += m0
#     return x
#
#
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# def generate_prime_candidate(length):
#     p = random.getrandbits(length)
#     p |= (1 << length - 1) | 1
#     return p
#
#
# def generate_prime_number(length=1024):
#     p = 4
#     while not is_prime(p):
#         p = generate_prime_candidate(length)
#     return p
#
#
# def generate_keypair(length):
#     p = generate_prime_number(length)
#     q = generate_prime_number(length)
#     n = p * q
#     t = (p - 1) * (q - 1)
#     e = random.randrange(1, t)
#     g = gcd(e, t)
#     while g != 1:
#         e = random.randrange(1, t)
#         g = gcd(e, t)
#     d = mod_inverse(e, t)
#     return (e, n), (d, n)
#
#
# def encrypt(public_key, plaintext):
#     e, n = public_key
#     ciphertext = [pow(ord(char), e, n) for char in plaintext]
#     return ciphertext
#
#
# def decrypt(private_key, ciphertext):
#     d, n = private_key
#     plaintext = [chr(pow(char, d, n)) for char in ciphertext]
#     return ''.join(plaintext)
#
#
# # 16 bits
# # 32 bits works fine, but 64 or higher doesn't
# key_length = 16
# public_key, private_key = generate_keypair(key_length)
#
# message = "Hello RSA!"
# print("Original message:", message)
#
# encrypted_message = encrypt(public_key, message)
# print("Encrypted message:", encrypted_message)
#
# decrypted_message = decrypt(private_key, encrypted_message)
# print("Decrypted message:", decrypted_message)

# matrix multiplication method
# def matrix_multiply(A, B, mod):
#     result = [[0] * len(B[0]) for _ in range(len(A))]
#     for i in range(len(A)):
#         for j in range(len(B[0])):
#             for k in range(len(B)):
#                 result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod
#     return result
#
#
# def matrix_determinant(A, mod):
#     if len(A) == 2:
#         return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % mod
#     determinant = 0,
#     for c in range(len(A)):
#         sub_matrix = [[A[r][col] for col in range(len(A)) if col != c] for r in range(1, len(A))]
#         determinant = (determinant + ((-1) ** c) * A[0][c] * matrix_determinant(sub_matrix, mod)) % mod
#     return determinant


# how bitcoin works, hash to protect signature is very similar to login methods
# look into hash functions and perhaps develop one


# try to build and understand bitcoin ledger
# writing a ledger, hashing signature
# the hash function should be simpler and self-written
# https://www.enjoyalgorithms.com/blog/introduction-to-hash-functions
# https://en.wikipedia.org/wiki/SHA-2


def simple_hash_function(data, mod=256):
    hash_value = 0
    for char in data:
        hash_value = (hash_value ^ ord(char)) * (hash_value << 5)
        hash_value = hash_value % mod
    return hash_value


def custom_encrypt(message, key, mod=256):
    encrypted_message = []
    hash_value = simple_hash_function(message, mod)

    for char in message:
        encrypted_char = (ord(char) + key + hash_value) % mod
        encrypted_message.append(chr(encrypted_char))

    encrypted_message.append(chr(hash_value))
    return ''.join(encrypted_message)


def custom_decrypt(encrypted_message, key, mod=256):
    hash_value = ord(encrypted_message[-1])
    encrypted_message = encrypted_message[:-1]
    decrypted_message = []

    for char in encrypted_message:
        decrypted_char = (ord(char) - key - hash_value) % mod
        decrypted_message.append(chr(decrypted_char))

    return ''.join(decrypted_message)

# key = 31
# message = "Hello, World!"
# print(f"Original message: {message}")
#
# encrypted_message = custom_encrypt(message, key)
# print(f"Encrypted message: {encrypted_message}")
#
# decrypted_message = custom_decrypt(encrypted_message, key)
# print(f"Decrypted message: {decrypted_message}")

# recreate the bitcoin system
# Ethereum

# ethereum has something called SMART CONTRACT

# bitcoin: Turing Incomplete

# ethereum: uses solidity, it is platform, not currency, immutable upon deployment,
# harder to secure due to scalability and complexity
# hash function : Keccak-256

# Ethereum addresses are unique identifiers that are derived from public keys or contracts using the Keccak-256
# one-way hash function.

# https://www.oreilly.com/library/view/mastering-ethereum/9781491971932/ch04.html#:~:text=Ethereum%20uses%20the%20Keccak%2D256%20cryptographic%20hash%20function%20in%20many%20places.


# dictionary usually take bigger storage but good a removing but bad at access and traversal
# arrays are terrible at removing items but good at access

# python hash: fast but not secure
# https://www.investopedia.com/terms/p/proof-work.asp#:~:text=Proof%20of%20work%20(PoW)%20is%20a%20decentralized%20consensus%20mechanism%20that,a%20reward%20for%20work%20done.

# try to invert the hash function

# smart contract is strict
# what if there is something wrong with the contract,
# is smart contract a feature of crypto or they are separate
# https://hedera.com/learning/smart-contracts/smart-contract-use-cases
# https://security.stackexchange.com/questions/38166/methods-used-to-reverse-a-hash
# what is Rainbow Table
#
# https://www.fool.com/terms/p/proof-of-work/
