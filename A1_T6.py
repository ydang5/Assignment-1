import statistics
#1 Given array data, find single mode value


values = [80, 90, 100, 150, 120, 110, 160, 110, 100]

# mode = statistics.mode(values)
#
# print(mode)
#
# #2 Given array data, find multiple mode values
# # This code demonstrates that we cannot calculate mode value because there
# # are more then one mode.
#
# arr_2 = [4, 5, 2, 6, 3, 7, 8, 9, 6, 5, 2]
#
# mode = statistics.mode(arr_2)
#
# print(mode)
#
# #3 Given array data, find range
#
# arr_3 = [21, 23, 26, 22, 25, 20, 19, 23]
#
# print(arr_3[0:lenth(arr_3)])


# 4. Given array data, find standard deviation

sample = [1, 2, 3, 4, 5]

# print standard deviation
# xbar is set to default value of 1
value = statistics.stdev(sample)
print ("Standard Deviation of sample is %s " % value)


# 5. Given array data, find variance
# creating a simple data - set
sample = [1, 2, 3, 4, 5]
# Prints standard deviation
# xbar is set to default value of 1
value = statistics.variance(sample)
print("Variance of sample is % s " % value)
