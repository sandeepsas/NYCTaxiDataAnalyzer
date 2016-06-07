import csv
import os

from pymongo import MongoClient


data_dir_path = "E:/Data Repo/Taxi-Trajectories/FOIL2013/Trip-Files/";

for filenames in os.listdir(data_dir_path):
   # print("Processing File = ", filenames)
    currentFile = open(data_dir_path+filenames, 'r');
    currentFileReader = csv.DictReader(currentFile);
    #for row in currentFileReader:
    print(currentFileReader.fieldnames[0]);
    #print  ("Number of Lines = ",len(currentFile.readlines()));

mongo_client = MongoClient();
