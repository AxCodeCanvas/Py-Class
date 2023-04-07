"""
# Dictionary

- key : value  pairs
- Unordered
- {}

[0] : "Python"
[1] : "Python"

key1 : "Python"
key2 : "Python"
"""

# Empty Dictionary

my_dict = {}
print(type(my_dict))  # <class 'dict'>

my_dict2 = dict()
print(type(my_dict2))  # <class 'dict'>

# With value

my_dict = {
    "name": "Hasan Mahmud",
    "fav_language": "Python",
    "one": 1,
    "two": 2.5,
    "lst": [1, 2, 3, 4],
    1: "One"
}
print(my_dict)  # {'name': 'Hasan Mahmud', 'fav_language': 'Python'}

my_dict2 = dict(
    {
        "name": "Hasan Mahmud",
        "fav_language": "Python",
        "fav_language2": "Java",
        "fav_language3": "C++",
        "fav_language4": "C",
        "one": 1,
        "two": 2.5,
        "lst": [1, 2, 3, 4]
    }
)
print(my_dict2)  # {'name': 'Hasan Mahmud', 'fav_language': 'Python'}

# Access

print(my_dict["name"])  # Hasan Mahmud
print(my_dict.get("fav_language"))  # Python

print(my_dict["lst"])
print(my_dict[1])

my_dict3 = {
    1: 1,
    2: 5.5
}

print(my_dict3.get(2))

#  Update / add
print("-----------------")
print(my_dict3)
my_dict3[1] = "One"

print(my_dict3)

my_dict3[3] = "Three"
print(my_dict3)

# Remove
print(my_dict3.pop(1))
print(my_dict3)

my_dict3.clear()
print(my_dict3)
