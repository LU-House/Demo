first = 'Your first name'
last = 'Your last name'
message = first + '['+ last +'] is a coder' # This method is perfectly works, but it's not ideal because as our text gets more complicated it becomes harder to visualize the output. That's why we need to use formatted strings, they make it easier for us to visualize the output.
print(message) 

# So, Let's make another variable, we can use f'' to represent the function of formatted string. 
msg = f'{first} [{last}] is a coder' # Then, we add curly braces, curly braces is the place for variable. With these curly braces, we're defining place holders or holes in our string, and when we run our program these holes will be filled with the value of our variables. So here we have two place holders. Based on this formatted string, we can easily visualize what the output looks like. Now let's print it on the terminal. Making sure we can get the exactly same output. 
print(msg)