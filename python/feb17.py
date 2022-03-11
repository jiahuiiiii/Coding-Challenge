'''Given a positive integer n, compute the nth term in the Fibonacci sequence. For those of you that have been living under a rock in the mathematical world, here's the definition:

    The first and second terms are 1.
    nth term is the (n-1)th term + the (n-2)th term. So the 3rd term is the 1st term + the 2nd term, the 4th term is the 3rd term + the 2nd term, etc.

Thus the sequence looks like this: 1, 1, 2, 3, 5, 8, 13, 21, ...'''

from attr import has


def fibo(n):
    if n == 0 or n == 1:
        return n
    return fibo(n-1) + fibo(n-2)
# Test.assert_equals(fibo(1), 1)
# Test.assert_equals(fibo(2), 1)
# Test.assert_equals(fibo(3), 2)
# Test.assert_equals(fibo(4), 3)
# Test.assert_equals(fibo(5), 5)
# Test.assert_equals(fibo(6), 8)
# Test.assert_equals(fibo(30), 832040)
# Test.assert_equals(fibo(420), 2662710205480735617346452022100755074809023407208374441801919604845563638678145849451440)

def factorial_stupid_for_loop(num):
    res = 1
    for i in range(1, num + 1):
        res *= i 
    return res

def factorial(num):
    if num == 1:
        return 1
    return factorial(num-1) * num

# Test.assert_equals(factorial(2), 2)
# Test.assert_equals(factorial(6), 720)
# Test.assert_equals(factorial(3), 6)
# Test.assert_equals(factorial(12), 479001600)
# Test.assert_equals(factorial(5), 120)

def reverse(s, res = ''):
    if s == '':
        return res
    res += s[-1]
    return res + reverse(s[:-1])


# Test.assert_equals(reverse("hello"), "olleh")
# Test.assert_equals(reverse("world"), "dlrow")
# Test.assert_equals(reverse("a"), "a")
# Test.assert_equals(reverse(""), "", "An empty string should return an empty string.")

def has_identical(lst):
    return bool([i for i in lst if i in [list(j) for j in list(zip(*lst))]])

    # modified = [list(j) for j in list(zip(*lst))]
    # return bool([i for i in lst if i in modified])

    # for i in lst:
    #     if i in modified:
    #         return True
    # return False

# Test.assert_equals(has_identical([
#     [4, 4, 4, 4], 
#     [2, 4, 9, 8], 
#     [5, 4, 7, 7], 
#     [6, 4, 1, 0]
# ]), True)

# Test.assert_equals(has_identical([
#     [4, 2, 4, 6, 1], 
#     [2, 4, 9, 4, 5], 
#     [5, 1, 7, 1, 9], 
#     [6, 4, 1, 0, 33], 
#     [5, 5, 5, 33, 5]
# ]), True)

# Test.assert_equals(has_identical([
#     [4, 2],
#     [2, 1]
# ]), True)

# Test.assert_equals(has_identical([
#     [4, 4, 9, 4], 
#     [2, 1, 9, 8], 
#     [5, 4, 7, 7], 
#     [6, 4, 1, 0]
# ]), False)

# Test.assert_equals(has_identical([
#     [4, 4],
#     [2, 1]
# ]), False)

# Test.assert_equals(has_identical([
#     [4, 4, 3],
#     [2, 1, 9], 
#     [3, 8, 1]
# ]), False)

# Test.assert_equals(has_identical([
#     [4, 4, 4],
#     [2, 1, 4]
# ]), False)

# Test.assert_equals(has_identical([
#     [4, 4, 4]
# ]), False)

# def gpa_calculator(dic):
    # return '{} GPA for {} is {}'.format(dic['name'], dic['semester'], '{:.2f}'.format(sum([i['credit_hours'] * 'FDCBA'.index(i['grade']) for i in dic['courses']]) / sum(i['credit_hours'] for i in dic['courses'])))
def gpa_calculator(dic):
    gpa_ = 0
    quality_points = 'FDCBA'
    for i in dic['courses']:
        gpa_ += (quality_points.index(i['grade']) * i['credit_hours'] / i['credit_hours'])
    return '{} GPA for {} is {}'.format(dic['name'], dic['semester'], '{:.2f}'.format(gpa_))

first = {"name": "Utsab Karkee", "courses": [{"name": "cal1", "credit_hours": 5, "grade": "A"}, {"name": "phy1", "credit_hours": 3, "grade": "A"}, {"name": "eng1", "credit_hours": 3, "grade": "B"}, {
    "name": "pysch1", "credit_hours": 3, "grade": "A"}, {"name": "music1", "credit_hours": 3, "grade": "A"}, {"name": "chem1", "credit_hours": 3, "grade": "A"}], "semester": "Fall 2013"}
