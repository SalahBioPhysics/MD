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
from subprocess import call # This is needed to submit jobs

"""
Description
-----------
The code should run vmd and namd MARTINI Residue-Based Coarse-Grain molecular dynamics
 
 
"""

def step1(frame_number):
	# This function copys the original PDB to the working dir 
	# and replace all the UNK residues with ALA.
	print ("Step 1:\tReplacing all the UNK residues with ALA and safe the output to "+str(frame_number))
	sys_call = 'cp /home/salah/MD/martini_md/ryr1/all_frames/'+str(frame_number)+'_5t9r_refined_morphing_real_space_refined.pdb .'
	os.system(sys_call)
	sys_call = 'cp ' + str(frame_number)+'_5t9r_refined_morphing_real_space_refined.pdb '+str(frame_number)+'.pdb'
	os.system(sys_call)
	sys_call = "sed -i -e 's/UNK/ALA/g' "+str(frame_number)+".pdb"
	subprocess.call([sys_call], shell=True)
	print ("Done")

def step2(frame_number):
	# using VMD to construct an all-atom PDB/PSF file pair for the protein
	print ("Step 2:\tConstruct an all-atom PDB/PSF")

	# change input/output file names in step2.tcl
	code_name = "/data1/salah/MD/martini_md/ryr1/bin/step2.tcl"
	first_line = "mol load pdb "+ str(frame_number)+".pdb"
	
	sys_call = "sed -i '1d' "+" "+code_name
	os.system(sys_call)
	sys_call = "sed  -i '1i "+first_line+"\'" + " " +code_name
	os.system(sys_call)
	sys_call = "vmd -dispdev text -e "+code_name+" > step2.log" # run VMD
	os.system(sys_call)
	print ("Done")
	
def step3(frame_number):
	# combine protein with lipids
	print ("Step 3:\tCombine protein with lipids")
	code_file = "/data1/salah/MD/martini_md/ryr1/bin/step3.tcl"
	sys_call = "vmd -dispdev text -e "+code_file+" > step3.log" # run VMD
	os.system(sys_call)
	print ("Done")

 
def step4(frame_number):
	# coarse-grain the system
	print ("Step 4:\tCoarse-grain the system")
	code_file = "/data1/salah/MD/martini_md/ryr1/bin/step4.tcl"
	sys_call = "vmd -dispdev text -e "+code_file+" > step4.log" # run VMD
	os.system(sys_call)
	print ("Done")

def step5(frame_number):
	# Creating a preliminary PSF for the CG system
	print ("Step 5:\tCreating a preliminary PSF for the CG system")
	code_file = "/data1/salah/MD/martini_md/ryr1/bin/step5.tcl"
	sys_call = "vmd -dispdev text -e "+code_file+" > step5.log" # run VMD
	os.system(sys_call)
	print ("Done")

def step6(frame_number):
	# Since this system contains both lipid and protein segments, we will need to correct
	# the psf file to account for secondary structure
	print ("Step 6:\tCorrect the psf file to account for secondary structure")
	code_file = "/data1/salah/MD/martini_md/ryr1/bin/step6.tcl"
	sys_call = "vmd -dispdev text -e "+code_file+" > step6.log" # run VMD
	os.system(sys_call)
	print ("Done")

def step7(frame_number):
	# solvate the system
	print ("Step 7:\tSolvate the system")
	code_file = "/data1/salah/MD/martini_md/ryr1/bin/step7.tcl"
	sys_call = "vmd -dispdev text -e "+code_file+" > step7.log" # run VMD
	os.system(sys_call)
	print ("Done")

def step8(frame_number):
	# Ionize the system
	print ("Step 8:\tIonize the system")
	code_file = "/data1/salah/MD/martini_md/ryr1/bin/step8.tcl"
	sys_call = "vmd -dispdev text -e "+code_file+" > step8.log" # run VMD
	os.system(sys_call)
	print ("Done")

def step9(frame_number):
	# solvate the system. Let the lipids relax around the protein 
	print ("Step 9:\tAdding constraints to the system. Let the lipids relax around the protein")
	code_file = "/data1/salah/MD/martini_md/ryr1/bin/step9.tcl"
	sys_call = "vmd -dispdev text -e "+code_file+" > step9.log" # run VMD
	os.system(sys_call)
	print ("Done")

def step10(frame_number):
	# since our protein contains several non-covalently-bonded segments, 
	# we must use NAMD’s extrabonds feature to keep the protein from falling apart 
	print ("Step 10:\tKeep the protein from falling apart.  Adding non-covalently-bonded segments")
	code_file = "/data1/salah/MD/martini_md/ryr1/bin/step10.tcl"
	sys_call = "vmd -dispdev text -e "+code_file+" > step10.log" # run VMD
	os.system(sys_call)
	print ("Done")


 
def main(frame_number): 
    #step1(frame_number)
    #step2(frame_number)
    #step3(frame_number)
    #step4(frame_number)
    #step5(frame_number)
    #step6(frame_number)
    #step7(frame_number)
    #step8(frame_number)
    #step9(frame_number)
    step10(frame_number)
 
 
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("Specify an input\nFor example 01 (stands for frame_01)")
        sys.exit()
    frame_number = sys.argv[1]
     
     
    main(frame_number)

