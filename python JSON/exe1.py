import json

with open("sample-data.json",'r') as file:
  a = json.load(file)

print("Interface Status")
print("="*80)
print("layer                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  -----")

for z in a['imdata'] :
   layer = z['l1PhysIf']['attributes']["layer"]
   Description = z["l1PhysIf"]['attributes']['descr'] 
   Speed = z["l1PhysIf"]['attributes']['speed']
   MTU = z["l1PhysIf"]['attributes']['mtu']
   if len(layer) == 1 :
       print(layer , Description ,"                            " , Speed , MTU)
   else:
       print(layer , Description ,"                             ",Speed,MTU)