second = {"name": "Ansha Mandal", "courses": [{"name": "cal1", "credit_hours": 5, "grade": "A"}, {
    "name": "kin1", "credit_hours": 3, "grade": "A"}], "semester": "Spring 2018"}
third = {"name": "Lila Jha", "courses": [{"name": "cal1", "credit_hours": 5, "grade": "B"}, {"name": "phy1", "credit_hours": 3, "grade": "B"}, {"name": "eng1", "credit_hours": 3, "grade": "B"}, {
    "name": "pysch1", "credit_hours": 3, "grade": "B"}, {"name": "music1", "credit_hours": 3, "grade": "C"}, {"name": "chem1", "credit_hours": 3, "grade": "A"}], "semester": "Summer 2018"}
fourth = {"name": "Rama Basnet", "courses": [{"name": "cal3", "credit_hours": 3, "grade": "B"}, {"name": "dan1", "credit_hours": 3, "grade": "C"}, {"name": "eng3", "credit_hours": 3, "grade": "A"}, {
    "name": "pysch1", "credit_hours": 3, "grade": "A"}, {"name": "music1", "credit_hours": 3, "grade": "A"}], "semester": "Spring 2017"}
fifth = {"name": "Rima Rawal", "courses": [{"name": "cal1", "credit_hours": 5, "grade": "A"}, {
    "name": "kin1", "credit_hours": 3, "grade": "F"}], "semester": "Spring 2018"}
class Test:
    @classmethod
    def assert_equals(self, v1, v2, message=""):
        print(v1, '<>', v2)
        assert v1 == v2, message or 'two val not equal lol'

    @classmethod
    def assert_not_equals(self, v1, v2, message=""):
        print(v1, '<!>', v2)
        assert v1 != v2, message or 'two val not equal lol'
Test.assert_equals(gpa_calculator(first),"Utsab Karkee GPA for Fall 2013 is 3.85")
Test.assert_equals(gpa_calculator(second),"Ansha Mandal GPA for Spring 2018 is 4.00")
Test.assert_equals(gpa_calculator(third),"Lila Jha GPA for Summer 2018 is 3.00")
Test.assert_equals(gpa_calculator(fourth),"Rama Basnet GPA for Spring 2017 is 3.40")
Test.assert_equals(gpa_calculator(fifth),"Rima Rawal GPA for Spring 2018 is 2.50")
def maximum_items(lst, max_):
    could_buy = 0
    lst = sorted([int(j[1:]) for j in lst])
    max__ = int(max_[1:])
    for i in lst:
        if i <= (max__):
            could_buy += 1
            max__-= i
    return could_buy if could_buy else 'Not enough funds!'
    

