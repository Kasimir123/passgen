# Imports the ability to save the list in a json format, DO NOT DELETE
import json

# Defines the function generate which creates the password combinations
def generate(char_possibilies, char_range):
    # Creates the empty list where the password combinations will be stored
    complete_list = []
    # The for loop which creates the password
    for current in char_range:
        a = [i for i in char_possibilies]
        for y in xrange(current):
            a = [x+i for i in char_possibilies for x in a]
        complete_list = complete_list+a
        
    return complete_list

# Defines the variables, the inputs are an example for which you know the first two characters in the password are either H, J, or K; and in which the 5 characters starting from the 3rd character are either 4, 5, or 6
letter_list = generate('HJK', xrange(1,2))
number_list = generate('456', xrange(3,5))

# If the generated password has several different parts like the example, this piece of code puts the pieces together 
complete_list = []
for letter_string in letter_list:
    for number_string in number_list:
        # Put the variables containing all the pieces of the password in the order that you want
        string = letter_string + number_string
        # Lets you see the possible combinations in your terminal while it is running, allows you to see if it is running correctly and how the progress is going, can be deleted to speed up process
        print string
        complete_list.append(string)

# Turns the Python list into json data
json_string = json.dumps(complete_list)

# Puts the data into a .json file
with open('output.json', 'w') as file:
    file.write(json_string)
    