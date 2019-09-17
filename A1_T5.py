# This code takes a list of integers and I got help from this mathematics
# links via https://www.purplemath.com/modules/meanmode.htm
#-------------------------------------------------------------------------------
# ALOGIRTHM
# STEP 1: Organize the list of numbers from greater to lower.
# STEP 2: Find the "Middle value".
# STEP 2 (A): Find median with EVEN middle value.
# STEP 2 (B): Find median with ODD middle value.
#-------------------------------------------------------------------------------
power_arr = [4, 5, 2, 6, 3, 7, 8, 9, 6, 5, 2] # GOAL: [13, 13, 13, 13, 14, 14, 16, 18, 21]
# STEP 1: Organize the list of numbers from greater to lower.
power_arr.sort()
# STEP 2: Find the "Middle value".
# The following code will tell me if the number is odd or even. I took this info
# from the following link: https://www.c-sharpcorner.com/blogs/python-program-to-check-odd-or-even1
a = len(power_arr)
print("The number of items inside list is", a)
def find_middle(input_list):
   """
   Code taken from https://stackoverflow.com/a/38130999
   """
   middle = float(len(input_list))/2
   return (input_list[int(middle)], input_list[int(middle-1)])
# STEP 2 (A): Find median with EVEN middle value.
middle_value = 0
if(a%2==0): #Even Odd Program using Modulus Operator (the)
   print("This Number is Even")
   x, y = find_middle(power_arr)
   middle_value = (x + y) / 2
# STEP 2 (B): Find median with ODD middle value.
else:
   print("This Number is Odd")
   middle_index = float(len(power_arr))/2
   print("The middle index is", middle_index)
   middle_value = power_arr[int(middle_index - .5)]
# Return the median
print("The median is", middle_value)
