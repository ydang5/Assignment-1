def c_to_k (c):
    #function convert is: c+ 273.15
    k = c + 273.15
    return k

celius = 25
k = c_to_k (celius)

print ("celius of " + str (celius) + " is " + str (k) + "in Kelvin")
