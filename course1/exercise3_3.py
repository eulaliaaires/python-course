score = input("Enter Score: ")
try:
    src = float(score)
except:
    print('Error: enter a valid score')
    quit()
if((src >= 0.0) & (src <= 1.0)):
    if(src >= 0.9):
        print('A')
    elif(src >= 0.8):
        print('B')
    elif(src >= 0.7):
        print('C')
    elif(src >= 0.6):
        print('D')
    else:
        print('F')
else:
    print('Error: score out of range')
