import random
# print the diff of 2 numbers
# the numbers are argument. default value == 0
# call the function with (9999, 4444)
# call the function with no parameters

def num_dif(x: int = 0, y: int = 0):
    print(f"{x}-{y}={x - y}")
    print(f"{y}-{x}={y - x}")

print(num_dif(9999, 4444))


# print the biggest of 3 number
# the numbers are argument. default value == 0
# call the function with -10, -100, 1

def biggest_of_three(x: int = 0, y: int = 0, z: int = 0):
    print(max([x,y,z]))

print(biggest_of_three(-10,-100,1))

# function that gets a list[int] and print its length

def list_length (l1: list[int] = []):
    print(len(l1))

list_length([1,2,3,4,5])

# function that gets a list of int
# print the diff between the max and the min
# call the function with [900, 1010, -87, 0, 10_000]
# should print 10_000 - (-87) = 10_087

def edge_diff(l2: list[int] = None):
    print(max(l2)-min(l2))

edge_diff([900, 1010, -87, 0, 10_000])

# function that gets 1 string as parameter
# print tail equals head or not
# "radar" --> print: head equals tail
# "mango" --> print: head is not equals tail
# bonus: ignore case sensitive "Radar" --> equals
# try on word radar, apple, level, civic, noon, shalom

def head_2_tail (my_str: str):
    my_str = my_str.lower()
    print("head 2 tail" if my_str == my_str[::-1] else "not head 2 tail" )

head_2_tail("Radar")
head_2_tail("mango")

# function that gets 2 booleans as parameter
# print "the same" if they are the same
# print "different" if they are different
# default False
# True True --> the same
# False True --> different
# True False --> different
# False False --> the same

def same_odd(x: bool = False, y: bool = False):
    if x==y:
        print("the same")
    else:
        print ("different")

same_odd(True,True)
same_odd(False,True)
same_odd(True,False)
same_odd(False,False)

# function that gets 2 floats as parameter
# create a list from these 2 floats
# sort the list and print it

def sort_list (x: float = 1, y:float = 0):
    l3:list [float] = []
    l3.append(x)
    l3.append(y)
    l3.sort()
    print(l3)

sort_list()
