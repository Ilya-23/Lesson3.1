calls = 0

def count_calls():
   global calls
   calls += 1

def string_info(string):
    count_calls()
    tuple_1 = (len(string), string.upper(), string.lower())
    return tuple_1

def is_contains(string, list_to_search):
    count_calls()
    contains = True
    for i in range(len(list_to_search)):
        if string.upper() == list_to_search[i].upper():
            contains = True
            break
        else:
            contains = False
    return contains

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)









