def combinations(array, tuple_length, prev_array=[]):
    if len(prev_array) == tuple_length:
        return [prev_array]
    combs = []
    for i, val in enumerate(array):
        prev_array_extended = prev_array.copy()
        prev_array_extended.append(val)
        combs += combinations(array[i+1:], tuple_length, prev_array_extended)
    return combs


# print(combinations([1, 2, 3, 4], 2))

def combo(lst, n, prev=[]):
    if len(prev) == n:
        return [prev]
    res = []
    for i, v in enumerate(lst):
        prev_extended = prev.copy()
        prev_extended.append(v)
        res += combo(lst[i+1:], n, prev_extended)
    return res

class Test:
    @classmethod
    def assert_equals(self, v1, v2, message=""):
        print(v1, '<>', v2)
        assert v1 == v2, message or 'two val not equal lol'

    @classmethod
    def assert_not_equals(self, v1, v2, message=""):
        print(v1, '<!>', v2)
        assert v1 != v2, message or 'two val not equal lol'

Test.assert_equals(combo([1, 2, 3, 4], 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
Test.assert_equals(combo([1, 2, 3, 4], 3), [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]])
Test.assert_equals(combo([1, 2, 3, 4], 1), [[1], [2], [3], [4]])
Test.assert_equals(combo([1, 2, 3, 4], 5), [])
Test.assert_equals(combo([1, 2, 3, 4], 0), [[]])
Test.assert_equals(combo(['a', 'b', 'c'], 0), [[]])
Test.assert_equals(combo(['a', 'b', 'c'], 4), [])
Test.assert_equals(combo(['a', 'b', 'c'], 1), [['a'], ['b'], ['c']])
Test.assert_equals(combo(['a', 'b', 'c'], 2), [['a', 'b'], ['a', 'c'], ['b', 'c']])
Test.assert_equals(combo(['a', 'b', 'c'], 3), [['a', 'b', 'c']])
