#from ... imprort... (as  ...)
#datetime
#random -> random.choice() which takes a list as an argument and returns a number from the list
#            random.randint() which takes two numbers as arguments and generates a random number between the two numbers you passed in
#import module_name as name_you_pick_for_the_module
#random.sample() that takes a range and a number as its arguments. It will return the specified number of random numbers from that range.
#from decimal import Decimal
#pipenv



#A dictionary is an unordered set of key: value pairs. menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
#add a key my_dict["new_key"] = "new_value"
#If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.
#no puede haber dos keys iguales, si intentas crear la misma con otro valor lo que hace es cambiar el valor de la original
#juntar dos listas students = {key:value for key, value in zip(names, heights)}
#Acces to de value->  value= dictionary[key]
#Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will return None by default, podemos especificar el valor que queremos que devuelva si no existe
#   dictionary.get(key, valor si no esta)
# Delete a Key  We can use .pop() to do this. Just like with .get(), we can provide a default value to return if the key does not exist in the dictionary:
#Get All Keys list() function. Dictionaries also have a .keys() method that returns a dict_keys object.  dict_keys object is a view object, which provides a look at the current state of the dicitonary, without the user being able to modify anything
#Get All Values Dictionaries have a .values() method that returns a dict_values object
#Get All Items You can get both the keys and the values with the .items() method.  Each element of the dict_list returned by .items() is a tuple consisting of:   (key, value)

#################### Scrabble ##############
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points= {key:value for key, value in zip(letters, points)}

letter_to_points[" "]= 0

def score_words(word):
    point_total=0
    for i in word:
        point_total+=letter_to_points.get(i, 0)
    return point_total

brownie_points=score_words("BROWNIE")
print(brownie_points)

player_to_words={}
player_to_words={"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELL", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

for player, words in player_to_words.items():
    player_points=0
    for word in words:
        player_points+=score_words(word)
    player_to_words[player]= player_points

print(player_to_words)


#################### Sum Values ####################
def sum_values(my_dictionary):
    tot=0
    for key in my_dictionary:
        tot+=my_dictionary.get(key, 0)
    return tot


# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6


#################### Even Keys ####################
def sum_even_keys(my_dictionary):
    ret=0
    for key in my_dictionary:
        if  key%2==0:
            ret+= my_dictionary.get(key, 0)
    return ret

# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6


#################### Add Ten ####################
def add_ten(my_dictionary):
    for key in my_dictionary:
        my_dictionary[key]+=10
    return (my_dictionary)

# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}


#################### Values That Are Keys ####################
def values_that_are_keys(my_dictionary):
    res=[]
    val= my_dictionary.values()
    for key in my_dictionary:
        if key in val:
            res.append(key)
    return res

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]


#################### Largest Value ####################
def max_key(my_dictionary):
    largest_key= ""
    largest_value=float("-inf")
    for key in my_dictionary:
        if my_dictionary[key]>largest_value:
            largest_key=key
            largest_value= my_dictionary[key]
    return largest_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"


#################### Word Length Dict ####################
def word_length_dictionary(words):
    dic={}
    for elem in words:
        dic[elem]= len(elem)
    return dic

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}


#################### Frequency Count ####################
def frequency_dictionary(words):
    freqs = {}
    for word in words:
        if word not in freqs:
            freqs[word] = 0
        freqs[word] += 1
    return freqs

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}


#################### Unique Values ####################
def unique_values(my_dictionary):
    res=0
    unique=[]
    for key in my_dictionary:
        if my_dictionary[key] not in unique:
            unique.append(my_dictionary[key])
            res+=1
    return res


# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1


#################### Count First Letter ####################
def count_first_letter(names):
    letters = {}
    for key in names:
        first_letter = key[0]
        if first_letter not in letters:
            letters[first_letter] = 0
        letters[first_letter] += len(names[key])
    return letters

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
