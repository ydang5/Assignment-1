def f_to_c (fahr):
    # Function of Fahrenheit to Celsius is: (F - 32) x .5556 = C
    c = (f - 32) * 0.5566
    return c

f = 75
c = f_to_c (f)
print("Fahrenheit of " + str (f) + " is " + str (c) + "in Celsius")
