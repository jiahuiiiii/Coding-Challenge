class Test:
    @classmethod
    def assert_equals(self, v1, v2, message=""):
        print(v1, '<>', v2)
        assert v1 == v2, message or 'two val not equal lol'

    @classmethod
    def assert_not_equals(self, v1, v2, message=""):
        print(v1, '<!>', v2)
        assert v1 != v2, message or 'two val not equal lol'

def can_give_blood(f, u):
    if f == u or f == 'O-':
        return True
    elif f == 'O+':
        if u[-1] == '+':
            return True
    elif f[0] == u[0] and f[1] == '-':
        return True
    return False
def can_give_blood_nice(donor, receiver):
    return not(donor[-1] == "+" and receiver[-1] != "+") and (donor[:-1] in receiver[:-1] or donor[:-1] == "O")

# tests = [
# 	(("O+", "A+"), True),
# 	(("A-", "B-"), False),
# 	(("A-", "AB+"), True),
# 	(("AB-", "B-"), False),
# 	(("AB+", "A+"), False),
# 	(("O-", "A-"), True),
# 	(("A-", "O-"), False),
# 	(("O+", "AB-"), False),
# 	(("O-", "AB+"), True),
# 	(("AB+", "AB+"), True),
# 	(("O+", "O-"), False),
# ]
	
# for test in tests:
# 	print("Input: " + str(test[0]))
# 	Test.assert_equals(can_give_blood(*test[0]), test[1])
import string

def move(s):
    al = string.ascii_lowercase
    ans = []
    for i in s:
        ans.append(al[al.index(i) + 1])
    return ''.join(ans)

