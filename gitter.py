import random as rnd

rnd.randint(1,17)

# iterate 100 times and print if the random  number is 17
for i in range(100):
    if rnd.randint(1,17) == 17:
        print("17")