line = "Python is great" 
line_with_quote = 'Python is "great"' # 1: if you want to use quote mark in string, you can use single quotation mark to replace the double quotation mark 
# The Capital of the name of variable matter. For example, letter and Letter are two different variables
Letter = """
Hello Guys, 
This is the how we make multiple lines string in python
Best,
"""
letter = "Zeyu Lu"
#         0123456
#              -2-1                       What about negative index? 
part_letter = letter[:3]

print(line_with_quote)
print(line)
print(Letter)
print(letter)
print(letter[0]) # if we want to get the first character of the variable by using square brackets
print(letter[-1])  # we can also use negative index, but this feature only for Python, -1 is the index of the last  character and so on
print(letter[0:3]) # if we want to type the multiple character instead of 1 character, we need colon. In this case, it will print all string from index 0 to index 3 which is "Zey" 
print(letter[0:]) #we have the deafult value for the start and end index. If we don't supply end index, python will return all the characters to the end of stringdatetime A combination of a date and a time
print(letter[1:]) # if we start with 1 then index 0 will be excluded
print(letter[:3]) # if we don't supply the end index, it will start with index 0 
print(part_letter)

'''
Now here is a a little exercise for you
The content is that define a variable, called name, and set it to Jennifer then print it 1 from -1
'''
