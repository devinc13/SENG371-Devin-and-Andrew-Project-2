# SENG371-Devin-and-Andrew-Project-2

##Our Project Question: 
For project two, we want to continue with the idea of examining the effect of progressive changes and anti-regressive changes on the number of reported bugs over time. Therefore, our question will still be:
####"How does the number of progressive and anti-regressive changes effect the number of bugs reported over time?"

##Hypotheses:
Our hypotheses are that the more progressive changes there are, the more bugs will be reported in the following weeks, and that the more anti-regressive changes there are, the less bugs will be reported over the next few months. That is, that increases in bugs will be the result of progrssive changes and decreases the result of anti-regressive changes.

##Methodology: 
The above hypotheses are what we found in project 1, but our proof and explanation of these were weak, so we want to improve this. Some of our issues were that the data wasn't precise enough, due to our monthly searches, and that we had difficulty detecting anti-regressive changes. These are what we want to improve upon in this project!
The overall idea will still be to search the dates and amount of progressive (features), anti-regressive (refactoring) and bugs, and plot these to find the relations between them.
Instead of only using our script to get all this information from github, we want to find different ways to obtain the anti-regressive, and make sure it is on a daily basis, instead of monthly. We will still use our script for counting bugs, as it seems quite reliable for that, although we will make sure that the search is limited to include only issues, not pull requests.
For anti-regressive changes, we would like to use the tool Transit that was created by another team. This will allow us to detect both the day of an anti-regressive change, and the size of it.
For features, we would like to still use the python script, but with some advanced searches. For repos without a "feature" label, we'd like to only search merged pull requests, and instead of searching for "feature", we will search for pull requests that don't contain the words bug, rewrite or refactor: "NOT bug AND NOT rewrite AND NOT refactor".
Once we have gathered this data (the number of bugs, anti-regressive changes and progressive changes on each day of the project), we will create a graph for each repo, and use these to figure out how the anti-regressive and progressive changes effect the number of bugs, and also look for any other interesting correlations.
Using the data, we also imported it into R, and calculated the correlation and covariance between progressive changes and bugs, and between anti-regressive changes and bugs.
After examining the correlations and covariance values from the original data, we realized this was checking the correlation and covariances between bugs and progressive/anti-regressive changes on the same days, but not checking things like how a feature would effect the number of bugs in the following days or weeks.
To solve this oversight, some research was done, and we found that you can calculate cross correlations in R, which show the correlation with lag intervals added (in our case, daily lag).
This allows us to see how features and anti-regressive changes correlated with the number of reported bugs throughout the following 28-30 days.

##Codebases/Systems: 
Ruby on Rails (6674 issues - GitHub issue tracker): https://github.com/rails/rails

Node.js (5608 issues - GitHub issue tracker): https://github.com/joyent/node 

Bootstrap (10,820 issues - GitHub issue tracker): https://github.com/twbs/bootstrap

##Metrics
Anti-regressive changes were all detected by using Transit on each repository. Progressive changes were done slightly differently on each repository, due to differences in labelling.
####Ruby on Rails
We analysed Rails between April 2011 and February 2015. Bugs were found by searching issues by the keyword "bug". Progressive changes were found by searching merged pull requests with the search "NOT bug AND NOT rewrite AND NOT refactor AND NOT fix AND NOT remove".

####Node
We analysed Node between August 2011 and February 2015. Bugs were found by searching issues by the keyword "bug". Progressive changes were found by searching merged pull requests with the search "NOT bug AND NOT rewrite AND NOT refactor AND NOT fix AND NOT remove".

####Bootstrap
We analysed Bootstrap between June 2009 and February 2015. Bugs were found by searching issues by the label "confirmed". Progressive changes were found by searching merged pull requests that had the label "feature".

##How to run the project!

####Progressive Changes and Bugs
To gather the csv data on Progressive changes and Bugs on the 3 repositories, you can run the script consecutively 6 times, writing text files with the output by running the following command:

python bugCounterDaily.py -u <githubUsername> -p <githubPassword> -a 2011 -b 4 -c 2015 -d 2 -o rails -r rails -q 'is:issue bug' 2>&1 | tee railsBugs.txt && python bugCounterDaily.py -u <githubUsername> -p <githubPassword> -a 2011 -b 4 -c 2015 -d 2 -o rails -r rails -q 'is:pr is:merged NOT bug AND NOT rewrite AND NOT refactor AND NOT fix AND NOT remove' 2>&1 | tee railsFeatures.txt && python bugCounterDaily.py -u <githubUsername> -p <githubPassword> -a 2011 -b 8 -c 2015 -d 2 -o twbs -r bootstrap -q 'is:issue' -l confirmed 2>&1 | tee bootstrapBugs.txt && python bugCounterDaily.py -u <githubUsername> -p <githubPassword> -a 2011 -b 8 -c 2015 -d 2 -o twbs -r bootstrap -q 'is:pr is:merged' -l feature 2>&1 | tee bootstrapFeatures.txt && python bugCounterDaily.py -u <githubUsername> -p <githubPassword> -a 2009 -b 6 -c 2015 -d 2 -o joyent -r node -q 'is:issue bug' 2>&1 | tee nodeBugs.txt && python bugCounterDaily.py -u <githubUsername> -p <githubPassword> -a 2009 -b 6 -c 2015 -d 2 -o joyent -r node -q 'is:pr is:merged NOT bug AND NOT rewrite AND NOT refactor AND NOT fix AND NOT remove' 2>&1 | tee nodeFeatures.txt

