# Get structures from Materials Project database(the MAPI_KEY has been set:http://pymatgen.org/usage.html#setting-the-mapi-key-environment-variable ).
# One should input the elements like this: C Ca-O
from pymatgen.matproj.rest import *
import re

elem = raw_input("Elements:").split(' ')
api = MPRester()
struct = []
for s in elem:
	struct.extend(api.get_structures(s))

f = open("POSCARS", 'w')
for i in struct:
	f.write(re.sub(r'(\d) \D+\n', "\\1\n", i.to(fmt="poscar")))

f.close

