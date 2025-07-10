# At first, gets two strings as inputs.
str1 = input("Please enter the first string: ")
str2 = input("Please enter the second string: ")

# Use "if" & "else" & "sorted" to compare two variables "str1" and "str2"
if sorted (str1) == sorted(str2):
# Output the result in this condition.
    print("the strings are anagrams :) ")
else:
# Output the result in this condition.
     print("the strings are not anagrams :( ")