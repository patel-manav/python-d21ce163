# Define Function
def swap_case(s):
    # Delcare Variable
    x = ""
    # Logic
    for y in s:
        if y.isupper() == True:
            x += (y.lower())
        else:
            x += (y.upper())
    return x

# Enter & Print Value Also Call swap_case function
if __name__ == '__main__':
    s = input()
    print(swap_case(s))
################# Created By Manav Dadhaniya - D21CE163 #####################