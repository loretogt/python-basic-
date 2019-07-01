################ Carly's Clippers ejercio ###################
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price=0

for i in prices:
    total_price+=i

average_price=total_price/len(prices)

print("Average Haircut Price: " + str(average_price))

new_prices=[price-5 for price in prices]

print(new_prices)

total_revenue=0

for i in range(len(hairstyles)):
    total_revenue=prices[i]*last_week[i]

print("Total Revenue: "+ str(total_revenue))

average_daily_revenue=total_revenue/7

#haurstyles under 30 NO FUNCIONA
new_list = [old_list[i] for i in range(old_list) if different_list[i] < 0]
cuts_under_30= [hairstyles[i] for i in range(hairstyles) if prices[i]< 30]

print(cuts_under_30)


################### Divisible by Ten ###################
def divisible_by_ten(nums):
    n=0
    for i in nums:
        if i%10==0:
            n+=1
    return n

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))


################### Greetings ###################
def add_greetings(names):
    saludo=[]
    for name in names:
    saludo.append("Hello, "+ name)
        return saludo



#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))


################### Delete Starting Even Numbers ###################
def delete_starting_evens(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


################### Odd Indices ###################
def odd_indices(lst):
    new_lst = []
    for index in range(1, len(lst), 2):
        new_lst.append(lst[index])
    return new_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))


################### Exponents ###################
def exponents(bases, powers):
    new_lst = []
    for base in bases:
        for power in powers:
            new_lst.append(base ** power)
    return new_lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))


################### Larger Sum ###################
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for number in lst1:
        sum1 += number
    for number in lst2:
        sum2 += number
    if sum1 >= sum2:
        return lst1
    else:
        return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))


################### Over 9000 ###################
def over_nine_thousand(lst):
    sum=0
    for i in lst:
        sum+=i
        if sum >=9000 :
            break
    return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))


################### Max Num ###################
def max_num(nums):
    max=nums[0]
    for i in nums:
        if max < i:
            max=i
    return max

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))


################### Same Values ###################
def same_values(lst1, lst2):
    res=[]
    i=0
    while i< len(lst1):
        if lst1[i]==lst2[i]:
            res.append(i)
        i=i+1
    return res

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


################### Reversed List ###################
def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if lst1[index] != lst2[len(lst2) - 1 - index]:
            return False
    return True
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

