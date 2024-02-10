fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Print the third, fourth, and fifth items (indexes 2, 3, and 4)
print(fruits[2:5])

###########################################

nums = [100, 200, 300, 400, 500]
reversed_nums = list(reversed(nums))
print(reversed_nums)

###############################
nums = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# Find the sublist [5000, 6000] and add 7000 after 6000
for i, item in enumerate(nums):
    if isinstance(item, list) and 6000 in item:
        item_index = item.index(6000)
        item.insert(item_index + 1, 7000)

print(nums)

###############################

nums = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "I"], "m", "n"]
sublist_to_add = ["h", "i", "门"]

# Extend the nested list with the provided sublist
nested_list = nums[2][1][2]
nested_list.extend(sublist_to_add)

print(nums)
####################################

age = '33'
print(type(age))

name = 'Ahmed'
print(type(name))

####################################
# 1. Length of the first string
string1 = "Hello World"
length_of_string1 = len(string1)
print("1. Length of the first string:", length_of_string1)

# 2. Get the first character of the first string
first_character = string1[0]
print("2. First character of the first string:", first_character)

# 3. Return the first string without any whitespace at the beginning or the end
trimmed_string1 = string1.strip()
print("3. First string without leading or trailing whitespace:", trimmed_string1)

# 4. Convert the first string to upper case
uppercased_string1 = string1.upper()
print("4. First string in upper case:", uppercased_string1)

# 5. Replace the last letter of the first string (Method 1)
replaced_string1_method1 = string1[:-1] + 'X'
print("5.1 First string with the last letter replaced (Method 1):", replaced_string1_method1)

# 5. Replace the last letter of the first string (Method 2)
replaced_string1_method2 = string1[:len(string1)-1] + 'Y'
print("5.2 First string with the last letter replaced (Method 2):", replaced_string1_method2)

#################################################
# Given list
fruits = ["apple", "banana", "cherry"]

# 1. Print the second item in the fruits list.
second_item = fruits[1]
print("1. Second item in the fruits list:", second_item)

# 2. Change the value from "apple" to "kiwi", in the fruits list.
fruits[0] = "kiwi"
print("2. Updated fruits list:", fruits)

# 3. Use the insert method to add "lemon" as the second item in the fruits list.
fruits.insert(1, "lemon")
print("3. Updated fruits list after inserting 'lemon':", fruits)

# 4. Use negative indexing to print the last item in the list.
last_item = fruits[-1]
print("4. Last item in the fruits list using negative indexing:", last_item)

##############################
# Given list
list1 = [5, 10, 15, 20, 25, 50, 20]

# Find value 20 in the list and replace it with 200 (only the first occurrence)
if 20 in list1:
    index_of_20 = list1.index(20)
    list1[index_of_20] = 200

print("Updated list1:", list1)


