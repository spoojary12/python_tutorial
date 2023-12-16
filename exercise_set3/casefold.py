string = "WeightAGE oF THe DiScuSSiON"
# print the string after casefold transformation
print(string.casefold())

string = "WeightAGE oF THe DiScuSSiON"
# print the string after center transformation
print(string.center(25))

string = "WeightAGE oF THe DiScuSSiON"
char_count = string.count('e')
print(char_count)

title = 'Python Programming'

# change encoding to utf-8
print(title.encode())

message = 'Python is fun'

# check if the message ends with fun
print(message.endswith('fun'))


str = "xyz\t12345\tabc"
# tabsize is set to 2
print(str.expandtabs(2))
# tabsize is set to 3
print(str.expandtabs(3))

word = 'python is fun'
print(word.find('fun'))

str = "This article is written in {}"
print(str.format("Python"))

# input stored in variable a. 
a = {'x':'John', 'y':'Wick'} 
  
# Use of format_map() function 
print("{x}'s last name is {y}".format_map(a))

text = 'Python is fun'

# find the index of is
result = text.index('is')
print(result)

# here a,b and c are characters and 1,2 and 3
# are numbers
string = "abc123"
print(string.isalnum())

string = 'Ayush'
print(string.isalpha())

print("100".isdecimal())

string = '15460'
print(string.isdigit())

string = "Coding_101"
print(string.isidentifier())


s = 'this is good'
print(s.islower())

pin = "523"

# checks if every character of pin is numeric 
print(pin.isnumeric())

text = 'apple'

# returns True if text is printable 
result = text.isprintable()

print(result)

string = '\n \n \n'
 
print(string.isspace())
 