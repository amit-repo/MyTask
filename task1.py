#!/usr/bin/python

import json, pdb

json_file='data.json'

# Reading jason format data from file
json_data=open(json_file)

#Loading Jason data
data = json.load(json_data)

#Api: To convert based on required units of medicine Eg. for 25gm, 50gm, etc
def convert_quantity(cur_quan, quant_value):
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
def iterate(raw_data,ele=None, data_instance=100):
    if(ele == None):
        return
    # if ele is Dict then call for iterate with new dict and and call with its key value
    elif('dict' in str(type(ele))):
        for key in ele.keys():
         #   print(key)
            iterate(ele,key,data_instance)
    elif(ele == "quantity"):
        #print("Before conversition :"+str(raw_data[ele]))
        raw_data[ele]=convert_quantity(data_instance,raw_data[ele])
        #print("After conversition :"+str(raw_data[ele]))
    else:
        # if no leaf further to iterate then return from here.
        if(check_if_notiterable(str(type(raw_data[ele])))):
            return
        for key in raw_data[ele]:
            #print(key)
            iterate(raw_data[ele], key, data_instance)


#Recursive call
iterate(data, "data", 25)


print(data)

