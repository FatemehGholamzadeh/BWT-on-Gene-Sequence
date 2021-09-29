import pandas as pd

from BWT import BWT
from docIO import read_dna, read_reads, Read, write_result

dna = read_dna()
bwt = BWT(dna)
sheet = pd.read_csv(r'ReadSet5.1.csv')
counter = 0
n = 0
print(len(sheet) / 4)
result = ""
for i in range(len(sheet)):
    n += 1
    r = Read(sheet.loc[i * 4 + 3][0], sheet.loc[i * 4 + 4][0])
    ad = bwt.backward_search(r.read)
    r.address = ad
    print(n)
    if r.address is not None:
        result += r.name + " @ " + str(r.address)+"\n"
        counter += 1
percentage = counter * 100 / n
result += "percentage : " + str(percentage)
print(result)
write_result(result)
