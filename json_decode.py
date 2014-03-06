#!/bin/python

import simplejson as json
import collections
from pprint import pprint

json_data = open('correct.json')
data = load(json_data)


pprint(data)

exit()

# data is a big hash(DICTionary) now

e = {} #declaring a new hash

# browsing through the data hash
for key,value in data.iteritems():
	if(key == "e"):
		e = value

# from this point onwards, we are just interested in 'e' block
# now e (declared above in line 12 is a hash, we can access key/value pairs of this hash)

#small test
ecnum = e['ec'] #what is the ec number

vinum = e['vi'] #what is the vi number

print "ec number is : " + str(ecnum)
print "vi id for this ec is : " + str(vinum) 
#now we can just slurp the e hash and when multiple jsons are fed in, 
#lets create a brand new dict to save all the information and variables inside
# the idea is to later on print out the contents saved in this hash into a neat desired output table


ecHash = collections.defaultdict(dict) #declare dict of dict (here the keys would be ec number like 110000)

# when there are mul
for ecnum in ecHash:
    ecHash[ecnum]['count'] += 1 #increment the count to see how many times this ec number was observed
else :
	ecHash[ecnum]['count'] = 1
	ecHash[ecnum]['vi'] = list()
	ecHash[ecnum]['vi'].append(vinum)

pprint(ecHash)

json_data.close()