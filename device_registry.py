##
#
# home asistant device registry
# 2021 by Martin Schlatter, Germany
#
import json
import csv
import itertools

with open('.storage/core.area_registry') as json_file:
    areareg = json.load(json_file)

areas = {}
for area in areareg["data"]["areas"]:
    id = area["id"]
    name= area["name"]
    areas[id] = name

with open('.storage/core.device_registry') as json_file:
    d = json.load(json_file)

models=[]

with open('devreg.csv', mode='w') as devreg:
 fieldnames = ["name","friendlyname","manufacturer","model","conn","id domain","device id","ha-id","area"]
 writer = csv.writer(devreg, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)  # csv.QUOTE_MINIMAL
 writer.writerow(fieldnames)
 for device in d["data"]["devices"]:
    conn = device["connections"][0][0] if len(device["connections"])>0 else None
    iddomain = device["identifiers"][0][0] if (len(device["identifiers"])>0 and len(device["identifiers"][0])>0) else None
    id  = device["identifiers"][0][1] if (len(device["identifiers"])>0 and len(device["identifiers"][0])>1) else None
    manu = device["manufacturer"]
    model = device["model"]
    name  = device["name"]
    friendlyname = device["name_by_user"]
    area  = device["area_id"]
    internal_id = device["id"]
    if area in areas:
        area = areas[area]  # replace id with name
    if manu is not None and model is not None:
        if manu is None: manu=''
        if model is None: model=''
        if conn is None: conn=''
        if iddomain is None: iddomain=''
        models.append((manu,model,conn,iddomain))

    writer.writerow([name,friendlyname,manu,model,conn,iddomain,id,internal_id,area])


key_func = lambda x: x

models.sort(key=key_func)
i=1
with open('models.csv', mode='w') as m:
    writer = csv.writer(m, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(["id","manu","model","conn","domain"])
    for key, group in itertools.groupby(models, key_func): 
        writer.writerow((i,)+key)
        i=i+1
