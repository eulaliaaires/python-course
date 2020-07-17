
def computepay(h,r):
    if h < 40:
        pay = h * r
    else:
        diff = h-40
        pay = (h-diff) * r + diff * 1.5 * r
    return pay
hours = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hours)
    r = float(rate)
except:
    print('Error: Enter a valid number')
    quit()

p = computepay(h,r)
print("Pay",p)
