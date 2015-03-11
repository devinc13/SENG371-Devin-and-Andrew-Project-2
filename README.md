# SENG371-Devin-and-Andrew-Project-2

##Our Project Question: 
For project two, we want to continue with the idea of examining the effect of progressive changes and anti-regressive changes on the number of reported bugs over time. Therefore, our question will still be:
####"How does the number of progressive and anti-regressive changes effect the number of bugs reported over time?"

##Hypotheses
Our hypotheses are that the more progressive changes there are, the more bugs will be reported in the following weeks, and that the more anti-regressive changes there are, the less bugs will be reported over the next few months.

##Methodology: 
The above hypotheses are what we found in project 1, but our proof and explanation of these were weak, so we want to improve this.
Instead of using our script to get all this information from github, we want to find different ways to obtain the anti-regressive, and make sure it is on a daily basis, instead of monthly. We will still use our script for counting bugs, as it seems quite reliable for that, although we will make sure that the search is limited to include only issues, not pull requests.
For anti-regressive changes, we would like to use the tool Transit that was created by another team. This will allow us to detect both the day of an anti-regressive change, and the size of it.
For features, we would like to still use the python script, but with some advanced searches. For repos without a "feature" label, we'd like to only search merged pull requests, and instead of searching for "feature", we will search for pull requests that don't contain the words bug, rewrite or refactor: "NOT bug AND NOT rewrite AND NOT refactor".

##Codebases/Systems: 
Ruby on Rails (6674 issues - GitHub issue tracker): https://github.com/rails/rails

node.js (5608 issues - GitHub issue tracker): https://github.com/joyent/node 

Bootstrap (10,820 issues - GitHub issue tracker): https://github.com/twbs/bootstrap

##Metrics
	 

##Results:

	
##Analysis

##Project Management Information

#####Milestones: 

Milestone 1 - March 11th: Install transit, try running it on a repo. 

Milestone 2 - March 18th: Modify script to search daily, and use advanced search queries (bug and feature searches)

Milestone 3 - March 25th: Modify/add to transit to be able to get the date and size of each code move.

Milestone 4 - March 30th: Collect Data and record results!

Milestone 5 - Stretch goal: Add auto generating graphs to the project.

#####Roles:








