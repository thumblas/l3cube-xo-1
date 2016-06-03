from Crypto.Cipher import AES
import os

global fileseprator
fileseprator='-----------------------------------------------------------\n'


def enc(key1,key2,content):
	obj = AES.new(key1, AES.MODE_CFB, key2)
	return obj.encrypt(content)

def dec(key1,key2,content):
	obj = AES.new(key1, AES.MODE_CFB, key2)
	return obj.decrypt(content)


dothis=True
def createFile(filename):
	global fileseprator
	if doesExist(filename):
		print 'File of this name already exists'
		return
	f=open("allfiles.txt","a")
	sentinel = ''
	file_content='\n'.join(iter(raw_input, sentinel))
	encfile_content=enc('This is a key123','This is a key456',file_content)
	f.write(filename+":\n"+encfile_content+"\n"+fileseprator)

def copyFile(filepath):
	global fileseprator
	if not os.path.isfile(filepath):
		print "The file does not exist at the given path"
		return
	if os.path.abspath(filepath).split('/')[:-1]==(os.path.abspath(__file__)).split('/')[:-1]:
		print "The to copy from must be from the external file"
		return
	filename=filepath.split('/')[-1]
	if doesExist(filename):
		print 'File of this name already exists'
		return
	f=open("allfiles.txt","a")
	fileToCopy=open(filepath,'r')
	file_content=fileToCopy.read()
	encfile_content=enc('This is a key123','This is a key456',file_content)
	f.write(filename+":\n"+encfile_content+"\n"+fileseprator)

def CopyFile(filepath,filename):
	global fileseprator
	if not os.path.isfile(filepath):
		print "The file does not exist at the given path"
		return
	if os.path.abspath(filepath).split('/')[:-1]==(os.path.abspath(__file__)).split('/')[:-1]:
		print "The to copy from must be from the external file"
		return
	f=open("allfiles.txt","a")
	fileToCopy=open(filepath,'r')
	file_content=fileToCopy.read()
	encfile_content=enc('This is a key123','This is a key456',file_content)
	f.write(filename+":\n"+encfile_content+"\n"+fileseprator)

def printFile(filename):
	global fileseprator
	f=open("allfiles.txt",'r')
	file_content=f.read()
	d=file_content.split("\n"+fileseprator)
	for fil in d:
		if fil.split(':\n')[0]==filename:
			print dec('This is a key123','This is a key456',fil.split(':\n')[1])
			return
	print 'File not Found'

def deleteFile(filename):
	global fileseprator
	f=open("allfiles.txt",'r')
	file_content=f.read()
	d=file_content.split("\n"+fileseprator)
	i=0
	newFile=""
	for fil in d:
		if fil.split(':\n')[0]==filename:
			j=0
			while(j<len(d)-1):
				if(j!=i):
					newFile=newFile+d[j]+"\n"+fileseprator
				j=j+1
			fw=open("allfiles.txt",'w')
			fw.write(newFile)
			print 'File Delted'
			return
		i=i+1
	print 'File not Found'

def ls():
	f=open("allfiles.txt",'r')
	file_content=f.read()
	d=file_content.split("\n"+fileseprator)
	for fil in d:
		print (fil.split(':\n')[0])

def doesExist(filename):
	f=open("allfiles.txt",'r')
	file_content=f.read()
	d=file_content.split("\n"+fileseprator)
	for fil in d:
		if fil.split(':\n')[0]==filename:
			return True
	return False

while(dothis):
	command = raw_input(">")
	args = command.split(" ")
	if(args[0]=="create"):
		if(len(args)==2):
			createFile(args[1])	
		else:
			print "usage : create <filename>"
	elif(args[0]=="copy"):
		if(len(args)==2):
			copyFile(args[1])
		elif(len(args)==3):
			CopyFile(args[1],args[2])
		else:
			print "usage : copy <path_to_the_file>\nusage : copy <path_to_external_files> <name_of_internal_file>"
	elif(args[0]=="print"):
		if(len(args)==2):
			printFile(args[1])
		else:
			print "usage : print <filename>"
	elif(args[0]=="delete"):
		if(len(args)==2):
			deleteFile(args[1])
		else:
			print "usage : delete <filename>"
	elif(args[0]=="ls"):
		if(len(args)==1):
			ls()
		else:
			print 'usage : ls'