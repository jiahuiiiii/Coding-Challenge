
def perrin_while(n):
    uwu = [3, 0, 2]
    if n < len(uwu):
        return uwu[n]
    while n >= len(uwu):
        uwu.append(uwu[-2] + uwu[-3])

    return uwu[n]
def perrin(n):
    if n == 2: return 2
    if n == 1: return 0
    if n == 0: return 3
    return perrin(n-2) + perrin(n-3)

class Test:
    @classmethod
    def assert_equals(self, v1, v2, message=""):
        print(v1, '<>', v2)
        assert v1 == v2, message or 'two val not equal lol'

    @classmethod
    def assert_not_equals(self, v1, v2, message=""):
        print(v1, '<!>', v2)
        assert v1 != v2, message or 'two val not equal lol'
Test.assert_equals(perrin(0), 3)
Test.assert_equals(perrin(38), 43721)
Test.assert_equals(perrin(58), 12110402)
Test.assert_equals(perrin(52), 2240877)
Test.assert_equals(perrin(36), 24914)
Test.assert_equals(perrin(44), 236282)
Test.assert_equals(perrin(50), 1276942)
Test.assert_equals(perrin(42), 134643)
Test.assert_equals(perrin(27), 1983)
Test.assert_equals(perrin(17), 119)
Test.assert_equals(perrin(45), 313007)
Test.assert_equals(perrin(46), 414646)
Test.assert_equals(perrin(28), 2627)
Test.assert_equals(perrin(37), 33004)
Test.assert_equals(perrin(43), 178364)
Test.assert_equals(perrin(22), 486)
Test.assert_equals(perrin(25), 1130)
Test.assert_equals(perrin(51), 1691588)
Test.assert_equals(perrin(34), 14197)
Test.assert_equals(perrin(15), 68)
Test.assert_equals(perrin(41), 101639)