# Test.assert_equals(maximum_items(["$1", "$1", "$2"], "$3"), 2)
# Test.assert_equals(maximum_items(["$10", "$7", "$2", "$60"], "$20"), 3)
# Test.assert_equals(maximum_items(["$15", "$5", "$30", "$30", "$10"], "$2"), "Not enough funds!")
# Test.assert_equals(maximum_items(["$99", "$8"], "$9"), 1)
# Test.assert_equals(maximum_items(["$85", "$88", "$72", "$77", "$53"], "$56"), 1)
# Test.assert_equals(maximum_items(["$12", "$2", "$49", "$21", "$76", "$64"], "$37"), 3)
# Test.assert_equals(maximum_items(["$3", "$17", "$12", "$98", "$12", "$91", "$41", "$73"], "$116"), 5)
# Test.assert_equals(maximum_items(["$18", "$16", "$32", "$30", "$43", "$80", "$13"], "$86"), 4)
# Test.assert_equals(maximum_items(["$20", "$11", "$8", "$59", "$64", "$36", "$41", "$99", "$98"], "$357"), 8)
# Test.assert_equals(maximum_items(["$12", "$98", "$56", "$88"], "$489"), 4)
# Test.assert_equals(maximum_items(["$12"], "$26"), 1)
# Test.assert_equals(maximum_items(["$65", "$78", "$78", "$61", "$51", "$91", "$76", "$27", "$85", "$70"], "$64"), 1)
# Test.assert_equals(maximum_items(["$28", "$64"], "$404"), 2)
# Test.assert_equals(maximum_items(["$69"], "$188"), 1)
# Test.assert_equals(maximum_items(["$59", "$99", "$59", "$90", "$75", "$19", "$36", "$56", "$79", "$5"], "$74"), 3)
# Test.assert_equals(maximum_items(["$73", "$7", "$75", "$33", "$7", "$95", "$11"], "$463"), 7)
# Test.assert_equals(maximum_items(["$58", "$64", "$85", "$21", "$91", "$1"], "$333"), 6)
# Test.assert_equals(maximum_items(["$89", "$7", "$27"], "$451"), 3)
# Test.assert_equals(maximum_items(["$10", "$63", "$25", "$2", "$10", "$59", "$71", "$60", "$88"], "$129"), 5)
# Test.assert_equals(maximum_items(["$23", "$82", "$75", "$17", "$67", "$67", "$95", "$48", "$15"], "$185"), 5)
# Test.assert_equals(maximum_items(["$86", "$22", "$92", "$8", "$44", "$97"], "$102"), 3)
# Test.assert_equals(maximum_items(["$16"], "$136"), 1)
# Test.assert_equals(maximum_items(["$37", "$46", "$68", "$7", "$75", "$53", "$79"], "$20"), 1)
# Test.assert_equals(maximum_items(["$71", "$36", "$5", "$56", "$33", "$66", "$91", "$49"], "$120"), 3)
# Test.assert_equals(maximum_items(["$43", "$70", "$25", "$100", "$47", "$95", "$8"], "$66"), 2)
# Test.assert_equals(maximum_items(["$70", "$11", "$87", "$65", "$6", "$9", "$63", "$55", "$90", "$95"], "$177"), 5)
# Test.assert_equals(maximum_items(["$24", "$90", "$100", "$31", "$99"], "$287"), 4)
# Test.assert_equals(maximum_items(["$34", "$62", "$62", "$98", "$100"], "$101"), 2)
# Test.assert_equals(maximum_items(["$59", "$90", "$97", "$34", "$31", "$37", "$31", "$97", "$52", "$70"], "$224"), 5)
# Test.assert_equals(maximum_items(["$29", "$71", "$23", "$27", "$46", "$33"], "$100"), 3)
# Test.assert_equals(maximum_items(["$34", "$6"], "$263"), 2)
# Test.assert_equals(maximum_items(["$36", "$34", "$74", "$90", "$14", "$21", "$96", "$24", "$67"], "$306"), 7)
# Test.assert_equals(maximum_items(["$78", "$83"], "$239"), 2)
# Test.assert_equals(maximum_items(["$6", "$8", "$67", "$64"], "$349"), 4)
# Test.assert_equals(maximum_items(["$95", "$59", "$58", "$28", "$82", "$38", "$65", "$33", "$29"], "$247"), 6)
# Test.assert_equals(maximum_items(["$57", "$97", "$47", "$91", "$70", "$78"], "$440"), 6)
# Test.assert_equals(maximum_items(["$45"], "$319"), 1)
# Test.assert_equals(maximum_items(["$5", "$89", "$78", "$73", "$44", "$93", "$57", "$80"], "$402"), 6)
# Test.assert_equals(maximum_items(["$1", "$26", "$54", "$12", "$5", "$61"], "$47"), 4)
# Test.assert_equals(maximum_items(["$16", "$50"], "$331"), 2)
# Test.assert_equals(maximum_items(["$6", "$51"], "$88"), 2)
# Test.assert_equals(maximum_items(["$74", "$91"], "$493"), 2)
# Test.assert_equals(maximum_items(["$51", "$81", "$64", "$51"], "$47"), "Not enough funds!")
# Test.assert_equals(maximum_items(["$32", "$60", "$12", "$93", "$82"], "$242"), 4)
# Test.assert_equals(maximum_items(["$92", "$55", "$35", "$78", "$1"], "$421"), 5)
# Test.assert_equals(maximum_items(["$46", "$41", "$47", "$52", "$99", "$62", "$50", "$62", "$65", "$38"], "$5"), "Not enough funds!")
# Test.assert_equals(maximum_items(["$33", "$4", "$4"], "$475"), 3)
# Test.assert_equals(maximum_items(["$78", "$11", "$37", "$95", "$60", "$11", "$53", "$58", "$97"], "$231"), 6)
# Test.assert_equals(maximum_items(["$20", "$69", "$46", "$91", "$42", "$49", "$54", "$44", "$96"], "$476"), 8)
# Test.assert_equals(maximum_items(["$60", "$42", "$93", "$47", "$67"], "$478"), 5)
# Test.assert_equals(maximum_items(["$81", "$14", "$12", "$89", "$69"], "$377"), 5)
# Test.assert_equals(maximum_items(["$16", "$67", "$76", "$78", "$72", "$19"], "$288"), 5)
# Test.assert_equals(maximum_items(["$47", "$55", "$27", "$73", "$72"], "$461"), 5)
