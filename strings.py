date = "11/12/2013"

# Go through the string and split
# where there is a '/'
date_manip = date.split('/')

#show the outcome
print ('Month: ' + date_manip[0] +
       '. Day: ' + date_manip[1] +
       '. Year: ' + date_manip[2])

