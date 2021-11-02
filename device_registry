import json
import csv

with open('.storage/core.area_registry') as json_file:
    areareg = json.load(json_file)

areas = {}
for area in areareg["data"]["areas"]:
    id = area["id"]
    name= area["name"]
    areas[id] = name

with open('.storage/core.device_registry') as json_file:
    d = json.load(json_file)

#>>> data["data"]["devices"][20]
#{'config_entries': ['d6a5c08bfbec4a1eba04d675f19cdf59'], 'connections': [['zigbee', '00:15:8d:00:04:14:05:27']], 'identifiers': [['zha', '00:15:8d:00:04:14:05:27']], 
#  'manufacturer': 'LUMI', 'model': 'lumi.sensor_motion.aq2', 'name': 'LUMI lumi.sensor_motion.aq2', 
# 'sw_version': None, 'entry_type': None, 'id': '6cce8aa3217f4e1688df18cdaf0d6a4d', 'via_device_id': '283c921e0f6742418aa167e4ee0fe7db', 
# 'area_id': '77475f19639f41738e46bf768b44c053', 'name_by_user': 'LUMI lumi.sensor_motion.aq2_Kuechenarbeitsplatte', 'disabled_by': None, 'configuration_url': None}

with open('devreg.csv', mode='w') as devreg:
 fieldnames = ["name","friendlyname","manufacturer","model","conn","id domain","device id","ha-id","area"]
 writer = csv.writer(devreg, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)  # csv.QUOTE_MINIMAL
 #writer.writeheader()
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
    #print(model)

    writer.writerow([name,friendlyname,manu,model,conn,iddomain,id,internal_id,area])
    #print(name,conn,ident,manu,model,name)
