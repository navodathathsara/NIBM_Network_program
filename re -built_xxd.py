from sys import argv

text_list=[]                                                    #define a new list

#file=str(input("xxd "))			                        #input file name
script, file=argv
fo=open(file,"r")						#open the file
textin=fo.read()						#read the file
fo.close()                                                      #close the file


def func(text):                                                         #define a function to get hexadecimal values
        string=""							#define new string variable
        for i in str(text):
                h=str(hex(ord(i)))[2::]				#convert the strings to hexadecimal of ascii 
                if len(h)==1:
                        h="0"+h
                string+=h
        count=0								#define new integer variable
        string2=""							#define new string variable
        for j in str(string):
                count+=1						#counting strings
                string2+=j
                if count%4==0:
                        string2+=" "					#devide string 4 by 4
        return string2

def replace_line(word):                                                 #define a function to replace '\n' to '.'
        new_word=""
        for i in str(word):
                if i=="\n":
                        new_word+="."
                else:
                        new_word+=i
        return new_word

def line(val):                                                          #define a function to display line no
        return "0"*(7-len(str(hex(val))[2::]))+str(hex(val))[2::]+"0"


text=""
count=0
for i in str(textin):
        text+=i
        count+=1
        if count == 16:
                text_list.append(text)
                count=0
                text=""
else:
        text_list.append(text)
        text=""


for i in range(len(text_list)):
        print(line(i),func(text_list[i]),"\t"+str(replace_line(text_list[i])))   #print the final result
