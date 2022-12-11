import csv

def distWordToWord(word1,word2):
    



csv_header = ['ID','Word1','Word2','Word3']
fileDirectory = "testFIle.csv"
dictIDKeyword = {}
num = 0
with open(fileDirectory) as dictFile :
    for row in csv.DictReader(dictFile,csv_header):
        print(row)
        dictIDKeyword[num] = row
        num += 1
