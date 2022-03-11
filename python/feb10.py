
def slutter(s):
    slice_ = s[:2]
    return f"{slice_}.. {slice_}.. {s}?"

def make_rug(height, width, material):
    return [[material for w in range(width)] for h in range(height)]

def construct_deconstruct(s):
    for i in range(1, len(s)+1):
        print(s[:i])

def square_patch(num):
    return [[num for i in range(num)] for i in range(num)]

def initialize(s):
    return [" ".join([f"{word[:1]}." for word in name.split()]) for name in s ]

def left_shift(arr, num):
    return arr[num:] + arr[:num]
