import urllib2
import re
import time
import sys
import getopt
from datetime import date, timedelta

usage = 'bugCounter.py -u <githubUsername> -p <githubPassword> -a <startYear> -b <startMonth> -c <endYear> -d <endMonth> -o <owner> -r <repository> -q <query> -l <label>'
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
	elif opt in ("-u"):
		username = arg
	elif opt in ("-p"):
		password = arg
	elif opt in ("-a"):
		startYear = int(arg)
	elif opt in ("-b"):
		startMonth = int(arg)
	elif opt in ("-c"):
		endYear = int(arg)
	elif opt in ("-d"):
		endMonth = int(arg)
	elif opt in ("-o"):
		owner = arg
	elif opt in ("-r"):
		repo = arg
	elif opt in ("-q"):
		query = arg
	elif opt in ("-l"):
		label = arg
userData = "Basic " + (username + ':' + password).encode("base64").rstrip()

total = 0
print 'Search query = ' + query
print 'Search label = ' + label

startDate = date(startYear, startMonth, 1)
endDate = date(endYear, endMonth, 1)
errorCount = 0

while startDate + timedelta(days=1) <= endDate:

	try:

		nextDate = startDate + timedelta(days=1)

		dateRange = str(startDate.year) + '-' + str(startDate.month).zfill(2) +'-' + str(startDate.day).zfill(2) + '..' + str(nextDate.year) + '-' + str(nextDate.month).zfill(2) + '-' + str(nextDate.day).zfill(2)
		url = 'https://api.github.com/search/issues?q=' + query.replace(" ", "+") + '+repo:' + str(owner) + '/' + str(repo) + '+created:' + dateRange

		if label != '':
			url += '+label:' + label
			
		req = urllib2.Request(url)
		req.add_header("Content-type", "application/x-www-form-urlencoded")
		req.add_header('Authorization', userData)
		res = urllib2.urlopen(req)

		p = re.compile('"total_count":(\d*)')

		m = p.search(res.read())
		total += int(m.group(1))
		print dateRange + ' = ' + m.group(1)
		csvCount += str(m.group(1)) + ','
		csvDates += str(dateCounter) + ','
		dateCounter += 1
		
		startDate += timedelta(days=1)
		sys.stdout.flush()
		time.sleep(3)
	except Exception:
		print "error!"
		errorCount += 1
print "Total = " + str(total) + " Error total = " + str(errorCount)

if csvCount[-1:] == ",":
    csvCount = csvCount[:-1]

if csvDates[-1:] == ",":
	csvDates = csvDates[:-1]
		
print "CSV dates = " + str(csvDates)
print "CSV count = " + str(csvCount)
sys.stdout.flush()
