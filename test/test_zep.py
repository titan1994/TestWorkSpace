values = [1.34, 3.25, 2.99]
coefficient = [3, 2, 2]

for i, j in zip(values, coefficient):
    print(i * j)


scores = [54,67,48,99,27]
for i, score in enumerate(scores):
   print(i, score)

print(enumerate(scores))


rg_test = range(1,20)

print(rg_test)

my_crazy_iterator = iter(rg_test)
print(my_crazy_iterator)
print(next(my_crazy_iterator))