import sys

counter1 = counter2 = 0
with open(sys.argv[1]) as file:
  for line in file:
    freq, letter, password = line.split(" ")
    low, high = map(int, freq.split('-'))
    count = len("".join([x for x in password if x == letter[:-1]]))
    if(count <= high) & (count >=low):
      counter1 = counter1 + 1
    if(password[low - 1] == letter[:-1]) ^ (password[high - 1] == letter[:-1]):
      counter2 = counter2 + 1
print(counter1, counter2)
