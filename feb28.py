def not_nice_max_possible(num1, num2):
    one = [i for i in str(num1)]
    two = [int(i) for i in str(num2)]
    for i in one:
        if two != [] and int(i) < (max(two)):
            one[one.index(i)] = str(max(two))
            two.pop(two.index(max(two)))

    return int(''.join(one))

def max_possible(num1, num2):
    one = [i for i in str(num1)]
    two = sorted([int(i) for i in str(num2)])
    for i in one:
        if two != [] and int(i) < two[-1]:
            one[one.index(i)] = str(two[-1])
            two.pop(-1)

    return int(''.join(one))

# Test.assert_equals(max_possible(9328, 456), 9658)
# Test.assert_equals(max_possible(523, 76), 763)
# Test.assert_equals(max_possible(9132, 5564), 9655)
# Test.assert_equals(max_possible(8732, 91255), 9755)
# Test.assert_equals(max_possible(589, 777), 789)
# Test.assert_equals(max_possible(1, 0), 1)
# Test.assert_equals(max_possible(8, 9), 9)
# Test.assert_equals(max_possible(28, 19), 98)
# Test.assert_equals(max_possible(12345, 4), 42345)

# std::vector<std::vector<int>> allPairs(std::vector<int> arr, int target) {
#     std::vector<std::vector<int>> ans;
#     std::map<int, int> m;

#     for (int i = 0; i < arr.size(); i++) {
#         if (m.find(target-arr[i]) != m.end()) {
#             std::vector<int> a = {target-arr[i], arr[i]};
#             std::sort(a.begin(), a.end());
#             ans.push_back(a);
#         } else {
#             m[arr[i]] = target-arr[i];
#         }
#     }

#     std::sort(ans.begin(), ans.end());
#     return ans;
# }
def all_pairs(lst, target):
    ans = []
    map_ = {}
    for i, v in enumerate(lst):
        complement = target - v
        if complement in map_:
            ans.append(sorted([v, map_[complement]]))
            del map_[complement]
        else:
            map_[v] = v
    return sorted(ans)

# Test.assert_equals(all_pairs([2, 4, 5, 3], 7), [[2, 5], [3, 4]])
# Test.assert_equals(all_pairs([5, 3, 9, 2, 1], 3), [[1, 2]])
# Test.assert_equals(all_pairs([4, 5, 1, 3, 6, 8], 9), [[1, 8], [3, 6], [4, 5]])
# Test.assert_equals(all_pairs([5, 2], 14), [])
# Test.assert_equals(all_pairs([5, 5, 2], 14), [])
# Test.assert_equals(all_pairs([8, 7, 7, 2, 4, 6], 14), [[6, 8], [7, 7]])
# Test.assert_equals(all_pairs([8, 7, 2, 4, 6], 14), [[6, 8]])
# Test.assert_equals(all_pairs([1, 3, 5, 4, 0], 4), [[0, 4], [1, 3]])
# Test.assert_equals(all_pairs([1, 3, 5, 4, 0, 2], 4), [[0, 4], [1, 3]])
# Test.assert_equals(all_pairs([1, 3, 5, 4, 0, 2, 2], 4), [[0, 4], [1, 3], [2, 2]])

