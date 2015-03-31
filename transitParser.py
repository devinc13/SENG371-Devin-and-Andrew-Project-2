import json
import sys
import getopt
import datetime
import csv

# How to run this script:
usage = "transitParser.py -f <JSON of transit output in .txt> -a <start date as DD-MM-YYYY> -b <end date as DD-MM-YYYY> -i <yes>\n\
Only include -i flag to count the number of commits per day"

# The minimum number of line moves to be accepted as an actual change.
# Modify this variable as desired.
MinNumLineMove = 5

revwalk = ""
pairings = {}
fileName = ""
intensityMode = ''
intensity = {}


#Parse the arguments passed into this script
try:
	opts, args = getopt.getopt(sys.argv[1:], "f:a:b:i:")
except getopt.GetoptError:
	print usage
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		print "Improper arguments. please invoke script as: " + usage
		sys.exit(2)
	elif opt in ("-f"):
		try:
			fileName = arg
			revwalk = json.loads(open(fileName, 'r').read())
		except IOError as e:
			print "Could not find file " + arg
			sys.exit(2)
	elif opt in ("-i"):
		intensityMode = 'yes'
	elif opt in ("-a"):
		startDate = datetime.datetime.strptime(arg, "%d-%m-%Y")
	elif opt in ("-b"):
		endDate = datetime.datetime.strptime(arg, "%d-%m-%Y")


#Parse 'dat JSON!
for commit in revwalk:
	# Check that transit has output info for this commit
	if commit["outputs"]:
		# Check if the number of moved lines passes our threshold value
		num_lines = commit["outputs"][0]["num_lines"]
		if num_lines >= MinNumLineMove:
			#import timstamp of commit as readable datetime
			commitDate = datetime.datetime.fromtimestamp(int(commit["new_time"]))
			#check if the date falls in the date range
			if commitDate >= startDate and commitDate <= endDate:
				# Add the dateCount + num_lines pairings if it does not exist
				# If it does, add num_lines to the existing entry
				dateCount = (commitDate - startDate).days
				if dateCount in pairings:
					pairings[dateCount] += num_lines
					intensity[dateCount] += 1
				else:
					pairings[dateCount] = num_lines
					intensity[dateCount] = 1

output = {}
totalDays = endDate - startDate

for x in range(0, totalDays.days):
	if x in pairings:
		output[x+1] = pairings[x]
	else:
		output[x+1] = 0

intensityOutput = {}
if intensityMode:
	for x in range(0, totalDays.days):
		if x in intensity:
			intensityOutput[x+1] = intensity[x]
		else:
			intensityOutput[x+1] = 0

keys = output.keys()
with open(fileName + '.csv', 'wb+') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows([output])
    if intensityMode:
    	dict_writer.writerows([intensityOutput])

print "Wrote to file " + fileName + ".csv"
sys.stdout.flush()
