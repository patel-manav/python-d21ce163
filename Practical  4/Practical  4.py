# Enter Size of Element
n = int(input('Enter Element Size: '))
# Enter Element
a = list(map(int, input('Enter {} Element Separate By Space: '.format(n)).split()))
# Declaration
d = max(a)
i =0
# Logic
for i in range(i,n):
    if d == max(a):
        a.remove(max(a))
# Print Answer
print('Runner Up Number Is: ',max(a))

################# Created By Manav Dadhaniya - D21CE163 #####################