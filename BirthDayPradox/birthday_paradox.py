import math
import random
print " Enter the Random Number\n"
random_number=raw_input()
print "Enter the number of times you want toconduct the trial"
no_of_trials=input()
print "Enter the number of times each date repeates itself"
repeat=int(raw_input())
global universal
universal=[]
def Initialize(d):
    global universal
    i=0
    temp=[]
    while(i<366):
        j=0
        while(j<d):
            temp.append(i)
            j=j+1
        i=i+1
    l=d*366
    i=0
    while(i<l):
        index=int(random.random()*365)
        universal.append(temp[index])
        temp[index]=temp[l-1-i]
        i=i+1

def experiment(random_number):
    global universal
    flag=False
    i=0
    u=[]
    while(i<len(universal)):
        u.append(universal[i])
        i=i+1
    bday=[]
    i=0
    while(i<int(random_number)):
        index=int(random.random()*365)
        bday.append(u[index])
        j=0
        while(j<i):
            if(bday[i]==bday[j]):
                flag=True
            j=j+1
        i=i+1
    print bday
    return flag



def calc(random_number,no_of_trials):
    num_pair=(int(random_number)*(int(random_number)-1))/2
    #print "\tnum_pair\t"
    #print num_pair
    #chance_unique_pair=364/365

    chance_pair=math.pow(0.997260,int(num_pair))
    #print "\tchance_pair\t"
    #print float(chance_pair)
    chance_match=(1-float(chance_pair))
    #print "\tchance_match\t"
    #print chance_match
    sucess=0
    i=0
    while i<no_of_trials:
        if(experiment(random_number)):
            sucess=sucess+1
        i=i+1
    print 'Out of '+str(no_of_trials)+' trials '+str(sucess)+' trials were successful'
    print 'The experimental Probablity is : '+str(sucess*100.0/no_of_trials)+'%'
    return chance_match

Initialize(repeat)
result=calc(int(random_number),no_of_trials)
print "Chances of two persons having birthdays on same day is \t"
print float(result)*100
