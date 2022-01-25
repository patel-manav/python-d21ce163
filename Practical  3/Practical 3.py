# Input
N = int(input('Enter Size of Each Group: '))
s = map(int, input('Enter Captain Room Number: ').split())
# Sorted Captain Room Number
s = sorted(s)
# Logic & Print Answer
for i in range(len(s)):
    if(i != len(s)-1):
        if(s[i]!=s[i-1] and s[i]!=s[i+1]):
            print(s[i])
            break;
    else:
        print(s[i])
################# Created By Manav Dadhaniya - D21CE163 #####################