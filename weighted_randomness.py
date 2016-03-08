import random
my_list = ['On-demand'] * 60 + ['Reserved'] * 20 + ['Spot'] * 10

for i in range(10):
	print random.choice(my_list)
