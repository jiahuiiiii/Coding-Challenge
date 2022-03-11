def is_parallelogram(lst):
    pass

# Test.assert_equals(is_parallelogram([(0, 0), (1, 0), (1, 1), (0, 1)]),  True)
# Test.assert_equals(is_parallelogram([(0, 0), (2, 0), (1, 1), (0, 1)]),  False)
# Test.assert_equals(is_parallelogram([(0, 0), (1, 1), (1, 4), (0, 3)]),  True)
# Test.assert_equals(is_parallelogram([(0, 0), (1, 2), (2, 1), (3, 3)]),  True)
# Test.assert_equals(is_parallelogram([(0, 0), (1, 0), (0, 1), (1, 1)]),  True)
# Test.assert_equals(is_parallelogram([(0, 0), (1, 1), (1, 4), (6, 3)]),  False)
# Test.assert_equals(is_parallelogram([(2, 0), (-2, 0), (0, 1), (0, -1)]),  True)
# Test.assert_equals(is_parallelogram([(2, 0), (-2, 0), (0, 2), (0, -1)]),  False)
# Test.assert_equals(is_parallelogram([(1, -1), (-1, 1), (2, 3), (-3, -2)]),  False)
# Test.assert_equals(is_parallelogram([(1, -1), (-1, 1), (2, 3), (-2, -3)]),  True)
# Test.assert_equals(is_parallelogram([(1, -1), (2, 3), (-1, 1), (-3, -2)]),  False)
# Test.assert_equals(is_parallelogram([(0, 0), (1, 1), (2, 0), (0, 1)]),  False)
# Test.assert_equals(is_parallelogram([(-1, -1), (3, 3), (1, 0), (1, 2)]),  True)
# Test.assert_equals(is_parallelogram([(-1, -1), (1, 0), (3, 4), (1, 2)]),  False)
# Test.assert_equals(is_parallelogram([(-1, -1), (1, 0), (3, 3), (1, 2)]),  True)
# Test.assert_equals(is_parallelogram([(-1, 0), (1, 0), (3, 3), (1, 2)]),  False)

def sums_of_powers_of_two(n):
    ans = []
    for i, v in enumerate(reversed(str(bin(n)[2:]))):
        if int(v) != 0:
            ans.append((int(v)*2)**i)
    return ans

# Test.assert_equals(sums_of_powers_of_two(1), [1])
# Test.assert_equals(sums_of_powers_of_two(5), [1, 4])
# Test.assert_equals(sums_of_powers_of_two(7), [1, 2, 4])
# Test.assert_equals(sums_of_powers_of_two(8), [8])
# Test.assert_equals(sums_of_powers_of_two(10), [2, 8])

# Test.assert_equals(sums_of_powers_of_two(21), [1, 4, 16])
# Test.assert_equals(sums_of_powers_of_two(53), [1, 4, 16, 32])
# Test.assert_equals(sums_of_powers_of_two(63), [1, 2, 4, 8, 16, 32])
# Test.assert_equals(sums_of_powers_of_two(99), [1, 2, 32, 64])
# Test.assert_equals(sums_of_powers_of_two(100), [4, 32, 64])

# Test.assert_equals(sums_of_powers_of_two(556846320), [16, 32, 64, 128, 1024, 2048, 16384, 32768, 1048576, 2097152, 16777216, 536870912])
# Test.assert_equals(sums_of_powers_of_two(509104470), [2, 4, 16, 64, 256, 4096, 16384, 524288, 1048576, 4194304, 33554432, 67108864, 134217728, 268435456])
# Test.assert_equals(sums_of_powers_of_two(929640411), [1, 2, 8, 16, 64, 128, 256, 512, 1024, 2048, 8192, 65536, 524288, 2097152, 4194304, 16777216, 33554432, 67108864, 268435456, 536870912])
# Test.assert_equals(sums_of_powers_of_two(341971175), [1, 2, 4, 32, 64, 128, 4096, 131072, 2097152, 4194304, 67108864, 268435456])
# Test.assert_equals(sums_of_powers_of_two(329418410), [2, 8, 32, 128, 512, 1024, 32768, 131072, 2097152, 8388608, 16777216, 33554432, 268435456])

def sum_missing_numbers(lst):
    lol = 0
    for i in range(min(lst), max(lst)+1):
        if i not in lst:
            lol += i
    return lol

# Test.assert_equals(sum_missing_numbers([1, 2, 3, 4, 5]), 0)
# Test.assert_equals(sum_missing_numbers([4, 3, 8, 1, 2]), 18)
# Test.assert_equals(sum_missing_numbers([17, 16, 15, 10, 11, 12]), 27)
# Test.assert_equals(sum_missing_numbers([-1, -4, -3, -2, -6, -8]), -12)

def isBalanced_(s):
    i = -1 
    if s == None:
        return None
    while len(s) != i:
        i = len(s)
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
        
    return len(s) == 0

def isBalanced(s):
    # first in last out
    pthMap = {"{": "}", "(": ")", "[": "]"}
    stack = []
    if s == None:
        return None
    for i in s:
        if i in "[]{}()":
            if i in pthMap.values():
                if not len(stack) or pthMap[stack.pop()] != i:
                    return False
            else: stack.append(i)
    return len(stack) == 0

class Test:
    @classmethod
    def assert_equals(self, v1, v2, message=""):
        print(v1, '<>', v2)
        assert v1 == v2, message or 'two val not equal lol'

    @classmethod
    def assert_not_equals(self, v1, v2, message=""):
        print(v1, '<!>', v2)
        assert v1 != v2, message or 'two val not equal lol'

Test.assert_equals(isBalanced('()'), True)
Test.assert_equals(isBalanced('{[()]}'), True)
Test.assert_equals(isBalanced('{{[[(())]]}}'), True)
Test.assert_equals(isBalanced('{{[[(())[]]]}}'), True)
Test.assert_equals(isBalanced('[()]{}{[()()]()}'), True)
Test.assert_equals(isBalanced('{[([)]]}'), False)
Test.assert_equals(isBalanced('{[('), False)
Test.assert_equals(isBalanced('])}'), False)
Test.assert_equals(isBalanced('[[]'), False)
Test.assert_equals(isBalanced('{)(}'), False)
Test.assert_equals(isBalanced('{{[[([())]]]}}'), False)
Test.assert_equals(isBalanced(None), None)