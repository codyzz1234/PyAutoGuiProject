import pyautogui
import os
import glob
from PIL import ImageGrab
from time import sleep
import time 
from datetime import datetime
import subprocess
import pandas as pd
import numpy as np
import webbrowser


def read():
    df = pd.read_excel('rostering.xlsx', header=None)
    for col in df.columns:
        print("Column is " , col)
    #df.items()

    #How many times the loop will iterate/how many rows exist
    rows = df.shape[0]
    print("No of rows: " + str(rows))

    #How many rows exist
    cols = df.shape[1]
    print("No of colsumns: " + str(cols))
    print("################" + "\n")

    #Print each row
    #for cols_name, data in df.items():
        #print("cols_name",cols_name, "\ndata",data)

    #Print each row 
    #for cols_name, data in df.items():
        #print(cols_name, data[0])
    #for cols_name, data in df.items():
        #print("cols_name",cols_name, "\ndata",data[1]

    #Testing
    #for i in df:
        #yes = df.values[0]
        #print(yes)

    #Idk what is this
    #list(df.itertuples(index=False, name='Event'))
    #for p in df.itertuples(index=False, name='Event'):
        #print(p._1)

    #breakthrough? apparently not lol
    #yes = pd.read_excel('rostering.xlsx', header=None, usecolss=[0])
    #no = yes.to_string(index=False, header=None)
    #print(no)

    #BREAKTHROUGH!!!
    #print(df.iloc[1,0])#.to_string(index=False, header=None))

    #DATE	CHAR	S.NAME	CHAR	LOCATION	C.NAME	SPECIAL CHARACTER	URL	SPECIAL CHARACTER	TYPE

    #noOfValues = cols*row
    #print(noOfValues)

    listOfValues = []
    columnA = []
    columnB = []
    columnC = []
    columnD = []
    columnE = []
    columnF = []
    columnG = []
    columnH = []
    count = 0
    for x in range(rows):	
        if x == rows:
            break
        for y in range(cols):
            rowOfValues = df.iloc[x,y]
            listOfValues.append(rowOfValues)
            columnA.append(df.iloc[x,y])
            columnB.append(df.iloc[x,y+1])
            columnC.append(df.iloc[x,y+2])
            columnD.append(df.iloc[x,y+3])
            columnE.append(df.iloc[x,y+4])
            columnF.append(df.iloc[x,y+5])
            columnG.append(df.iloc[x,y+6])
            columnH.append(df.iloc[x,y+7])
            print("Row of values is ", rowOfValues)
            break;
        count = count + 1
        #print(str(listOfValues) + "\n")
        #print("################" + "\n")
    
    valuesToUse = {
        "columnA": columnA,
        "columnB": columnB,
        "columnC": columnC,
        "columnD": columnD,
        "columnE": columnE,
        "columnF": columnF,
        "columnG": columnG,
        "columnH": columnH
    }
    
    print("Count is ",count)
    #for i in range(len(listOfValues)):
        #print(listOfValues)

    print(str(listOfValues) + "\n")

    for pos, value in enumerate(listOfValues):
        print(pos,value)

    for pos, value in enumerate(listOfValues):
        if pos == 40:
            print(value + " XXX")
    

    #while i < (str(rows)):
        #print(str(listOfValues[8:15]) + "\n")
        #i += 1
    print("Column A", valuesToUse["columnA"])
    print("Column B", valuesToUse["columnB"])
    print("Column C", valuesToUse["columnC"])
    print("Column D", valuesToUse["columnD"])
    print("Column E", valuesToUse["columnE"])
    print("Column F", valuesToUse["columnF"])
    print("Column G", valuesToUse["columnG"])
    print("Column H", valuesToUse["columnH"])

    # Access List in Dictionary.
    assigned = valuesToUse["columnA"]
    print("Assigned is " ,assigned)

    #Loop through list
    for i in assigned:
        print("i is " + i)
        
    #Get list length, a.k.a number of rows/loops
    print("List length is ",len(assigned))
    return valuesToUse


def launchBrowserAndEnterStudio():
    fireImgX,fireImgY = pyautogui.locateCenterOnScreen(r"C:\Users\kenle\Desktop\PyAutoGUI\PyAutoGUI\Images\firefox.png")
    pyautogui.click(fireImgX,fireImgY)
    time.sleep(3)
    pyautogui.write('youtube.com')
    pyautogui.press('enter')
   

def pyAutoGui(valuesToUse):
    launchBrowserAndEnterStudio();
    print("he")


def main():
    valuesToUse = read();
    pyAutoGui(valuesToUse)
    
main();
