import csv
import os

from pymongo import MongoClient


data_dir_path = "E:/Data Repo/Taxi-Trajectories/FOIL2013/Trip-Files/";

filenames = os.listdir(data_dir_path);

print("Step 1",filenames )

#for filenames in os.listdir(data_dir_path):
   # print("Processing File = ", filenames)
currentFile = open(data_dir_path+filenames[0], 'r');

print("Step 2",filenames[0] )

currentFileReader = csv.DictReader(currentFile);
    #for row in currentFileReader:
    #print(currentFileReader.fieldnames[0]);
    #print  ("Number of Lines = ",len(currentFile.readlines()));

mongo_client = MongoClient();
db = mongo_client.nyctaxitrips2
db.segment.drop()
header = currentFileReader.fieldnames

print("Step 3",header )

count = 0;
for each in currentFileReader:
    row={}
    for field in header:
        row[field]=each[field]

    db.segment.insert(row)
    count = count+1;

    if count >20:
        break;

print ("DONE!");
