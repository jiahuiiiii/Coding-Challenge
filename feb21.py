from itertools import zip_longest
# def post_fix(text):
#     res = []
#     for i, v in enumerate(reversed(sorted(text.split()))):
#         if v.isdigit():
#             res.append(v)
#         elif v in '+-*/':
#             res.insert("".join(res).rindex(res[i-1]), v)
#             print(res)
#     return eval("".join(res))

def post_fix(s):
    l1 = []
    l2 = []
    for i in s.split():
        if i.isdigit():
            l1.append(i)
        elif i in '+-*/':
            l2.append(i)
    l3 = zip_longest(l1, l2, fillvalue='')
    return eval("".join("".join(i) for i in l3))

def post_fix_one_line(s): return eval("".join("".join(i) for i in zip_longest([i for i in s.split() if i.isdigit()], [i for i in s.split() if not i.isdigit()], fillvalue="")))

def happiness_number(s): 
    lol = 0
    for i in range(len(s)-1):
        if (s[i] + s[i+1]) in [':)','(:']:
            lol += 1
        elif (s[i] + s[i+1]) in [':(','):']:
            lol -= 1

    return lol

def happiness_number_one_line(s): return sum([[-1, 1][s[i]+s[i+1] in ":)(:"] for i in range(len(s)-1) if (s[i]+s[i+1]) in ":),(:):,:("])

class Test:
    @classmethod
    def assert_equals(self, v1, v2, message=""):
        print(v1, '<>', v2)
        assert v1 == v2, message or 'two val not equal lol'

    @classmethod
    def assert_not_equals(self, v1, v2, message=""):
        print(v1, '<!>', v2)
        assert v1 != v2, message or 'two val not equal lol'
# Test.assert_equals(post_fix("2 2 +"), 4)
# Test.assert_equals(post_fix("2 2 /"), 1)
# Test.assert_equals(post_fix("8 4 / 9 * 3 1 * /"), 54)
# Test.assert_equals(post_fix("5 6 * 2 1 + /"), 32)
# Test.assert_equals(post_fix("10 10 * 10 /"), 10)
# Test.assert_equals(post_fix("1 1 + 2 2 + -"), 2)

Test.assert_equals(happiness_number(':):('), -1)
Test.assert_equals(happiness_number('(:)'), 2)
Test.assert_equals(happiness_number('::::'), 0)
Test.assert_equals(happiness_number(':)::(()::'), -2)
Test.assert_equals(happiness_number('))):'), -1)
Test.assert_equals(happiness_number(':):)('), 1)
Test.assert_equals(happiness_number(':(:(:()):'), -2)
Test.assert_equals(happiness_number('()((:())):'), -1)
Test.assert_equals(happiness_number(':(:)'), 1)
Test.assert_equals(happiness_number('(:):(:)(('), 2)
Test.assert_equals(happiness_number(':(:(:'), 0)
Test.assert_equals(happiness_number(')())(()'), 0)
Test.assert_equals(happiness_number(':()):'), -2)
Test.assert_equals(happiness_number('():(('), -2)
Test.assert_equals(happiness_number('::::(():('), -3)
Test.assert_equals(happiness_number(')(():((::'), -1)
Test.assert_equals(happiness_number('(::):('), 0)
Test.assert_equals(happiness_number('):()::('), -4)
Test.assert_equals(happiness_number(':::(:('), -1)
Test.assert_equals(happiness_number(')((:'), 1)
Test.assert_equals(happiness_number('(:::(:('), 0)
Test.assert_equals(happiness_number('))(:(:'), 1)
Test.assert_equals(happiness_number('::))(:('), 1)
Test.assert_equals(happiness_number('(((())))'), 0)