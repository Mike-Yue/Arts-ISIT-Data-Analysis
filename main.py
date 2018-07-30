import matplotlib
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import csv
import datetime
from datetime import timedelta

date_primitives_list = []
date_list = []
content_check_total = []
content_check_monday = []
content_check_tuesday= []
content_check_wednesday = []
content_check_thursday = []
content_check_friday = []
list_for_content_checks = []
list_for_content_checks.append(content_check_monday)
list_for_content_checks.append(content_check_tuesday)
list_for_content_checks.append(content_check_wednesday)
list_for_content_checks.append(content_check_thursday)
list_for_content_checks.append(content_check_friday)
weeks = []

with open('credentials.txt', 'r') as cred_file:
	username_password = cred_file.read()
	data = username_password.split(',')
print(data)


plotly.tools.set_credentials_file(username=data[0], api_key=data[1])

with open('content_check.csv', 'r') as content_check_file:
	csv_content_data = csv.reader(content_check_file)
	next(csv_content_data)
	for row in csv_content_data:
		content_check_total.append(row[1])
		date_primitives_list.append(row[2])


for primitive_date in date_primitives_list:
	split_date = primitive_date.split('-')
	date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
	date_list.append(date)

for i in range(0, date_list[0].weekday()):
	if(i >= 5):
		break
	else:
		list_for_content_checks[i].append('0')

for i in range(0, len(date_list)):
	if(date_list[i].weekday() == 0):
		content_check_monday.append(content_check_total[i])
	elif(date_list[i].weekday() == 1):
		content_check_tuesday.append(content_check_total[i])
	elif(date_list[i].weekday() == 2):
		content_check_wednesday.append(content_check_total[i])
	elif(date_list[i].weekday() == 3):
		content_check_thursday.append(content_check_total[i])
	elif(date_list[i].weekday() == 4):
		content_check_friday.append(content_check_total[i])
	else:
		pass

for i in range(date_list[len(date_list) - 1].weekday() + 1, 7):
	if(i >= 5):
		break
	else:
		list_for_content_checks[i].append('0')

for check in list_for_content_checks:
	print(len(check))
	print(check)

num_weeks = len(content_check_monday)
if(date_list[0].weekday() == 0):
	for date in date_list:
		if(date.weekday() == 0):
			weeks.append('Week of ' + date.strftime("%B %d, %Y"))
else:
	weeks.append('Week of ' + (date_list[0] - timedelta(date_list[0].weekday())).strftime("%B %d, %Y"))
	for date in date_list:
		if(date.weekday() == 0):
			weeks.append('Week of ' + date.strftime("%B %d, %Y"))

trace = go.Heatmap(z=[content_check_monday, content_check_tuesday, content_check_wednesday, content_check_thursday, content_check_friday],
                   x=weeks,
                   y=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

data=[trace]
py.plot(data, filename='course-migration-heatmap')
