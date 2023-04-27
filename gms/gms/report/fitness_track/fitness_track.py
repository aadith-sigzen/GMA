# Copyright (c) 2023, Aadith and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	labels = []
	values = []
	for i in data:
		labels.append(i['date'])
		values.append(i['calories'])
	chart = {
        "type": "bar",
        "data": {
			"labels": labels,
			"datasets": [
				{"values": values},	
        	],
        }
    }
	return columns, data, "Calories", chart




def get_columns():
	return [
		"Weight:Float:200",
		"calories:int:200",
		"steps:int:200",
		"date:Date:200"
		
	]



def get_data(filters=None):
	data=[]
	from_date = None
	to_date = None	
	if filters.gym_member and filters.from_date and filters.to_date:
		from_date=datetime.strptime(filters.from_date, '%Y-%m-%d').date()
		to_date=datetime.strptime(filters.to_date, '%Y-%m-%d').date()
		doc= frappe.get_doc("Gym Member",filters.gym_member)
		for chi in doc.health_matrix:
			if from_date and to_date:
				if(from_date<=chi.date and to_date>=chi.date):
					row={
					"weight":chi.weight
					,"calories":chi.calories
                	,"steps":chi.steps
					,"date":chi.date
					}
					data.append(row)


	return data