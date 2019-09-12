def f_to_k(fahr):
    # formular to convert Fahrenheit to Kelvin is (F − 32) × 5/9 + 273.15 = K
    k = (f - 32) * 5/9 + 273.15
    return k

f = 70
k = f_to_k(f)
print("Fahrenheit of " + str (f) + " is " + str (k) + "in Kelvin")
