import string
from typing import Collection

def mirror_cipher(message, key=string.ascii_lowercase):
    key = key.strip()
    message = message.lower()
    encrypted_msg = ''
    
    for i in message:
        if i in key:
            index = key.index(i)
            reversed_key = key[::-1]
            encrypted_msg += reversed_key[index]
        else:
            encrypted_msg += i

    return encrypted_msg

# print(mirror_cipher('Hello World', 'ihatecodingdfajkfhldsfd'))
# print(mirror_cipher("Mubashir Hassan", "edabitisamazing"), "tuzishar hissid")
# print(mirror_cipher("Matt MacPherson"), "nzgg nzxksvihlm")
# print(mirror_cipher("Airforce is best", "pilot"), "aorfirce os besp")
# print(mirror_cipher("hello"), "svool")
# print(mirror_cipher("goodbye"), "tllwybv")
# print(mirror_cipher("ngmlsoor"), "mtnohlli")
# print(mirror_cipher("gsrh rh z hvxivg"), "this is a secret")
# print(mirror_cipher("hello", "abcdefgh"), "adllo")
# print(mirror_cipher("goodbye", ""), "goodbye")
# print(mirror_cipher("this is a secret", " *"), "this*is*a*secret")

alphabet = string.ascii_lowercase
# def alphabet_index(alphabet, string):
#     string = string.lower()
#     res = ''
#     arr = []
#     for i in string:
#         index = alphabet.index(i)
#         arr.append(index)

#     max_ = arr.max() + 1

#     return str(max_ + 1) + alphabet[max_]

# print(alphabet_index(alphabet, ''))

def longest_abecedarian(lst):
    abecedarian = []
    for word in lst:
        temp = sorted(word)
        if "".join(temp) == word:    
            abecedarian.append(word)
    return max(abecedarian or [""], key=lambda x: len(x))

def num_type(num):
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
    sum_ = sum(factors)
    if sum_ == num:
        return 'Perfect'
    factors.clear()
    for j in range(1, sum_):
        if sum_ % j == 0:
            factors.append(j)
    if sum(factors) == num:
        return 'Amicable'
    return 'Neither'


from collections import Counter
        
# def palindrome_sieve(lst):
#     bruh = []
#     for i in lst:
#         if len(i) % 2 == 0: #even
#             bruh.append(i)
#             if Counter(bruh).values() % 2 == 0:


    ## a number must occurs twice if length is even
    ## a number must occurs twice expect one number if length is odd

def true_equations(lst):
    res = []
    for e in lst:
        left, right = e.split('=')
        if eval(left) == int(right):
            res.append(e)
    return res

print(true_equations(["82/41=2", "21-17=3", "3+99=2", "9*9=81","7*6=42","101+10=111","2*3=5","143/11=13"]))