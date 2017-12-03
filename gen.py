# https://stackoverflow.com/questions/11747254/python-brute-force-algorithm
# https://www.sentrylogin.com/sentry/NoSockets/loginActionAJAX.asp?Sentry_ID=13645&e=email&p=test&psist=1&ip=76.193.122.96&ms=1512334603040
import json

def generate(char_possibilies, char_range):
    complete_list = []
    for current in char_range:
        a = [i for i in char_possibilies]
        for y in xrange(current):
            a = [x+i for i in char_possibilies for x in a]
        complete_list = complete_list+a
        
    return complete_list

letter_list = generate('HJK', xrange(1,2))
number_list = generate('456', xrange(3,7))
    
complete_list = []
for letter_string in letter_list:
    for number_string in number_list:
        string = letter_string + number_string
        print string
        complete_list.append(string)
    
json_string = json.dumps(complete_list)

with open('output.json', 'w') as file:
    file.write(json_string)
    