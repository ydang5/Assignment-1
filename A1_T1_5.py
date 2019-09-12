# Kelvin to Celsius
def k_to_c (celsius):
    #formular for Kelvin to Celsius is C = K - 273.15
    c = k - 273.15
    return c

k = 300
c = k_to_c (k)
c_rounded = round(c , 2)

print ("Kelvin of " + str (k) + " is " + str (c_rounded) + "in Celsius")
