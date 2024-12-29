# region Pycharm Shortcuts
"""
Execute Selection in Console: Alt+Shift+E
Execute Script : Shift + Fn +F10
Collapse All : CTRL + Shift + "-Button"
Expand All: CTRL + Shift + "+Button"
Renam Variable : Shift + F6
"""
# endregion

# region Logic Order
result = not False or True and False
print(result)
result = (not False) or (True and False)
print(result)
# endregion

#region Shorthand Statement
x=29
x = x+1 if x%2 else x
print(x)
#endregion

#region Match Case
x=10
match x:
    case 0:
        print(0)
    case 1:
        print(1)
    case 2:
        print(2)
    case _:
        print("Everything else")
#endregion



# region List Reference Copy
lst1 = [1, [1, 1, 1], 1]
print(f"{lst1=}: Original")
lst2 = lst1
print(f"{lst2=}: Reference to Original")
print("lst1[0]=0,lst1[1][0]=0 : Modifications")
lst1[1][0] = 0 #Also changes in lst2 because only "shallow copy
lst1[0] = 0 #
print(f"{lst1=}: {id(lst1)=}")
print(f"{lst2=}: {id(lst2)=}")
# endregion
# region List Shallow Copy
import copy
lst1 = [1, [1, 1, 1], 1]
print(f"{lst1=}: Original")
lst2 = copy.copy(lst1)
print(f"{lst2=}: Shallow Copy")
print("lst1[0]=0,lst1[1][0]=0 : Modifications")
lst1[1][0] = 0 #Also changes in lst2 because only "shallow copy
lst1[0] = 0 #
print(f"{lst1=}")
print(f"{lst2=}: Side Effect!")
# endregion
# region List Deep Copy
import copy
lst1 = [1, [1, 1, 1], 1]
print(f"{lst1=}: Original")
lst2 = copy.deepcopy(lst1)
print(f"{lst2=}: Shallow Copy")
print("lst1[0]=0,lst1[1][0]=0 : Modifications")
lst1[1][0] = 0 #Also changes in lst2 because only "shallow copy
lst1[0] = 0 #
print(f"{lst1=}:")
print(f"{lst2=}: No Side Effect")
# endregion


# region String Immutable
str_a = "hello"
id1 = id(str_a)
str_a += "world"
id2 = id(str_a)
print(f"Strings are immutable: {id1 is not id2}")
# endregion
# region Integer Immutable
int_a = 1002
id1 = id(int_a)
int_a += 10004
id2 = id(int_a)
print(f"Integers are immutable: {id1 is not id2}")
# endregion
# region Fixed Reference Small Integers (-5 to 256)
nr_list = list(range(-10, 300))
references1 = [id(nr) for nr in nr_list]
nr_list2 = list(range(-10, 300))
references2 = [id(nr) for nr in nr_list2]

for idx in range(len(references1)):
    if references1[idx] == references2[idx]:
        print(f"Integer {nr_list[idx]=} and {nr_list[idx]=} have same reference")
# endregion

# region Check Type of an Object
if type(112) is type(int()):
    print("112 is an Integer")

if type(112) is int:
    print("112 is an Integer")

if isinstance(112, int):
    print("112 is an Integer")


# endregion

# region Lambda Functions
keys_list = ["a","b","c","d","e"]
values_list = [1,2,4,5,6]

a_dict = dict(map(lambda key,value: (key+"_", value+10), keys_list, values_list))
print(a_dict)
# endregion