# write a function that gets a number and
# returns half of it (as int)
def half_num(x: int):
    return x // 2

# write a function that gets 2 floats and returns the smaller one
def small_float(x: float, y: float):
    return min(x,y)

# write a function that gets 2 string and returns the longer string
def long_str(x: str, y: str):
    return x if len(x) > len(y) else y

# write a function that gets 2 bool and returns True if they are the same otherwise False
def equal_bool(x: bool, y: bool):
    return x == y

# write a function that gets 2 list and returns the longer list
def long_list(x: list, y: list):
    return x if len(x) > len(y) else y

# write a function that gets a string and returns the reversed string
def rev_str(x: str):
    return x[::-1]

# write a function that gets a word and a list[word] return true if the word appear in the
#  list otherwise returns false
def word_in_list(x: str, y: list[str]):
    return True if x in y else False

# *Bonus: write a function that gets a word and a list[word] return index of the word
# if it appears in the list otherwise returns None
def word_index(x: str, y: list[str]):
    return y.index(x) if x in y else None

# to check
print(int(half_num(8)))
print(small_float(1.2, 3.3))
print(long_str("ido", "hamrani"))
print(equal_bool(False, False))
print(long_list([1, 3], [1, 1, 1]))
print(rev_str("ido"))
print(word_in_list("hello", ["hello", "world"]))
print(word_index("there", ["hi", "there"]))
