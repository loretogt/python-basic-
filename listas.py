last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects= ["physics", "calculus", "poetry", "history" ]
grades=[98, 97, 85, 88]
subjects.append("computer science")
grades.append(100)

gradebook= list(zip(subjects, grades))
gradebook.append(("visual arts", 93))

full_gradebook= last_semester_gradebook+gradebook

print(full_gradebook)

################## Operaciones con listas ################

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len=len(inventory)
first=inventory[0]
last=inventory[-1]
inventory_2_6=inventory[2:6]
first_3=inventory[:3]
twin_beds=inventory.count('twin bed')
inventory.sort()

##################  Ejemplo de la pizeria ################

toppings= ["pepperoni", "pineapple", "cheese", "sausage", "olives", "olives", "mushrooms"]
prices=[2, 6, 1, 3, 2, 7, 2]
num_pizzas=len(toppings)
print ("We sell "+ str(num_pizzas) + " different kinds of pizza!")
pizzas= list(zip(prices, toppings))
print(pizzas)
pizzas.sort()
cheapest_pizza=pizzas[0]
priciest_pizza=pizzas[-1]
three_cheapest=pizzas[:3]
print(three_cheapest)
num_two_dollar_slices=prices.count(2)
print(num_two_dollar_slices)


################EJERCICIOS################

################ Double Index ################
def double_index(lst, index):
    if index < len(lst):
        lst[index] = lst[index] * 2
    return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))


################ Remove Middle ################
def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


################ More Than N ################
def more_than_n(lst, item, n):
    if lst.count(item)>n:
        return True
    else:
        return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


################ More Frequent Item ################
def more_frequent_item(lst, item1, item2):
    if lst.count(item1)>=lst.count(item2):
        return item1
    else:
        return item2

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


################ Middle Item ################
def middle_element(lst):
    if len(lst) % 2 == 0:
        sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
        return sum / 2
    else:
        return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))


################ Append Sum ################
def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))


################ Larger List################
def larger_list(lst1, lst2):
    if len(lst1)>=len(lst2):
        return lst1[-1]
    else:
        return lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


################ Combine Sort################
def combine_sort(lst1, lst2):
    sort_list=lst1+lst2
        sort_list.sort()
        return sort_list

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))


################ Append Size################
def append_size(lst):
    tam = len(lst)
    lst.append(tam)
    return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

################ Every Three Nums ################+
def every_three_nums(start):
    return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))
