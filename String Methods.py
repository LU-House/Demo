#In this chapter, I'm going to show you some really cool things you can do with Python String
course = 'Python Is Great'
# Now, In order to calculate the number of characters in this string, you can use a built in function called len
print(len(course)) # it's particulary useful when you receive input from the user. For example you have noticed that when you fill out a form online, each input field often has a limit. For example, you might have 50 characters for your name. So using this len function we can enforce a limit on the number of characters in an input field. If the user types in more characters than we allow, we can display an error, this len function is another function built into Python, it's a general purpose function, so it's not limited to counting the number of characters in a string, in the future when we look at lists, I want to show you that we can use this function to count the number of items in a list, So it's a general purpose function.
# Now we also have functions specifically for strings. For example we have functions for coverting all these characters to upper case or lower case. To access these functions we use the dot operator. 
#Then I want you type course then dot look these are all the functions that are specific to strings. Now in accurate terms, we refer to these function as methods, this is a term in object oriented programming that we want to look at in the future. but for now, what I want you take away is that when a function belongs to something else, or is specifc to some kind of object, we refer to that function as a method.
#For example, here we have this function, upper, for converting the string into upper case. More accurately because this function is specific to a string, we refer to this as a method. In contrast, len and print are general purpose functions, they don't belong to string or number or other kinds of objects. So this is the difference between functions and methods. 
print(course.upper())
#Note that this method does not change or modify our original string, in fact, it creates a new string and return it
print(course)
# if we print our course variable right after we call the upper method, we can see that our course variable still has its original form. 
print(course.lower())
print(course.title())
print(course.find('Python')) # we also gonna learn about the find method which returns the index of a character or sequence of characters
print(course.replace('P','L')) # we also have replace method for replacing characters and words in s string
# One last things I want to show you in this chapter, There are times that you want to check the existence of a character or sequence of characters in your string. In those situations you use the in operator. So let's say you want to know if this string contains the word python. 
# WE can write an expression like this. String Python in course, SO we 're checking to see if python is in course variable. and this is an expression that produces a boolean value, and I get true and false, so we refer to this expression
print('Python' in course)