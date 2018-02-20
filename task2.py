#!/usr/bin/python

import requests
import pandas as pd

name = "KeiNishikori"

#url="http://www.tennisabstract.com/cgi-bin/player.cgi?p="+name
url = "http://www.minorleaguesplits.com/tennisabstract/cgi-bin/jsmatches/"+name+".js"

r = requests.get(url)
print(r.status_code)
print(r.headers['content-type'])

match = r.text
#print(match)
match = match.encode('ascii','ignore')
dictionary = {" "  : "",
              "\n" : "",
              ";"  : ""}

for i,j in dictionary.iteritems():
    match = match.replace(i,j)
    match_data = match[match.find("varmatch")+11:]
#print(match)
#print(match_data)
match_data_final = eval(match_data)
#print(match)

data_url_final = []
for i, value in enumerate(match_data_final):
#    print(i, value)
    if(value[34] == ""):
        continue
    else:
        x = { "date" : pd.to_datetime(value[0]),
            "ofwon_osown" : int(value[34]) + int(value[35]),
            "opts" : int(value[32]),
            "fwon_swon" : int(value[25]) + int(value[26]),
            "pts" : int(value[23]),
            "ace" : int(value[21]) }
        data_url_final.append(x)

#print(data_url_final)
# Saving data to dataframe
data=pd.DataFrame(data_url_final)

#print(data)
# Sorting the obtained data based on date and fetching last 10 matches.
data=data.sort_values(by='date',ascending=False)
data_table=data.iloc[0:9]

#Calculate sum of above obtained values.
ofwon_osown_total = data_table['ofwon_osown'].sum()
opts_total = data_table['opts'].sum()
fwon_swon_total = data_table['fwon_swon'].sum()
pts_total = data_table['pts'].sum()
ace_total = data_table['ace'].sum()


ace_pc = (float(ace_total)/float(pts_total))*100
spw_pc = (float(fwon_swon_total)/float(pts_total))*100
rpw_pc = (float(1 - (float(ofwon_osown_total)/float(opts_total))))*100

print("\n")
print(data_table)

print("\n")
print("Player name: "+name)
print{"ace %": ace_pc, "spw %": spw_pc, "rpw %": rpw_pc}
