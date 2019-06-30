premium=125.00

def cost_ground (weight):
    if weight<=2:
        return weight*1.5+20
    elif (weight>=2) and (weight<=6):
        return weight*3+20
    elif (weight>=6) and (weight<=10):
        return weight*4+20
        else:
    return weight*4.75+20


def cost_drone (weight):
    if weight<=2:
        return weight*4.5
    elif (weight>=2) and (weight<=6):
        return weight*9
    elif (weight>=6) and (weight<=10):
        return weight*12
    else:
        return weight*14.25


def shipping(weight):
    ground= cost_ground(weight)
    drone=cost_drone(weight)
    if (ground<drone) and (ground<premium):
        print ("The shipping method that is cheapest is the Ground Shipping")
        print ("It cost "+ str(ground)+ "$")
    if (drone<ground) and (drone<premium):
        print ("The shipping method that is cheapest is the Drone Shipping")
        print ("It cost "+ str(drone)+ "$")
    if (premium<drone) and (premium<ground):
        print ("The shipping method that is cheapest is the Ground Shipping")
        print ("It cost "+ str(premium)+ "$")


#Pruebas
print (cost_ground(8.4))
print (cost_drone(1.5))

print(shipping(4.8))
print(shipping(41.5))
