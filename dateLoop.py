import urllib2
import re
import time
import sys
import getopt
from datetime import date, timedelta

usage = 'dateLoop.py -a <startYear> -b <startMonth> -c <endYear> -d <endMonth>'
query = ''
label = ''
csvCount = ''
csvDates = ''
dateCounter = 1

try:
	opts, args = getopt.getopt(sys.argv[1:],"hu:p:a:b:c:d:o:r:q:l:")
except getopt.GetoptError:
	print usage
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		print usage
		sys.exit()
	elif opt in ("-a"):
		startYear = int(arg)
	elif opt in ("-b"):
		startMonth = int(arg)
	elif opt in ("-c"):
		endYear = int(arg)
	elif opt in ("-d"):
		endMonth = int(arg)

startDate = date(startYear, startMonth, 1)
endDate = date(endYear, endMonth, 1)
errorCount = 0

while startDate + timedelta(days=1) <= endDate:

	try:

		formattedDate = str(startDate.year) + '-' + str(startDate.month).zfill(2) +'-' + str(startDate.day).zfill(2)

		print formattedDate
		csvCount += str(-99) + ','
		csvDates += str(dateCounter) + ','
		dateCounter += 1
		
		startDate += timedelta(days=1)
		sys.stdout.flush()
	except Exception:
		print "error!"
		errorCount += 1
print "DONE! Error total = " + str(errorCount)

if csvCount[-1:] == ",":
    csvCount = csvCount[:-1]

if csvDates[-1:] == ",":
	csvDates = csvDates[:-1]
		
print "CSV dates = " + str(csvDates)
print "CSV count = " + str(csvCount)
sys.stdout.flush()
