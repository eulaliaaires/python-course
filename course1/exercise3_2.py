hours = input('Enter hours:')
rate = input('Enter rate:')
try:
    h = float(hours)
    r = float(rate)
    if h < 40:
        pay = h * r
    else:
        diff = h-40
        pay = (h-diff) * r + diff * 1.5 * r
    print(pay)
except:
    print('Enter a valid number')

# alternatively

# hours = input('Enter hours:')
# rate = input('Enter rate:')
# try:
#     h = float(hours)
#     r = float(rate)
# except:
#     print('Enter a valid number')
#     quit()
# if h < 40:
#     pay = h * r
# else:
#     diff = h-40
#     pay = (h-diff) * r + diff * 1.5 * r
# print(pay)
