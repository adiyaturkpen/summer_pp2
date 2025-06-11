import json
fi = open(r"C:\Users\Lenovo\pp2\pp2-summer\lab4\json\sample-data.json")
data = json.load(fi)
moredata= data["imdata"]
print("Interface Status" "\n"
"================================================================================" "\n"
"DN                                                 Description           Speed    MTU  " "\n"
"-------------------------------------------------- --------------------  ------  ------" "\n")

for item in moredata:
    print(item["l1PhysIf"]["attributes"]["dn"],'                            ',item["l1PhysIf"]["attributes"]["speed"],' ',item["l1PhysIf"]["attributes"]["mtu"])
