# This program which will provide the air quality rating of
# the `volatile organic compounds` (TVOC)

TVOC = 2398

if TVOC > 2200 and TVOC < 5500:
    print ("level 5, unhealty")

if TVOC > 660 and TVOC <= 2200:
    print ("level 4, poor")

if TVOC > 220 and TVOC <=660:
    print ("level 3, moderate")

if TVOC > 65 and TVOC <= 220:
    print ("level 2, good")

if TVOC <= 65:
    print ("level 1, excellent")
