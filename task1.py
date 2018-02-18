#!/usr/bin/python

import json, pdb, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', type=int, help="Enter gram unit ...", required=False)
args = parser.parse_args()


json_file='data.json'

# Reading jason format data from file
json_data=open(json_file)

#Loading Jason data
data = json.load(json_data)

#Api: To convert based on required units of medicine Eg. for 25gm, 50gm, etc
def convert_quantity(quant_value):
    cur_quan = 100
    if(args.o):
        cur_quan = int(args.o)
    new_quant = (quant_value/100)*cur_quan
    return new_quant

#Api: To find for leaf node and skip further iterations 
def check_if_notiterable(type_ds):
#    type_ds = str(type(raw_data))
    if ('unicode' in type_ds):
        return True
    elif('bool' in type_ds):
        return True
    elif('int' in type_ds):
        return True
    elif('str' in type_ds):
        return True
    elif('float' in type_ds):
        return True

#Api: Recursive call to convert the quantiy unit based on required grams Eg. 25gm, 50gm, etc
def iterate(raw_data,ele=None):
    if(ele == None):
        return
    # if ele is Dict then call for iterate with new dict and and call with its key value
    elif('dict' in str(type(ele))):
        for key in ele.keys():
         #   print(key)
            iterate(ele,key)
    elif(ele == "quantity"):
        #print("Before conversition :"+str(raw_data[ele]))
        raw_data[ele]=convert_quantity(raw_data[ele])
        #print("After conversition :"+str(raw_data[ele]))
    else:
        # if no leaf further to iterate then return from here.
        if(check_if_notiterable(str(type(raw_data[ele])))):
            return
        for key in raw_data[ele]:
            #print(key)
            iterate(raw_data[ele], key)


#Recursive call
iterate(data, "data")


print(data)

