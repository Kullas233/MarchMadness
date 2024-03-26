import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Regex Cheat sheet : https://www.dataquest.io/blog/regex-cheatsheet/
# Regex python tester : https://pythex.org/
# re doc : https://docs.python.org/3/library/re.html

possteams = []
with open("PPRG.txt", "r") as txt_file:
   lines = txt_file.readlines()
reg = r'<td class="text-left nowrap" data-sort="[A-z\s\.&\-\(\)\;]*">' #the group of char a to c
string = ""
for line in lines:
    string+=line
    #   print(line)
regs = re.findall(reg,string)
for reg in regs:
    possteams.append(reg[40:-2])
# if re.match(reg, line): #Check if regex is correct
#     print(line)
    
    
reg = r'<td class="text-right" data-sort="\d*\.*\d*">' #the group of char a to c
poss = []
regs = re.findall(reg,string)
count = 0
for reg in regs:
    if count % 6 == 0:
        poss.append(reg[34:-2])
    count+=1

rebteams = []
with open("rebounds.txt", "r") as txt_file:
   lines = txt_file.readlines()
reg = r'<td><.*"><.*class="school">[A-z\s\.&\-\(\)\;\']*</a>' #the group of char a to c
string = ""
for line in lines:
    string+=line
    #   print(line)
regs = re.findall(reg,string)
for reg in regs:
    rebteams.append(reg[reg.index('"school"')+9:-4])

reg = r'<td>.*</td>' #the group of char a to c
rebs = []
regs = re.findall(reg,string)
count = 0
for reg in regs:
    if(count % 8 == 4 or count % 8 == 6):
        rebs.append(reg[4:-5])
    count+=1










# for x in range(len(poss)):
#     print(possteams[x]+",", poss[x])

for x in range(len(rebteams)):
    print(rebteams[x]+",", rebs[x*2], rebs[x*2+1])

# for x in range(len(rebteams)):
#     max = 0
#     match = ""
#     # print(rebteams[x])
#     for y in range(len(possteams)):
#         tmp = fuzz.ratio(rebteams[x], possteams[y])
#         if tmp > max:
#             max = tmp
#             match = possteams[y]
#     if(max < 70):
#         print(max, match)