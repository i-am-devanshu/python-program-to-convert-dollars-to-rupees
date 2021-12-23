import re

string = input("Enter The String : ")

match1 = re.findall('[0-9]+(?:\.[0-9]+)?\$',string)  # Regex to find $ 
match2=re.findall('[0-9]+ dollars',string) # Regex to find dollars

if match1 != []:
     for x in range(len(match1)):
          string = string.replace((match1[x][:-1]+"$"),(str(int(match1[x][:-1])*75))+"Rs")

if match2 != []:
     for x in range(len(match2)):
          string = string.replace((match2[x][:-7]+"dollars"),(str(int(match2[x][:-7])*75))+"Rupees")

print(string)
