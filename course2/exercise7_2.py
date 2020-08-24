# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    total = float(total) + float(line[19:].lstrip())
#     print(total)
#     print(line[19:].lstrip())
# print(count)

print("Average spam confidence:", float(total/count))