def cars(wheels, body, figures):
    return min(wheels // 4, body, figures // 2)

# Test.assert_equals(cars(37, 15, 20), 9)
# Test.assert_equals(cars(72, 7, 21), 7)
# Test.assert_equals(cars(9, 44, 34), 2)
# Test.assert_equals(cars(50, 38, 7), 3)
# Test.assert_equals(cars(68, 9, 44), 9)
# Test.assert_equals(cars(3, 29, 54), 0)
# Test.assert_equals(cars(28, 34, 80), 7)
# Test.assert_equals(cars(88, 50, 83), 22)
# Test.assert_equals(cars(66, 18, 21), 10)
# Test.assert_equals(cars(97, 6, 10), 5)
# Test.assert_equals(cars(921, 310, 350), 175)
# Test.assert_equals(cars(736, 430, 851), 184)
# Test.assert_equals(cars(405, 379, 740), 101)
# Test.assert_equals(cars(593, 78, 389), 78)
# Test.assert_equals(cars(875, 370, 675), 218)
# Test.assert_equals(cars(863, 274, 203), 101)
# Test.assert_equals(cars(959, 331, 537), 239)
# Test.assert_equals(cars(416, 340, 551), 104)
# Test.assert_equals(cars(692, 348, 543), 173)
# Test.assert_equals(cars(527, 412, 951), 131)

def minesweeper_numbers(lst):
    coors = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1],
    ]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == 1:
                lst[i][j] = 9
    for i, v in enumerate(lst):
        for j, w in enumerate(v):
            if w == 0:
                minecount = 0
                for n in range(len(coors)):
                    if (i + coors[n][0] >= 0) and (i + coors[n][0] < len(lst)):
                        if (j + coors[n][1] >= 0) and (j + coors[n][1] < len(v)):
                            if lst[i + coors[n][0]][j + coors[n][1]] == 9:
                                minecount += 1
                lst[i][j] = minecount

    return lst
                


class Test:
    @classmethod
    def assert_equals(self, v1, v2, message=""):
        print(v1, '<>', v2)
        assert v1 == v2, message or 'two val not equal lol'

    @classmethod
    def assert_not_equals(self, v1, v2, message=""):
        print(v1, '<!>', v2)
        assert v1 != v2, message or 'two val not equal lol'

Test.assert_equals(minesweeper_numbers([]), [])

Test.assert_equals(minesweeper_numbers([
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]), [
  [9, 9, 9],
  [9, 8, 9],
  [9, 9, 9]
])

Test.assert_equals(minesweeper_numbers([
  [0, 0, 0, 1],
  [0, 1, 0, 0],
  [1, 0, 0, 0],
  [0, 0, 1, 0]
]), [
  [1, 1, 2, 9],
  [2, 9, 2, 1],
  [9, 3, 2, 1],
  [1, 2, 9, 1]
])

Test.assert_equals(minesweeper_numbers([
    [0, 1, 0, 0],
  [0, 0, 1, 0],
  [0, 1, 0, 1],
  [1, 1, 0, 0],
]), [
  [1, 9, 2, 1],
  [2, 3, 9, 2],
  [3, 9, 4, 9],
  [9, 9, 3, 1],
])

Test.assert_equals(minesweeper_numbers([
    [1, 0, 0, 0, 0, 0, 1, 0],
  [1, 0, 1, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 0],
  [0, 1, 0, 1, 0, 0, 0, 1],
  [0, 0, 0, 1, 0, 1, 1, 0],
  [0, 1, 1, 0, 0, 0, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 1, 0, 1],
]), [
  [9, 3, 1, 2, 1, 2, 9, 1],
  [9, 3, 9, 2, 9, 3, 2, 2],
  [2, 3, 3, 3, 2, 2, 9, 2],
  [1, 9, 3, 9, 3, 3, 4, 9],
  [2, 3, 5, 9, 3, 9, 9, 4],
  [2, 9, 9, 2, 2, 3, 9, 9],
  [9, 4, 3, 2, 1, 2, 4, 3],
  [1, 2, 9, 1, 1, 9, 2, 9],
])

Test.assert_equals(minesweeper_numbers([
  [1, 1, 0, 0, 0, 0, 0, 0],
  [1, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 1, 1, 0],
  [0, 1, 0, 0, 0, 0, 1, 1],
  [1, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 0, 1, 0, 1, 1],
]), [
  [9, 9, 2, 0, 0, 0, 0, 0],
  [9, 9, 2, 0, 0, 1, 1, 1],
  [4, 4, 2, 0, 0, 1, 9, 1],
  [9, 9, 2, 2, 3, 4, 3, 2],
  [3, 3, 3, 9, 9, 9, 9, 3],
  [2, 9, 2, 3, 4, 5, 9, 9],
  [9, 3, 2, 3, 9, 4, 4, 4],
  [1, 2, 9, 3, 9, 3, 9, 9],
])