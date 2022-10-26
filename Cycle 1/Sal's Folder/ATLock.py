#New ATLock File
import sys
import random
import os.path as os
from datetime import date

lock_type = 3
f1 = " "
f2 = " "
fn1 = " "
fn2 = " "
s = " " 
s1 = " "
s2 = " "
lock_code = " "

i = 0
j = 0
k = 0
lock_pos = 0
lock_dat = 0
this_dat = 0 #All integers

def encode(s):
    i, j, k #All ints
    if(lock_code != " "):
        i = 1
        for i in len(s):
            lock_pos += 1
            if(lock_pos > len(lock_code)):
                lock_pos = 1
            #if(s[i] < " " or s[i] > '~'):  #Not exactly correct but those represent the printable ASCII lowest and highest characters\
            if(ord(s[i]) < 31 or ord(s[i]) > 128):
                s[i] = " "

            this_dat = ord(s[i]) & 15
            #s[i] = s[i] ^ (lock_code[lock_pos] ^ lock_dat) + 1 
            s[i] = chr((ord(s[i]) ^ (ord(lock_code[lock_pos]) ^ lock_dat)) + 1)
            lock_dat = this_dat
        encode = s          
    
def prepare(s, s1):
    i, j, k, l = 0 #Ints
    s2 #string
    if(len(s1) == 0 or s1[1] == ';'):  #Remove comments
        s1 = " "
    else:
        k = 0
        var = 1
        step = -1
        i = len(s1)
        for i in range(i, var, step):
            if(s1[i] == ';'):
                k = i
        if(k > 0):
            s1 = len(s1, k - 1) 
    
    s2 = " "  #Remove excess space
    i = 1
    for i in len(s1):
        if(s1.isspace() == False and s1[i] != ','):  #Condition is not (s1[i] in [' ',#8,#9,#10,','])
            s2 = s2 + s1[i]
        elif(s2 != " "):
            s = s + s2 + " "
            s = " "
    
    if(s2 != " "):
        s = s + s2
    
    prepare = s
    
def write_line(s, s1):
    s = prepare(s, s1)
    if(len(s) > 0):
        s = encode(s)
        f2.write(s)
        #print(f2, s)
    
def main():
    lock_pos = 0
    lock_dat = 0

    if(len(sys.argv) < 1 or len(sys.argv) > 2):  
        f1.write("Usage: ATRLOCK <robot[.at2]> [locked[.atl]]")     #btrim removes white space in front and back of string
    
    f1 = open(fn1, "r")
    f2 = open(fn2, "w")
    
    fn1 = str.strip(str.upper(sys.argv[1]))  
        
    if(fn1 == os.basename(fn1)):   #base_name grabs the part of a file before the .atr portion
        fn1 = fn1 + ".AT2"  
    
    if(fn1 == None):
        print("Robot ", fn1, " not found!")
        exit(0)
    
    if(len(sys.argv) == 2):
        fn2 = str.strip(str.upper(sys.argv[2]))
    else:
        fn2 = os.basename(fn1) + ".ATL"
        
    if(fn2 == os.basename(fn2)):
        fn2 = fn2 + ".ATL"
    
    if(fn2 != False):
        print("Output name ", fn1, " not valid!")
        exit(0)
        
    if(fn1 == fn2):
        print("Filenames cannot be the same!")
        exit(0)
        

    
    #Copying comment header
    
    f2.write(";------------------------------------------------------------------------------")
    s = " "
    
    while s == " " and not f1:
        s = f1.readline()
        s = str.strip(s)       
        if(s[1] == ';'):
            f2.write(s)
            s = " "
            
    #lock header
    today = date.today()
    barePath = os.split(os.basename(fn1))
    f2.write(";------------------------------------------------------------------------------")  
    f2.write('; ', barePath[1], 'Locked on ', today)   #no_path(base_name(fn1)),  #no_path removes path before file name
    f2.write(";------------------------------------------------------------------------------")  
    lock_code = " "
    k = random.randrange(20, 41, 1)
    
    i = 1
    for i in k:
        lock_code = lock_code + chr(random.randrange(65, 97, 1))
    
    f2.write("#Lock", lock_type, " ", lock_code)
    
    #decode lock code
    i = 1
    for i in len(lock_code):
        lock_code[i] = chr(ord(lock_code[i]) - 65)
        
    f2.write("Encoding \"" , fn1, "\"...")
    
    #encode robot
    
    s = str.strip(s)     
    
    if(len(s) > 0):
        write_line(" ", str.upper(s))
    
    while not f1:
        s1 = f1.readline()
        s = " "
        s1 = str.strip(str.upper(s)) 
        write_line(s, s1)
        
    f2.write("Done. Used LOCK Format #", lock_type,".")
    f2.write("Only ATR2 v2.08 or later can decode.")
    f2.write("LOCKed robot saved as \"", fn2, "\"")

    f1.close()
    f2.close()