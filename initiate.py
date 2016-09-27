#! python

#    Affex Asset
#    Importer tool
#    Author_Audun_Ase

import os

###
#    Initiate library.
###

drive = os.path.join('your','path','here','hiplib')
execscript = open(os.path.join(drive, 'aasset.py'))
exec(execscript.read()) 

sys.exit()
