#Instantiating a class looks a lot like calling a function. We would be able to create an instance of our defined CoolClass as follows: cool_instance = CoolClass()
#A class instance is also called an object.
#object.variable  class variable is a variable that’s the same for every instance of the class.
#Methods are functions that are defined as part of a class. The first argument in a method is always the object that is calling the method. Convention recommends that we name this first argument self.
#__init__ method is used to initialize a newly created object Methods that are used to prepare an object being instantiated are called constructors.
#Instance variables and class variables are both accessed similarly in Python.
#hasattr() will return True if an object has a given attribute and False otherwise
#getattr() is a Python function that works a lot like the usual dot-syntax (i.e., object_name.attribute_name) but we can supply a third argument that will be the default if the object does not have the given attribute.
#We can use the dir() function to investigate an object’s attributes at runtime
#__repr__. This is a method we can use to tell Python what we want the string representation of the class to be. __repr__ can only have one parameter, self, and must return a string.

################## example ##################

class Student:
    def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
        
    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)

class Grade:
    minimum_passing = 65
        
    def __init__(self, score):
        self.score = score

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))


#Inheritance    class clase_hija(clase_padre)
# An Exception is a class that inherits from Python’s Exception class.
#We can validate this ourselves using the issubclass() function. returns True if the first argument is a subclass of the second argument
#An overridden method is one that has a different definition from its parent class
#super() gives us a proxy object. With this proxy object, we can invoke the method of an object’s parent class (also called its superclass). We call the required function as a method on super()
# An interface in Python usually refers to the names of the methods and the arguments they take
#Polymorphism is the term used to describe the same syntax doing different actions depending on the type of data.
#Python gives us the power to define dunder methods that define a custom-made class to look and behave like a Python builtin. Python offers the dunder method __add__
#__init__, our constructor, which sets a list of users to the instance variable self.user_list and sets the group’s permissions when we create a new UserGroup
#__iter__, the iterator, we use the iter() function to turn the list self.user_list into an iterator so we can use for user in user_group syntax.
#__len__, the length method, so when we call len(user_group) it will return the length of the underlying self.user_list list.
#__contains__, the check for containment, allows us to use user in user_group syntax to check if a User exists in the user_list we have.

class Menu:
    def __init__(self, name, items, start_time, end_time):
    self.name= name
    self.items= items
    self.start_time=start_time
    self.end_time= end_time
        
    def __repr__(self):
        return self.name + ' menu avaliable form '+ str(self.start_time)+ '-'+str(self.end_time)
                
    def calculate_bill(self, purchased_items):
        bill=0
        for p_item in purchased_items:
            if p_item in self.items:
                bill+= self.items[p_item]
        return bill


class Franchise:
    def __init__(self, address, menus):
    self.address= address
    self.menus= menus
        
    def __repr__(self):
        return self.address
                
    def available_menus(self, time):
        avali=[]
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                avali.append(menu)
        return avali

class Business:
    def __init__(self, name, franchises):
    self.name= name
    self.franchises= franchises

#Brunch
brunch_items=   {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch= Menu('Brunch', brunch_items, 1100, 1600)
#test
#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee' ]))

#Early Bird
early_bird_items={
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird= Menu('Early Bird', early_bird_items, 1500, 1800)

#Dinner
diner_bird_items= {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner= Menu('Dinner', diner_bird_items, 1700, 2300)


#Kids menu
kids_bird_items= {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids= Menu('Kids menu', kids_bird_items, 1100, 2100)

menus= [brunch, early_bird, dinner, kids]

flagship_store= Franchise('1232 West End Road', menus)
new_installment= Franchise('12 East Mulberry Street', menus)

#print(flagship_store.available_menus(1200))
#print(flagship_store.available_menus(1700))

basta= Business("Basta Fazoolin' with my Hear", [flagship_store, new_installment])

arepa_items= {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu= Menu("Take a’ Arepa", arepa_items, 1000, 20000)

arepas_place= Franchise('189 Fitzgerald Avenue', [arepas_menu])

arepa= Business("Take a' Arepa", [arepas_place])

#print(arepa.franchises[0].menus[0])
