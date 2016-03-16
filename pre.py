import csv

import collections
import random
import pprint
from datetime import datetime, timedelta

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
#print flavor_dict
#Flavors Generation
with open('sample-dataset1.csv') as fp:
	k = 0
	reader = csv.reader(fp)
	with open('sample.csv', 'wb') as fp2:
		writer = csv.writer(fp2)		
		writer.writerow(["Submit Time","Wait Time","Run Time","No. Allocated Processors","Requested Memory","Flavor"])
		for row in reader:
			if k > 0 and k <= 1000:
				new_row = row
				core = row[3]
				ram = row[4]
				core_dict = flavor_dict[core]
				new_row.append(core_dict[ram])
				writer.writerow(new_row)
			k += 1
#Random Instance type allocation
new_data_set = []
with open('sample.csv') as fp:
	k = 0
	reader = csv.reader(fp)
	with open('final.csv','wb') as fp2:
		#Weighted randomness
		od_count = 0
		r_count = 0
		s_count = 0
		choices_list = ['On-demand'] * 60 + ['Reserved'] * 20 + ['Spot'] * 10
		writer = csv.writer(fp2)
		writer.writerow(["Submit Time","Wait Time","Run Time","No. Allocated Processors","Requested Memory","Flavor","Instance Type","Priority"])
		for row in reader:
			if k > 0:
				new_row = row
				priority = ""
				random_instance_type = random.choice(choices_list)
				if random_instance_type == 'On-demand':
					od_count += 1
					priority = "high"
				elif random_instance_type == 'Reserved':
					r_count += 1
					priority = "low"
				else:
					s_count += 1
					priority = "low"		
				new_row.append(random_instance_type)
				new_row.append(priority)
				new_data_set.append(new_row)
				writer.writerow(new_row)
			k += 1

		print 'On-demand instances: ' + str(od_count)
		print 'Reserved instances: ' + str(r_count)
		print 'Spot instances: ' + str(s_count)

date_list = []
init = "1/1/70 12:00 AM"
final = "12/22/71 10:27 PM"
start = datetime.strptime(init,"%m/%d/%y %I:%M %p")
end = datetime.strptime(final, "%m/%d/%y %I:%M %p")
step = timedelta(minutes=1)
while start <= end:
	date = start.strftime("%m/%d/%y %I:%M %p")
	date_list.append(date)
	start += step

print date_list[:8]

with open('final1.csv','wb') as ff:
	writer = csv.writer(ff)
	writer.writerow(["Submit Time","Wait Time","Run Time","No. Allocated Processors","Requested Memory","Flavor","Instance Type","Priority"])
	for i in date_list:
		# print if
		flag = 0
		for j in new_data_set:
			# print "SAleem"
			# print i 
			# # print j[0]
			# if i == "01/01/70 12:07 AM" and j[0] == "01/01/70 12:07 AM":
			# 	print i
			# 	print j[0]
			# 	print "Salee"
			# 	print "Sake"
			if datetime.strptime(i,"%m/%d/%y %I:%M %p") == datetime.strptime(j[0],"%m/%d/%y %I:%M %p"):
				writer.writerow(j)
				print i
				print j[0]
				# print datetime.strptime(j[0],"%m/%d/%y %I:%M %p")
				break
			else:
				# print i
				flag = 1
		if flag == 1:
				writer.writerow([i,"-","-","NA","NA","NA","NA","NA"])