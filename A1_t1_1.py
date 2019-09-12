def c_to_f (c):
    #Formular = (c * 9/5) +32
    f = (c * 9/5) + 32
    return f

c = 25
f = c_to_f (c)

print("celius of " + str (c) + " is " + str (f) + "in Fahrenheit")
