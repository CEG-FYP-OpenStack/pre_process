import csv
import collections

comb_dict = {}
with open('sample-dataset1.csv') as csvfile:
	i = 0
	reader = csv.reader(csvfile)
	for row in reader:
		if i > 0:
			if row[3] in comb_dict:
				comb_dict[row[3]].append(row[4])
			elif row[3] not in comb_dict:
				comb_dict[row[3]] = [row[4]]
		i += 1
for i in comb_dict:
	ram_list = comb_dict[i]
	unique_list = sorted(list(set(ram_list)))
	comb_dict[i] = unique_list
	print i + ':\n'
	print comb_dict[i]
	print '\n'

flavor_dict = {}
k = 0
for i in comb_dict:
	for j in comb_dict[i]:
		if i not in flavor_dict:
			flavor_dict[i] = {j:k}
			k += 1
		else:
			flavor_dict[i][j] = k
			k += 1
print '\n'
for i in flavor_dict:
	print '\n'
	print i
	print '\n'
	print flavor_dict[i]
	print '\n'
print flavor_dict

with open('sample-dataset1.csv') as fp:
	k = 0
	reader = csv.reader(fp)
	with open('sample.csv', 'wb') as fp2:
		writer = csv.writer(fp2)		
		writer.writerow(["Submit Time","Wait Time","Run Time","No. Allocated Processors","Requested Memory","Flavor"])
		for row in reader:
			if k > 0:
				new_row = row
				core = row[3]
				ram = row[4]
				core_dict = flavor_dict[core]
				new_row.append(core_dict[ram])
				writer.writerow(new_row)
			k += 1
