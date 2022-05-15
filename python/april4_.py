class Test:
    @classmethod
    def assert_equals(self, v1, v2, message=""):
        print(v1, '<>', v2)
        assert v1 == v2, message or 'two val not equal lol'

    @classmethod
    def assert_not_equals(self, v1, v2, message=""):
        print(v1, '<!>', v2)
        assert v1 != v2, message or 'two val not equal lol'


topsy_turvy_ = lambda lo, hi: [i for i in range(lo, hi+1) if all(int(p) in [1,6,8,9,0] for p in str(i)) and list({"6":"9", "9":"6"}[d] if d in "69" else d for d in str(i))[::-1] == list(str(i))]

def topsy_turvy(l, r):
    res = []
    for i in range(l, r+1):
        res_ = []
        for p in str(i):
            if int(p) in [1, 6, 8, 9, 0]:
                for d in str(i):
                    if d in '69':
                        res.append(list({"6":"9", "9":"6"}[d]))
        if res_[::-1] == list(str(i)):
            res.append(i)
    return
                    

Test.assert_equals(topsy_turvy(0, 10), [0, 1, 8])
Test.assert_equals(topsy_turvy(11, 100), [11, 69, 88, 96])
Test.assert_equals(topsy_turvy(2000, 6000), [])
Test.assert_equals(topsy_turvy(1000, 2000), [1001, 1111, 1691, 1881, 1961])
Test.assert_equals(topsy_turvy(10000, 15000), [10001, 10101, 10801, 11011, 11111, 11811])

print(topsy_turvy(0, 10))
print(topsy_turvy(11, 100))
print(topsy_turvy(2000, 6000))
print(topsy_turvy(1000, 2000))
print(topsy_turvy(10000, 15000))