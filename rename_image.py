import csv
import os

with open( "saved_tweets.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        ids = row[0]
        text = row[1]
        #print(ids)


        path = 'D:\Twitter\image'
        for file in os.listdir(path):
            print(ids)
            #new_name = file.replace(file,ids + '.jpg')
            #os.rename(os.path.join(path,file),os.path.join(path,new_n