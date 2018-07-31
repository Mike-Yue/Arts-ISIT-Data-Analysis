import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import csv
import datetime
from datetime import timedelta

def content_check_heatmap_generator():
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
				weeks.append(date.strftime("%B %d, %Y"))
	else:
		weeks.append((date_list[0] - timedelta(date_list[0].weekday())).strftime("%B %d, %Y"))
		for date in date_list:
			if(date.weekday() == 0):
				weeks.append(date.strftime("%B %d, %Y"))

	trace = go.Heatmap(z=[content_check_monday, content_check_tuesday, content_check_wednesday, content_check_thursday, content_check_friday],
	                   x=weeks,
	                   y=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

	data=[trace]
	layout = go.Layout(
			title = 'Content Checks Completed Per Day',
			paper_bgcolor='rgba(0,0,0,0)',
			plot_bgcolor='rgba(0,0,0,0)',
			autosize = False,
			width = 1200, height = 500)
	fig = go.Figure(data = data, layout = layout)
	plotly.offline.plot(fig, filename='course-migration-content-check-heatmap.html')
	return trace

def double_check_heatmap_generator():
	date_primitives_list = []
	date_list = []
	double_check_total = []
	double_check_monday = []
	double_check_tuesday= []
	double_check_wednesday = []
	double_check_thursday = []
	double_check_friday = []
	list_for_double_checks = []
	list_for_double_checks.append(double_check_monday)
	list_for_double_checks.append(double_check_tuesday)
	list_for_double_checks.append(double_check_wednesday)
	list_for_double_checks.append(double_check_thursday)
	list_for_double_checks.append(double_check_friday)
	weeks = []

	with open('double_check.csv', 'r') as double_check_file:
		csv_double_data = csv.reader(double_check_file)
		next(csv_double_data)
		for row in csv_double_data:
			double_check_total.append(row[1])
			date_primitives_list.append(row[2])

	print(date_primitives_list)

	for primitive_date in date_primitives_list:
		split_date = primitive_date.split('/')
		date = datetime.date(int(split_date[2]), int(split_date[0]), int(split_date[1]))
		date_list.append(date)
	for i in range(0, date_list[0].weekday()):
		if(i >= 5):
			break
		else:
			list_for_double_checks[i].append('0')

	for i in range(0, len(date_list)):
		if(date_list[i].weekday() == 0):
			double_check_monday.append(double_check_total[i])
		elif(date_list[i].weekday() == 1):
			double_check_tuesday.append(double_check_total[i])
		elif(date_list[i].weekday() == 2):
			double_check_wednesday.append(double_check_total[i])
		elif(date_list[i].weekday() == 3):
			double_check_thursday.append(double_check_total[i])
		elif(date_list[i].weekday() == 4):
			double_check_friday.append(double_check_total[i])
		else:
			pass

	for i in range(date_list[len(date_list) - 1].weekday() + 1, 7):
		if(i >= 5):
			break
		else:
			list_for_double_checks[i].append('0')

	for check in list_for_double_checks:
		print(len(check))
		print(check)

	num_weeks = len(double_check_monday)
	if(date_list[0].weekday() == 0):
		for date in date_list:
			if(date.weekday() == 0):
				weeks.append(date.strftime("%B %d, %Y"))
	else:
		weeks.append((date_list[0] - timedelta(date_list[0].weekday())).strftime("%B %d, %Y"))
		for date in date_list:
			if(date.weekday() == 0):
				weeks.append(date.strftime("%B %d, %Y"))

	trace = go.Heatmap(z=[double_check_monday, double_check_tuesday, double_check_wednesday, double_check_thursday, double_check_friday],
	                   x=weeks,
	                   y=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

	data=[trace]
	layout = go.Layout(
			title = 'Double Checks Completed Per Day',
			paper_bgcolor='rgba(0,0,0,0)',
			plot_bgcolor='rgba(0,0,0,0)',
			autosize = False,
			width = 1200, height = 500)
	fig = go.Figure(data = data, layout = layout)
	plotly.offline.plot(fig, filename='course-migration-double-check-heatmap.html')
	return trace

def overall_heatmap_generator():
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
	double_check_total = []
	double_check_monday = []
	double_check_tuesday= []
	double_check_wednesday = []
	double_check_thursday = []
	double_check_friday = []
	list_for_double_checks = []
	list_for_double_checks.append(double_check_monday)
	list_for_double_checks.append(double_check_tuesday)
	list_for_double_checks.append(double_check_wednesday)
	list_for_double_checks.append(double_check_thursday)
	list_for_double_checks.append(double_check_friday)
	overall_monday = []
	overall_tuesday = []
	overall_wednesday = []
	overall_thursday = []
	overall_friday = []
	weeks = []

	with open('content_check.csv', 'r') as content_check_file:
		csv_content_data = csv.reader(content_check_file)
		next(csv_content_data)
		for row in csv_content_data:
			content_check_total.append(row[1])

	with open('double_check.csv', 'r') as double_check_file:
		csv_double_data = csv.reader(double_check_file)
		next(csv_double_data)
		for row in csv_double_data:
			double_check_total.append(row[1])
			date_primitives_list.append(row[2])

	for primitive_date in date_primitives_list:
		split_date = primitive_date.split('/')
		date = datetime.date(int(split_date[2]), int(split_date[0]), int(split_date[1]))
		date_list.append(date)

	for i in range(0, date_list[0].weekday()):
		if(i >= 5):
			break
		else:
			list_for_double_checks[i].append('0')
			list_for_content_checks[i].append('0')

	for i in range(0, len(date_list)):
		if(date_list[i].weekday() == 0):
			content_check_monday.append(content_check_total[i])
			double_check_monday.append(double_check_total[i])
		elif(date_list[i].weekday() == 1):
			content_check_tuesday.append(content_check_total[i])
			double_check_tuesday.append(double_check_total[i])
		elif(date_list[i].weekday() == 2):
			content_check_wednesday.append(content_check_total[i])
			double_check_wednesday.append(double_check_total[i])
		elif(date_list[i].weekday() == 3):
			content_check_thursday.append(content_check_total[i])
			double_check_thursday.append(double_check_total[i])
		elif(date_list[i].weekday() == 4):
			content_check_friday.append(content_check_total[i])
			double_check_friday.append(double_check_total[i])
		else:
			pass

	for i in range(date_list[len(date_list) - 1].weekday() + 1, 7):
		if(i >= 5):
			break
		else:
			list_for_content_checks[i].append('0')
			list_for_double_checks[i].append('0')

	for i in range(0, len(content_check_monday)):
		overall_monday.append(int(content_check_monday[i]) + int(double_check_monday[i]))
		overall_tuesday.append(int(content_check_tuesday[i]) + int(double_check_tuesday[i]))
		overall_wednesday.append(int(content_check_wednesday[i]) + int(double_check_wednesday[i]))
		overall_thursday.append(int(content_check_thursday[i]) + int(double_check_thursday[i]))
		overall_friday.append(int(content_check_friday[i]) + int(double_check_friday[i]))

	num_weeks = len(double_check_monday)
	if(date_list[0].weekday() == 0):
		for date in date_list:
			if(date.weekday() == 0):
				weeks.append(date.strftime("%B %d, %Y"))
	else:
		weeks.append((date_list[0] - timedelta(date_list[0].weekday())).strftime("%B %d, %Y"))
		for date in date_list:
			if(date.weekday() == 0):
				weeks.append(date.strftime("%B %d, %Y"))

	trace = go.Heatmap(z=[overall_monday, overall_tuesday, overall_wednesday, overall_thursday, overall_friday],
	                   x=weeks,
	                   y=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

	data=[trace]
	layout = go.Layout(
			title = 'Content/Double Checks Completed Per Day',
			paper_bgcolor='rgba(0,0,0,0)',
			plot_bgcolor='rgba(0,0,0,0)',
			autosize = False,
			width = 1200, height = 500)
	fig = go.Figure(data = data, layout = layout)
	plotly.offline.plot(fig, filename='course-migration-overall-heatmap.html')
	return trace


if __name__ == '__main__':
	with open('credentials.txt', 'r') as cred_file:
		username_password = cred_file.read()
		data = username_password.split(',')
	plotly.tools.set_credentials_file(username=data[0], api_key=data[1])

	content_check_list = content_check_heatmap_generator()
	double_check_list = double_check_heatmap_generator()
	overall_list = overall_heatmap_generator()

	data = [content_check_list, double_check_list, overall_list]

	updatemenus = list([
    dict(active=-1,
         buttons=list([   
            dict(label = 'Content Checks',
                 method = 'update',
                 args = [{'visible': [True, False, False]},
                         {'title': 'Content Check Heatmap'}]),
            dict(label = 'Double Checks',
                 method = 'update',
                 args = [{'visible': [False, True, False]},
                         {'title': 'Double Check Heatmap'}]),
            dict(label = 'Combined Checks',
                 method = 'update',
                 args = [{'visible': [False, False, True]},
                         {'title': 'Content/Double Check Combined Heatmap'}])
        	]),
    	)
	])

	layout = dict(showlegend=False, updatemenus=updatemenus, autosize = False, width = 1500, height = 600, paper_bgcolor='rgba(0,0,0,0)',	plot_bgcolor='rgba(0,0,0,0)')
	fig = dict(data=data, layout=layout)
	plotly.offline.plot(fig, filename='dropdown-heatmap.html')

