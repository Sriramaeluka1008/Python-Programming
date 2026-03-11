#sentence = "Python is amazing"
# Output: "Pto saaig

sentence = "Python is amazing"
sentence1 = sentence[::2]
print(sentence1)


# Output: "Python_is_fun_and_powerful"
str  = "Python is fun and powerful"
replace_str = str.replace(" ","_")
print(replace_str)

# #Check if the string contains only digits
s = "12345"
s1 = s.isdigit()
print(s1)

#Print the string in reverse order
# Output: "gnizama si nohtyP
s = "Python is amazing"
s_rev = s[::-1]
print(s_rev)

'''Capitalize the first letter of each word in the string 
and print the modified string.'''
# Output: "Python Programming Is Fun"
s = "python programming is fun"
s1 = s.title()
print(s1)