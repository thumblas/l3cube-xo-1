#!/usr/bin/python

import sys,os 

##
#	A "log" will be generated for the given file. 
#	Each time CASE 1 is run a new line is added to the existing log 
#	Log format:
#	1>  When run for the first time           #<line 1 content>#(line 2 content)........
#	2>  When lines are appended		  #<newly addedline 1>#<newly added line 2>.........
#	3>  When line is deleted		  !<line number of deleted line>!<line number of deleted line>........
##

#######################################################################
#	Code to verify which usage case
#		1	python src.py <filename>
#		2	python src.py no	(no is version number)
##
arg_length = len(sys.argv)	
choice = sys.argv[1]
files = os.popen("ls").readlines()
case_par = 0
for i in files:
	if(i[:-1]==choice):
		case_par = 1

if(case_par):			
#######################################################################
# USAGE CASE 1
#	a)	First entry
#	b)	Lines appended
#	c) 	Lines deleted
##



############## CASE 1a - First entry
	log = open("log","a")			
	if(log.tell() == 0):			# Check if 1st entry in log
		##
		#	If first entry fill log with # entries of all lines
		##

		with open(choice) as f:
			content = f.readlines()
		log_line = ""
		for i in content[0:len(content)-1]:
			log_line = log_line+"#"+i[0:len(i)-1]
		log_line = log_line + "#"+content[-1] 
		log.write(log_line)
		log.close()
	
	else:					
		
############## 


		
		with open("log") as f:
			versions = f.readlines()	#Array with each element 
		with open(choice) as f:
			content = f.readlines()		#Array with each element as one line of the
#-------------------------------------------------------------------------------------------
#Code to calculate length from log and compare with actual length and determine if line 
#appended or deleted 
		lengthy = 0
		for i in versions:
			a = i.split('#')
			if(len(a)>1):
				lengthy = lengthy +len(a)-1 
			else:
				lengthy = lengthy -len(i.split('!'))+1


#-------------------------------------------------------------------------------------------



		if(lengthy>len(content)):
		#####
		#	Code for if line deleted
			#------------------------------------------------------------
			#This code creates a file based from logs to compare with current state
			versioned_file = []
			for i in versions:
				a = i.split('#')
				if(len(a)>1):
					for t in a[1:-1]:
						versioned_file.append(t)
					if(i==versions[-1]):
						versioned_file.append(a[-1])
					else:
						versioned_file.append(a[-1][:-1])
				else:
					a = i.split('!')
					if(len(a)>1):
						for t in a[1:]:
							versioned_file[int(t)] = "Blank"
			#------------------------------------------------------------
			new_log_line = "\n"
			next_point = 0
			
			for i in range(len(versioned_file)):
				if(versioned_file[i]=="Blank"):
					print "1"
					continue
				elif(next_point>len(content)-1):
					new_log_line = new_log_line + "!" + str(i)
					print "2"

				elif(next_point==len(content)-1):
					print "3"
					if(versioned_file[i]==content[next_point]):
						continue
					else:
						new_log_line = new_log_line + "!" + str(i)


				elif(versioned_file[i]==content[next_point][:-1]):
					next_point = next_point +1
					print "4"
					continue
				
				else:
					print "5"
					new_log_line = new_log_line + "!" + str(i)

			log.write(new_log_line)
			log.close()

		
		#####
		else:
		#####
		#	Code for if lines appended
		
			lengthy = 0
			for i in versions:
				a = i.split('#')
				if(len(a)>1):
					lengthy = lengthy +len(a)-1 
				else:
					lengthy = lengthy -len(i.split('!'))+1
			
			new_log_line = "\n"
			for i in content[lengthy:-1]:
				new_log_line = new_log_line + "#" + i[0:len(i)-1]
			new_log_line = new_log_line + "#" + content[-1]
			log.write(new_log_line)
			log.close()

		#####

#######################################################################
# USAGE CASE 2
#	
else:												# USAGE CASE 2
	with open("log") as f:
		versions = f.readlines()		
	versions = versions[:int(choice)]			# Read first <i/p parameter> no of lines from log
	versioned_file = []
	for i in versions:
		a = i.split('#')
		if(len(a)>1):
			for t in a[1:-1]:
				versioned_file.append(t)
			if(i==versions[-1]):
				versioned_file.append(a[-1])
			else:
				versioned_file.append(a[-1][:-1])
		else:
			a = i.split('!')
			if(len(a)>1):
				for t in a[1:]:
					versioned_file[int(t)] = "Blank"
	for i in versioned_file:
		if (i != "Blank"):
			print i

