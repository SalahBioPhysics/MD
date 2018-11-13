#!/usr/bin/python
import sys
import os
import re
import time
import datetime
import subprocess
import os.path
import tempfile
from tempfile import mkstemp
from shutil import move
from os import remove, close
from subprocess import call
import math

# This code calculates the distances between the atoms in all of the chains

def non_bonded_interactions(v1,v2):
	distance_v1v2 = math.sqrt( (v2[0]-v1[0])**2 + (v2[1]-v1[1])**2 + (v2[2]-v1[2])**2 )
	return distance_v1v2


def main(distance):
	pdb_1 = "/Users/salah_salah/Dropbox/myGithub/MD/ryr1/frame_01/B.pdb"
	pdb_2 = "/Users/salah_salah/Dropbox/myGithub/MD/ryr1/frame_01/A.pdb"
	lines_1 = open(pdb_1).readlines()
	lines_2 = open(pdb_2).readlines()
	x_1 = 0.0
	y_1 = 0.0
	z_1 = 0.0
	x_2 = 0.0
	y_2 = 0.0
	z_2 = 0.0
	with open("/Users/salah_salah/Dropbox/myGithub/MD/ryr1/frame_01/distances.txt",'w') as fp1:
		for everyline_1 in lines_1:
			for everyline_2 in lines_2:
				fields_1 = everyline_1.split()
				fields_2 = everyline_2.split()
				
				if len(fields_1) == 11:
					x_1 = float(fields_1[6])
					y_1 = float(fields_1[7])
					z_1 = float(fields_1[8])
				elif len(fields_1) == 10:
					x_1 = float(fields_1[5])
					y_1 = float(fields_1[6])
					z_1 = float(fields_1[7])
				if len(fields_2) == 11:
					x_2 = float(fields_2[6])
					y_2 = float(fields_2[7])
					z_2 = float(fields_2[8])
				elif len(fields_2) == 10:
					x_2 = float(fields_2[5])
					y_2 = float(fields_2[6])
					z_2 = float(fields_2[7])
				v1 = [x_1,y_1,z_1]
				v2 = [x_2,y_2,z_2]
				if fields_1[2] == 'CA' and fields_2[2] == 'CA':
					distance_v1v2 = non_bonded_interactions(v1,v2)
					if distance_v1v2 < float(distance): 
						if len(fields_1) == 11:
							fp1.write("The distance between res B" + fields_1[5] + " and res A" +fields_2[5]+ " in chain A is "+ str(distance_v1v2)+'\n')
						if len(fields_1) == 10:
							fp1.write("The distance between res B" + fields_1[4] + " and res A" +fields_2[5]+ " in chain A is "+ str(distance_v1v2)+'\n')
		fp1.close()



	


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("Specify an input\nFor example 01 (stands for frame_01)")
        sys.exit()
    distance = sys.argv[1]
     
     
    main(distance)