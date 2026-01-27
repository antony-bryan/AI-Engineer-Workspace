import random

# random_integer = random.randint(1,10)
# print(random_integer)


# random_number_0_to_1 = random.random() # 0.0 <= X < 1.0
# print(random_number_0_to_1)

random_coin_toss = random.randint(0,1)
if random_coin_toss == 0:
    print("Tails")
else:
    print("Heads")