# Test.assert_equals(move("hello"), "ifmmp")
# Test.assert_equals(move("lol"), "mpm")
# Test.assert_equals(move("bye"), "czf")
def mubashir_cipher(message):
    key = [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
    return "".join(dict(key+[i[::-1] for i in key])[i] if i.isalpha() else i for i in message)
    # [i[::-1] for i in key] reverse every single list in key
    # key+[i[::-1] for i in key] will return a list with 26 nester list
    # dict(key+[i[::-1] for i in key]) will return 26 key value pair
    # dict(key+[i[::-1] for i in key])[i] will return the value of i 

# Test.assert_equals(mubashir_cipher("mubashir is not amazing"), "cegkvxzy zv ljf kckizlb")
# Test.assert_equals(mubashir_cipher("cegkvxzy zv ljf kckizlb"), "mubashir is not amazing")
# Test.assert_equals(mubashir_cipher("edabit is amazing !"), "uqkgzf zv kckizlb !")
# Test.assert_equals(mubashir_cipher("%$ &%"), "%$ &%")
# Test.assert_equals(mubashir_cipher("~!@#$%^&*()_+= -0 98 76 54 3 2 1"), "~!@#$%^&*()_+= -0 98 76 54 3 2 1")
# Test.assert_equals(mubashir_cipher("matt && is amazing"), "ckff && zv kckizlb")
# Test.assert_equals(mubashir_cipher("evgeny sh is amazing"), "usbulr vx zv kckizlb")
# Test.assert_equals(mubashir_cipher("usbulr vx zv kckizlb"), "evgeny sh is amazing")
# Test.assert_equals(mubashir_cipher("airforce needs me ?"), "kzytjymu luuqv cu ?")
# Test.assert_equals(mubashir_cipher("pakistan is love !"), "wkazvfkl zv njsu !")

def pascal_triangle(layer):
    ans = [[1]]
    for i in range(1, layer):
        ans.append([])
        ans[i].append(1)
        for j in range(1, i):
            ans[i].append(ans[i-1][j-1] + ans[i-1][j])
        if layer != 0:
            ans[i].append(1)
    return ans

def pascal_triangle(layer):
    res = [[1]]
    for i in range(1, layer):
        res.append([])
        for j in range(i+1):
            res[-1].append((res[-2][j-1] if j-1 >= 0 else 0)+(res[-2][j] if j < len(res[-2]) else 0))
    return res

def is_harshad(n):
    return n % sum([int(i) for i in str(n)]) == 0
# num_vector, res_vector = [
#   [75, 171, 481, 89, 516, 200, 209, 12345, 53, 27],
#   [False, True, True, False, True, True, True, True, False, True]
# ]
# for i, n in enumerate(num_vector): Test.assert_equals(is_harshad(n), res_vector[i])

def binary_to_text(b):
    return ''.join(chr(int(b[i:i+8], 2)) for i in range(0, len(b), 8))


# Test.assert_equals(binary_to_text("01110100011110010111000001100101011100110110001101110010011010010111000001110100"), "typescript")
# Test.assert_equals(binary_to_text("01101110011011110110010001100101"), "node")
# Test.assert_equals(binary_to_text("0111001001100101011000010110001101110100"), "react")
# Test.assert_equals(binary_to_text("01101010011000010111011001100001"), "java")
# Test.assert_equals(binary_to_text("011010110110111101110100011011000110100101101110"), "kotlin")
# Test.assert_equals(binary_to_text("011100000111100101110100011010000110111101101110"), "python")
# Test.assert_equals(binary_to_text("01101000011000010111001101101011011001010110110001101100"), "haskell")

from collections import Counter

def odd_one_out(lst):
    lol = (Counter([len(i) for i in lst]))
    if len(lol) == 2:
        if 1 in {v:i for i,v in lol.items()}:
            return True
    return False

# Test.assert_equals(odd_one_out(["silly", "mom", "let", "the"]), True)
# Test.assert_equals(odd_one_out(["swanky", "rhino", "moment"]), True)
# Test.assert_equals(odd_one_out(["the", "them", "theme"]), False)
# Test.assert_equals(odd_one_out(["very", "to", "an", "some"]), False)
# Test.assert_equals(odd_one_out(["very", "to", "then", "some"]), True)
# Test.assert_equals(odd_one_out(["ab", "cd", "ef", "gh", "a"]), True)
# Test.assert_equals(odd_one_out(["abcd", "cdef", "a", "efgh", "ghij"]), True)
# Test.assert_equals(odd_one_out(["abcd", "cdef", "abc", "def", "efgh", "ghij"]), False)
# Test.assert_equals(odd_one_out(["def", "abcd", "cdef", "abc", "efgh", "ghij"]), False)
# Test.assert_equals(odd_one_out(["def", "abcd", "cdef", "efgh", "ghij", "abc"]), False)
# Test.assert_equals(odd_one_out(["a", "b", "cf", "efg"]), False)

def hex_color_mixer(lst):
    lst = ([i[1:] for i in lst])
    oof = [[i[j:j+2] for j in range(0, len(i), 2)] for i in lst]
    lol = [[int((str(j)), 16) for j in i] for i in oof]
    return '#' + ''.join([hex(sum(i) // len(lst) + ((sum(i) / len(lst)) - (sum(i) // len(lst)) >= 0.5))[2:].zfill(2) for i in zip(*lol)]).upper()
    
Test.assert_equals(hex_color_mixer(["#FFFF00", "#FF0000"]), "#FF8000", "Example #1")
Test.assert_equals(hex_color_mixer(["#FFFF00", "#0000FF"]), "#808080", "Example #2")
Test.assert_equals(hex_color_mixer(["#B60E73", "#0EAEB6"]), "#625E95", "Example #3")
Test.assert_equals(hex_color_mixer(["#FF0000", "#00FF00", "#0000FF"]), "#555555")
Test.assert_equals(hex_color_mixer(["#99CC00", "#663399", "#1A8191"]), "#5E8063")
Test.assert_equals(hex_color_mixer(["#918381", "#D53B21", "#A54C83", "#DEFACF"]), "#BA817D")
Test.assert_equals(hex_color_mixer(["#140A23", "#46B31E", "#CFDF08", "#263534", "#EAD1FB", "#235E02"]), "#65803F")
Test.assert_equals(hex_color_mixer(["#FFFFFF", "#000000", "#000000", "#FFFFFF"]), "#808080")
Test.assert_equals(hex_color_mixer(["#CCCCCC"]), "#CCCCCC")