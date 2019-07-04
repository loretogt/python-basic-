#.lower() returns the string with all lowercase characters.
#.upper() returns the string with all uppercase characters.
#.title() returns the string in title case, which means the first letter of each word is capitalized.
#.split() eturned a list with each word in the string.
#.join() is essentially the opposite of .split(), it joins a list of strings together with a given delimiter. entre parentesis el objeto y antes el delimitador
#.strip(). Stripping a string removes all whitespace characters from the beginning and end. You can also use .strip() with a character argument, which will strip that character from either end of the string, pero aqui no te quita los espacios, sino lo que le pases como argumento
#.replace(). Replace takes two arguments and replaces all instances of the first argument in a string with the second argument. The syntax is as follows
        #string_name.replace(character_being_replaced, new_character)
#.find() It then returns the first index value where that string is located.
#.format() takes variables as an argument and includes them in the string that it is run on. You include {} marks as placeholders for where those variables will be imported.
        #def favorite_song_statement(song, artist):
            #return "My favorite song is {} by {}.".format(song, artist)
        #def favorite_song_statement(song, artist):
            #return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

#################### ejercicio Thread Shed ####################

daily_sales = \
"""Edith Mcbride   ;,;$1.21   ;,;   white ;,;
    09/15/17   ,Herbert Tran   ;,;   $7.29;,;
    white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52
    ;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell
    ;,;   $5.13   ;,; white   ;,; 09/15/17,
    Eduardo George   ;,;$20.39;,; white&yellow
    ;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;
    purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,;
    purple&yellow ;,;09/15/17,   Shaun Brock;,;
    $17.98;,;purple&yellow ;,; 09/15/17 ,
    Erick Harper ;,;$17.41;,; blue ;,; 09/15/17,
    Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   ,
    Carroll Boyd;,; $14.51;,;   purple&blue   ;,;
    09/15/17   , Teresa Carter   ;,; $19.64 ;,;
    white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40
    ;,; white&red   ;,; 09/15/17, Craig Chambers;,;
    $8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,;
    09/15/17   ,   Marvin Morgan;,;   $16.49;,;
    green&blue&red   ;,;   09/15/17 ,Marjorie Russell
    ;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
    Israel Cummings;,;   $11.86   ;,;black;,;
    09/15/17,   June Doyle   ;,;   $22.29 ;,;
    black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;
    $8.35;,;   white&black&yellow   ;,;   09/15/17,
    Rhonda Farmer;,;$2.91 ;,;   white&black&yellow
    ;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green
    ;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow
    ;,; 09/15/17   ,Hubert Miles;,;   $3.59
    ;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue
    ;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;
    black   ;,;   09/15/17 , Audrey Ferguson ;,;
    $5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,;
    $17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
    Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;
    09/15/17,   Shannon Chavez   ;,;$19.26   ;,;
    yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;
    yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50
    ;,;   yellow;,;   09/15/17, Ruben Jones   ;,;
    $14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
    ;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,;
    black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67
    ;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;
    $8.31;,;   black&red ;,;   09/15/17,   Stacey Payne
    ;,;   $15.70   ;,;   white&black&red ;,;09/15/17
    ,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,;
    09/15/17 , Melody Moran ;,;   $30.84
    ;,;yellow&black;,;   09/15/17 , Louise Becker   ;,;
    $12.31 ;,; green&yellow&black;,;   09/15/17 ,
    Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17
    ,Justin Blake ;,; $22.46   ;,;white&yellow ;,;
    09/15/17,   Beverly Baldwin ;,;   $6.60;,;
    white&yellow&black ;,;09/15/17   ,   Dale Brady
    ;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   ,
    Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17
    ,Sonja Barnett ;,; $14.22 ;,;white&black;,;
    09/15/17, Angelica Garza;,;$11.60;,;white&black
    ;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,;
    white&black&red ;,;09/15/17   ,   Rex Hudson
    ;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs
    ;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   ,
    Hannah Pratt;,;   $22.61   ;,;   purple&yellow
    ;,;09/15/17,Gayle Richards;,;$22.19 ;,;
    green&purple&yellow ;,;09/15/17   ,Stanley Holland
    ;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
    Terrance Saunders ;,;   $23.70  ;,;green&yellow&red
    ;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,;
    red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,;
    green&red ;,;   09/15/17   ,Irving Patterson
    ;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17,
    Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17,
    Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   ,
    Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17
    ,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
    Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17
    , Beatrice Newman ;,;$22.45   ;,;white&purple&red
    ;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;
    red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;
    black&red;,; 09/15/17,   Javier Bailey   ;,;
    $24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,
    Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17
    ,   Traci Craig ;,;$0.65;,; green&yellow;,;
    09/15/17 , Jeffrey Jenkins   ;,;$26.45;,;
    green&yellow&blue   ;,;   09/15/17,   Merle Wilson
    ;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin
    ;,;$8.74   ;,; purple&black   ;,;09/15/17 ,
    Leonard Guerrero ;,;   $1.86   ;,;yellow
    ;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;
    09/15/17   ,Donna Ball ;,; $28.10  ;,;
    yellow&blue;,;   09/15/17   , Terrell Barber   ;,;
    $9.91   ;,; green ;,;09/15/17   ,Jody Flores;,;
    $16.34 ;,; green ;,;   09/15/17,   Daryl Herrera
    ;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,
    Rogelio Gonzalez;,; $9.51;,;   white&black&blue
    ;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,;
    green;,;   09/15/17,Owen Ward;,; $21.64   ;,;
    green&yellow;,;09/15/17,Malcolm Morales ;,;
    $24.99   ;,;   green&yellow&black;,; 09/15/17 ,
    Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17
    ,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17
    , Leticia Manning;,;$15.70 ;,; green&purple;,;
    09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,;
    09/15/17,Lewis Glover;,;   $13.66   ;,;
    green&white;,;09/15/17,   Gail Phelps   ;,;$30.52
    ;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris
    ;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

#------------------------------------------------
# Start coding below!

daily_sales_replaced=daily_sales.replace(";,;",'+')

#separamos cada daily transaction
daily_transactions=daily_sales_replaced.split(',')
#print(daily_transactions)

daily_transactions_split=[]
for trans in daily_transactions:
    daily_transactions_split.append(trans.split('+'))
#print(daily_transactions_split)

transactions_clean = []
for trans in daily_transactions_split:
    trans_clean = []
    for data in trans:
    trans_clean.append(data.replace("\n","").strip(" "))
        transactions_clean.append(trans_clean)

#print(transactions_clean)

customers=[]
sales=[]
thread_sold=[]

for trans in transactions_clean:
    customers.append(trans[0])
    sales.append(trans[1])
    thread_sold.append(trans[2])

#print(customers)
#print(sales)
#print(thread_sold)

total_sales=0
for sale in sales:
    total_sales+=float(sale.strip('$'))
#print (total_sales)

#print(thread_sold)

thread_sold_split=[]
for sale in thread_sold:
    for color in sale.split('&'):
        thread_sold_split.append(color)
#print(thread_sold_split)

def color_count (color):
    cont=0
        for col in thread_sold_split:
            if col== color:
                cont+=1
                    return cont

print(color_count('white'))

colors = ['red','yellow','green','white','black','blue','purple']

for color in colors:
    print ("Thread Shed sold {0} threads of {1} thread today.".format(color_count(color),color ))


#################### ejercicio Count Letters ####################
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
    uniques = 0
    for letter in letters:
        if letter in word:
            uniques += 1
    return uniques

# Uncomment these function calls to test your tip function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4


#################### ejercicio Count X ####################
# Write your count_char_x function here:
def count_char_x(word,x):
    cont=0
    for let in word:
        if let==x:
            cont+=1
    return cont

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
#should print 1


#################### ejercicio Count Multi Xfor ####################
# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
    splits = word.split(x)
    return(len(splits)-1)

# Uncomment these function calls to test your  function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1


#################### ejercicio Substring Between ####################
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
    start_ind = word.find(start)
    end_ind = word.find(end)
    if start_ind > -1 and end_ind > -1:
        return(word[start_ind+1:end_ind])
    return word

# Uncomment these function calls to test your tip function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


#################### ejercicio X Length ####################
def x_length_words(sentence, x):
    lst= sentence.split(" ")
    for word in lst:
        if len(word)<x:
            return False
    return True

# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True


#################### ejercicio Check Name ####################
def check_for_name(sentence, name):
    lst=sentence.split(" ")
    for word in lst:
        if name.lower()==word.lower():
            return True
    return False

# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False


#################### ejercicio Every Other Letter ####################
def every_other_letter(word):
    every_other = ""
    for i in range(0, len(word), 2):
        every_other += word[i]
    return every_other

# Uncomment these function calls to test your tip function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print


#################### ejercicio Reverse ####################
def reverse_string(word):
    reverse = ""
    for i in range(len(word)-1, -1, -1):
        reverse += word[i]
    return reverse

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print


#################### ejercicio Make Spoonerism ####################
def make_spoonerism(word1, word2):
    return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

# Uncomment these function calls to test your tip function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a


#################### ejercicio Add Exclamation ####################
def add_exclamation(word):
    while(len(word) < 20):
        word += "!"
    return word

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
