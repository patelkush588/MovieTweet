# coding: utf-8

# In[1]:

import Orange
import string
print "Please enter a genre of movies:"
print "Comedy"
print "Action"
print "Crime"
print "Horror"
print "Drama "
print "Sport"
print "Romance"
print "Documentary"
print "Sci-Fi"
print "Thriller"


var = raw_input("Enter a genre from above: ")

raw_data = ["Comedy, Family, Drama, Romance",
            "Action, Sport, Sci-Fi, Thriller",
            "Romance, Documentary, Horror, Action",
            "Horror, Crime, Romance, Sci-Fi",
            "Thriller, Comedy, Documentary, Drama",
            "Action, Crime, Sport, Romance",
            "Thriller, Sci-Fi, Crime, Action"]

raw_data.append(var)

#print raw_data

# write data to the text file: data.basket
f = open('data.basket', 'w')
for item in raw_data:
    f.write(item + '\n')
f.close()

# Load data from the text file: data.basket
data = Orange.data.Table("data.basket")


# Identify association rules with supports at least 0.3
rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.2)


# print out rules
#print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
#for r in rules[:]:
 #   print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

rule = rules[0]
maximum = 0.1
for idx, d in enumerate(data):
    if idx is 7:
        print '\nYour Entered Choice is {0}'.format(raw_data[idx])
        for r in rules:
            if r.applies_left(d) and not r.applies_right(d):
                if r.confidence > maximum:
                    printing_str = r
                    maximum = r.confidence

string_1= str(printing_str)
print "\n"
print "Following genre is suggested:"
var = string_1.split("->",1)[1]
print var

year=raw_input("Enter Calender Year you want movie suggestions of:")


aline = open('movies.dat.txt', 'r').readlines()
result = []
print "Suggested Movies are:"
for x in aline:
    movie_dat = x.split('::')[2]
    s_movie = movie_dat
    if var[2:] in s_movie:
        movie = x.split('::')[1]
        if year in movie:
            print movie


