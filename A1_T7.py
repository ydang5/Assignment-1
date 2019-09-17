# This program checks carbon dioxide data to reflect air quality

CO2_value = 2000

if CO2_value >= 1600:
    print("Air quality is BAD, and ventilation is required")

elif CO2_value >= 1100 and CO2_value < 1600:
    print("Air quality is MEDICORE, and ventilation is recommended")

elif CO2_value >= 900 and CO2_value < 1100:
    print("Air quality is FAIR")

elif CO2_value >=700 and CO2_value < 900:
    print("Air quality is GOOD")

elif CO2_value < 700:
    print ("Air quality is EXCELLENT")
