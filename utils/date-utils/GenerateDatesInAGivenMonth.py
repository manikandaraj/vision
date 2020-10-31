import os
import argparse
import traceback
from datetime import datetime
from datetime import date
import calendar

def main(argObj):
	try:
		todayDate = date.today()
		year = todayDate.year
		month = todayDate.month
		if(argObj.year is not None and argObj.month is not None):
			year = int(argObj.year)
			month = int(argObj.month)
		numOfDays = calendar.monthrange(year, month)[1]
		daysInMonth = [date(year, month, day) for day in range(1, numOfDays+1)]
		dateFormat = "%b %d, %Y %A"
		for dateObj in daysInMonth:
			print(dateObj.strftime(dateFormat))
	except Exception as excepErr:
		print("Exception in main() -> :{}:".format(excepErr))
		print("Traceback -> :{}:".format(traceback.format_exc()))

if __name__ == '__main__':
	scrDir = os.path.dirname(os.path.realpath(__file__))
	print("Current Working Directory -> :{}:".format(scrDir))
	parser = argparse.ArgumentParser(description='Script for Getting Dates of Days in a Month')
	parser.add_argument('-y', dest='year', action='store', required=False, help='Year in 4 Digit Format')
	parser.add_argument('-m', dest='month', action='store', required=False, help='Month in 2 Digit Format')
	argArr = parser.parse_args()
	main(argArr)

