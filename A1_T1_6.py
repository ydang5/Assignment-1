# Kelvin to Fahrenheit
def k_to_f (k):
    # formular of Kelvin to Fahrenheit is (K − 273.15) × 9/5 + 32 = -F
    f = - (k - 273.15) * 9/5 +32
    return f

k = 300
f = k_to_f (k)

print("Kelvin of " + str (k) + " is " + str (f) + "in Fahrenheit")