##### *** WARNING *** 
Due to the number of network calls being made to Github's API, and their rate limiting, running the script as shown above will take a LONG time. Like over 12 hours, so be prepared!

####Anti-Regressive Changes


##Results:
(Graphs are really hard to see, you need to click on them to open them, and zoom wayyyyyyy in.)
Rails:
![Scaled Rails Chart](/Graphs/Scaled Graphs/Rails chart scaled.png?raw=true)
Bootstrap:
![Scaled Bootstrap Chart](/Graphs/Scaled Graphs/Bootstrap chart scaled.png?raw=true)
Node:
![Scaled Node Chart](/Graphs/Scaled Graphs/Node chart scaled.png?raw=true)

####Cross Correlation Graphs
(These graphs are plotting the correlation of either progressive or anti-regressive changes vs bugs, and plotting the correlation lag in daily increments. For example, for features at day 14, positive correlation means that the more features there are, the more bugs there are 14 days later, and negative correlation would mean that the more features there are, the less bugs there are 14 days later.)

![](/Graphs/CrossCorrelationCharts/RailsFeaturesVsBugsCrossCorrelation.jpg?raw=true)
![](/Graphs/CrossCorrelationCharts/RailsAnti-regressiveVsBugsCrossCorrelation.jpg?raw=true)
![](/Graphs/CrossCorrelationCharts/BootstrapFeaturesVsBugsCrossCorrelation.jpg?raw=true)
![](/Graphs/CrossCorrelationCharts/BootstrapAnti-regressiveVsBugsCrossCorrelation.jpg?raw=true)
![](/Graphs/CrossCorrelationCharts/NodeFeaturesVsBugsCrossCorrelation.jpg?raw=true)
![](/Graphs/CrossCorrelationCharts/NodeAnti-regressiveVsBugsCrossCorrelation.jpg?raw=true)

##Analysis:
Our original plan of studying the more detailed daily graphs didn't work out, as the graphs are so massive, it is extremely difficult to pull any meaningful conclusions. Instead, we used R to calculate the cross correlations to help prove or disprove our hypothesis. The cross correlation shifts the data by daily increments (lag), and calculates the correlation at each shift. This data was graphed manually, resulting in the above Cross Correlation graphs.
Taking a look at the Cross Correlation graphs shows us the following:
####Rails:
For Rails, we can see that a progressive change (feature) resulted in more bugs during the first 14 days following the feature, but after that it isn't consistent, either slightly increasing or decreasing the number of bugs. The anti-regressive changes in Rails seem to decrease the number of bugs in the first two weeks, but increase the number of bugs in the 3rd and 4th weeks afterwards.
 
####Bootstrap:
Bootstrap's Cross Correlation graph is very clear that progressive changes result in more bugs in the following 28 days. Anti-regressive changes, on the other hand, seem to slightly decrease the number of bugs in the first couple of weeks, but increase the number of bugs in the following weeks.

####Node:
Progressive changes in node almost always result in an increase of bugs in the following 4 weeks. Anti-regressive changes also often result in an increase of bugs, although there were a few lags that did result in a decrease in the number of bugs, mainly in the first week and a half.

####So what does all this mean?
Overall, from the data we collected and the Cross Correlation graphs made from it, it seems that progressive changes increase the number of bugs in the 28-30 days after the change. Anti-regressive changes aren't quite as clear, but they do seem to decrease the number of bugs in the first 2 weeks following the refactor, but then increase the number of bugs in the 3rd and 4th following weeks. One possible reason for this increase in the 3rd and 4th weeks might be due to the fact that the refactoring decreases familiarity with the codebase, causing developers to make mistakes because of that.

##Threats to Validity:
-Only examining 3 repositories doesn't give us enough data to have confidence in our results.

-Our data for anti-regressive changes (from Transit) is very bursty, with lots of days with no anti-regressive changes, followed by ones with a value of 1000, since we were counting the number of lines moved.

-Increasing our granularity to a daily basis may have been too specific, resulting in messier data. Maybe a weekly compromise would be better.

##Future Work:
The following tasks would be interesting to pursue in the future:

-Running the R analysis on the data to generate the cross correlation data on larger ranges (it currently only lags the data by a month) could give us insight into longer term effects of progressive and anti-regressive changes.

-Automating more of the process

-Examining more repositories

-Exploring different ways of collecting data for anti-regressive and progressive changes

-Consider looking at the data on a weekly basis, instead of daily.

##Project Management Information:

#####Milestones: 

Milestone 1 - March 11th: Install transit, try running it on a repo. 

Milestone 2 - March 18th: Modify script to search daily, and use advanced search queries (bug and feature searches)

Milestone 3 - March 25th: Modify/add to transit to be able to get the date and size of each code move.

Milestone 4 - March 30th: Collect Data and record results!

Milestone 5 - Stretch goal: Add auto generating graphs to the project. **Since original graphs proved to be huge and messy and hard to read, this was omitted.

Milestone 6 - No date, added later: Import data into R, perform statistical analysis, and create cross correlation graphs.

#####Roles:

Andrew - In charge of getting results from transit, parsing them to match our other data, and attempting to automate some of this with bash scripts.

Devin - In charge of updating the python script and doing R stuff.

#####Project Burndown Chart:
(This does not include Milestone 6, as it wasn't originally part of the plan)
![Burndown Chart](/Graphs/Burndown Chart.png?raw=true "Burndown Chart")
## Link to Project Video:












