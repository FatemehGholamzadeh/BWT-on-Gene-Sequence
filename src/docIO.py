import csv
import pandas as pd


def read_dna():
    dna = ""
    with open('EcoliGenome.csv') as csvfile:
        read = csv.reader(csvfile, delimiter=',')
        for row in read:
            dna += row[0]
    return dna

def read_l():
    f = open("l.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        return contents


def read_reads():
    reads = []
    sheet = pd.read_csv(r'ReadSet5.1.csv')
    for i in range(len(sheet)):
        if i % 4 == 3:
            print("kk")
            reads.append(Read(sheet.loc[i][0], sheet.loc[i + 1][0]))
    return reads


def write_result(result):
    file1 = open("results.txt", "w")
    file1.write(result)
    file1.write("\n")
    file1.close()


def write_l(l):
    str1 = ''.join(l)
    file1 = open("l.txt", "w")
    file1.write(str1)
    file1.close()


def sort_table():
    file1 = open("myfile.txt", "r+")
    data = file1.readlines()
    data.sort()
    return data


class Read:
    def __init__(self, name, read):
        self.name = name
        self.read = read
        self.address = {}

    def priint(self):
        print("name :")
        print(self.name)
        print("read: ")
        print(self.read)
