# region Pycharm Shortcuts
# Execute Selection in Console: Alt+Shift+E
# Execute Script : Shift + Fn +F10
# endregion

# region Shallow Copy
list_a = [1,2,3,4,5]
list_b = list_a
list_a.append(6)
print(f"{list_a=} and {list_b=}")
# endregion
# region Deep Copy
import copy
list_a = [1,2,3,4,5]
list_b = copy.deepcopy(list_a)
list_a.append(6)
print(f"{list_a=} and {list_b=}")
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
an_integer = 23
a_float = 2.3455
a_string = "sihfihfin"
a_tuple = (1,2,3)
a_dict = {"a": 1, "b":2, "c": 3}
a_list = [1,2,3,4,5,6]
list_with_different_values = [an_integer, a_float, a_string, a_tuple, a_dict, a_list]

def find_datatype(_list, datatype_class):
    for element in list_with_different_values:
        if isinstance(element,datatype_class):
            print(f"{element=} is of type {datatype_class}")

find_datatype(list_with_different_values, str)
# endregion

# region Lambda Functions
keys_list = ["a","b","c","d","e"]
values_list = [1,2,4,5,6]

a_dict = dict(map(lambda key,value: (key+"_", value+10), keys_list, values_list))
print(a_dict)
# endregion