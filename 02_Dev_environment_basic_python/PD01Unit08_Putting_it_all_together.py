# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:46:23 2020

@author: msmorris
"""

# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

datadir = ""
datafile = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        # read first line load into header for keys we will use later
        header = f.readline().split(",")
        # controller so we can break out of loop at certain point
        counter = 0 
        for line in f:
            if counter == 10:
                break
            fields = line.split(",")
            # initialize empty dictionary that will use following loop
            entry = {}
            # construction of dictionary
            for k, value in enumerate(fields):
                # strip removes any extra white space
                entry[header[k].strip()] = value.strip()
            data.append(entry)
            counter +=1
    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline
test()

### CSV module
'''
take a look at the data in excel specifically lines 10 through 20 1 record
is a problem record can you find which one, remember we are talking about parsing
right now. 
'''
'''
import csv handles a lot of issues you can find in a csv file such as , that
might be needed or ways to clean or isolate , like ' and " that might be needed
'''

DictReader - 
assumes you want to read your data into dictionaries
assumes first row is a header row and those are the names for fields
deals with quote fields and commas

import csv 
import pprint

datadir = ""
datafile = "beatles-diskography.csv"

def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile, 'r') as sd:
        r = csv.DictReader(sd)
        for line in r:
            data.append(line)
            return data
if __name__ == '__main__':
    datafile = os.path.join(datadir, datafile)
    parse_csv(datafile)
    d = parse_csv(datafile)
    pprint.pprint(d)


## INTRO to XLRD
'''
helps process dozens to hundreds of files that have been published as excel
.xls and .xlsx

xlwt allows us to create excle workbooks

The following will read in all the data from a workbook
'''
pip install xlrd

import xlrd

datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    # specify which sheet you want to work with 
    sheet = workbook.sheet_by_index(0)

    # loop to read data and load it into a python list called data
    data = [[sheet.cell_value(r, col) 
                for col in range(sheet.ncols)] 
                    for r in range(sheet.nrows)]
    
    # print out row 3 and column 2
    print("\nList Comprehension")
    print("data[3][2]:",(data[3][2]))
    
    # loop through entire sheet 1 column at a time and prints out after row 50
    print("\nCells in a nested loop:")    
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if row == 50:
                print(sheet.cell_value(row, col))


    ### other useful methods:
    print("\nROWS, COLUMNS, and CELLS:")
    print("Number of rows in the sheet:", sheet.nrows)
    
    print("Type of data in cell (row 3, col 2):", sheet.cell_type(3, 2))
    print("Value in cell (row 3, col 2):", sheet.cell_value(3, 2))
    print("Get a slice of values in column 3, from rows 1-3:",sheet.col_values(3, start_rowx=1, end_rowx=4))
    
    print("\nDATES:")
    print("Type of data in cell (row 1, col 0):", sheet.cell_type(1, 0))
    '''FIX
    print(exceltime = sheet.cell_value(1, 0))
    print("Time in Excel format:",exceltime)
    print("Convert time to a Python datetime tuple, from the Excel float:",xlrd.xldate_as_tuple(exceltime, 0))
    
    data = {
            'maxtime': (0,0,0,0,0,0),
            'maxvalue': 0,
            'mintime':(0,0,0,0,0,0),
            'minvalue': 0,
            'avgcoast': 0
            }
    '''
    return data

def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)
test()

### parsing through and reviewing 2 columns
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format

"""

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    
    # look at all values in column 1
    cv = sheet.col_values(1,start_rowx=1, end_rowx=None)
    
    # get max val and min val in the entire column
    maxval = max(cv)
    minval = min(cv)
    
    #find where the values exist using index
    maxpos = cv.index(maxval) + 1 # +1 ensures wont review headers
    minpos = cv.index(minval) + 1
    
    # get the actual time
    maxtime = sheet.cell_value(maxpos,0)
    # turn the time into a date tuple
    realtime = xlrd.xldate_as_tuple(maxtime, 0)
   # get the actual min time
    mintime = sheet.cell_value(minpos, 0)
   # turn the time into a date tuple
    realmintime = xlrd.xldate_as_tuple(mintime, 0)
    
    # create dictionary with our stats
    data = {
            'maxtime': realtime,
            'maxvalue': maxval,
            'mintime': realmintime,
            'minvalue': minval,
            'avgcoast': sum(cv) / float(len(cv))
            }
    return data

data = parse_file(datafile)
import pprint
pprint.pprint(data)

def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)
test()


    



