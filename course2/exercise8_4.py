fname = input("Enter file name: ")
fh = open(fname)
lst = list()
def sort (list):
    return sorted(list)

for line in fh:
  currentLine = line.rstrip().split()
  for word in currentLine:
    if word in lst:
        continue
    lst.append(word)
sorted = sort(lst)
print(sorted)


# print(sorted)
