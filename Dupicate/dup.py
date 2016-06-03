import os
import hashlib
import fnmatch
import getpass

#RUN using Sudo Permissions

global foldername
files=[]
duplicates=[]
d_size={}
def getfiles(foldername):
    for i in os.listdir(foldername):
        itempath=os.path.join(foldername,i)
        if os.path.isfile(itempath):
            #print "Directory\t"+foldername+"\ttraversing\t\n"
            files.append(itempath)
        elif os.path.isdir(itempath):
            getfiles(itempath)
        #print files
    return 0

def comp_size():
    for f in files:
        for k in files:
            if f==k:
                break
            else:
                if os.path.getsize(f) == os.path.getsize(k):
                    #duplicates.append
                    #d_size[f]=k
                    d_size.__setitem__(f,k)
    return 0

def get_md5(filename):
    md5 = hashlib.md5()
    with open(filename,'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            md5.update(chunk)
    return md5.digest()

fileToBeDeleted=[]

def comp_md5():
    for f1 in files:
        for k1 in files:
            if f1==k1:
                break
            else:
                if get_md5(f1)==get_md5(k1):
                    print "Files\t"+f1+"\tand\t"+k1+"\tare equal\t\n"
		    fileToBeDeleted.append(f1)
    for a in fileToBeDeleted:
	os.system('rm '+a)
    return 0

def fcount(path):
  count = 0
  print 'List of Hard Disks Attached'
  print 'home'
  for f in os.listdir(path):
    child = os.path.join(path, f)
    if os.path.isdir(child):
      count += count + 1 # unless include self
      print f
  return count

#lists all paritions on hard disk , here user is username
user=getpass.getuser()
path = "/media/"+user
count=fcount(path)
try:
	path_file=raw_input()
	if(path_file=='home'):
	  print "Scanning /home/user"
	  getfiles('/home/'+user)
	else:
	  getfiles(path+'/'+path_file)
except OSError:
	pass
	

comp_size()
comp_md5()

