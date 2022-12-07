import collections

# create a counter to count the frequency of each character
freq = collections.Counter("hello world")
# print freq in accending order
freq = sorted(freq.items(), key=lambda x: x[1])
print(freq)
