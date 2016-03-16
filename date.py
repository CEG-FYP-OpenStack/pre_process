import datetime
date1 = "1/1/70 12:00 AM"
date2 = "12/22/71 10:27 PM"

start = datetime.datetime.strptime(date1,"%m/%d/%y %H:%M %p")
end = datetime.datetime.strptime(date2,"%m/%d/%y %H:%M %p")
step = datetime.timedelta(minutes=1)
while start <= end:
	print start.strftime("%m/%d/%y %H:%M %p")
	start += step
