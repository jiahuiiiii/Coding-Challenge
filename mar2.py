def can_give_blood(f, u):
    if f == u or f == 'O-':
        return True
    elif f == 'O+':
        if u[-1] == '+':
            return True
    elif f[0] == u[0] and f[1] == '-':
        return True
    return False


class Test:
    @classmethod
    def assert_equals(self, v1, v2, message=""):
        print(v1, '<>', v2)
        assert v1 == v2, message or 'two val not equal lol'

    @classmethod
    def assert_not_equals(self, v1, v2, message=""):
        print(v1, '<!>', v2)
        assert v1 != v2, message or 'two val not equal lol'

tests = [
	(("O+", "A+"), True),
	(("A-", "B-"), False),
	(("A-", "AB+"), True),
	(("AB-", "B-"), False),
	(("AB+", "A+"), False),
	(("O-", "A-"), True),
	(("A-", "O-"), False),
	(("O+", "AB-"), False),
	(("O-", "AB+"), True),
	(("AB+", "AB+"), True),
	(("O+", "O-"), False),
]
	
for test in tests:
	print("Input: " + str(test[0]))
	Test.assert_equals(can_give_blood(*test[0]), test[1])