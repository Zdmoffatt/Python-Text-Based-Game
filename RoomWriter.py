# RoomWriter.py
# Creates room description and information files for text based games

'''
Format of files:
<Start>
NameOfRoom = <string>
RoomDescriptionInitial = <string>
NormalDescriptionDifferent = <boolean>
RoomDescriptionNormal = <string>

NumberOfConnections = <int>
NorthConnection     = <boolean>
SouthConnection     = <boolean>
EastConnection      = <boolean>
WestConnection      = <boolean>
UpConnection        = <boolean>
DownConnection      = <boolean>
Special1Connection  = <boolean>
.
.
.
Special9Connection  = <boolean>

NumberOfItems = <int>

<ItemNum>
ItemName = <string>
ItemDescriptionInRoom = <string>
ItemDescriptionInInv = <string>

<End>
'''

print("RoomWriter.py")
print("What is the room number?")
roomNum = input()
roomFile = open(roomNum+'.txt','w')
roomFile.write("<Start>\n")

print("Please enter the room name")
roomName = input()
roomFile.write("NameOfRoom = "+roomName+"\n")

print("Please enter the inital room description")
initialDescription = input()
roomFile.write("RoomDescriptionInitial = "+initialDescription+"\n")

print("Do you wish the room to change description after it is initially entered? (y/n)")
changeDescription = input()
if(changeDescription == 'y'):
    roomFile.write("NormalDescriptionDifferent = True\n")
    print("Please enter the normal room description")
    normalDescription = input()
    roomFile.write("RoomDescriptionNormal = "+normalDescription+"\n")

else:
    roomFile.write("NormalDescriptionDifferent = False\n")
    roomFile.write("RoomDescriptionNormal = None\n")

while True:
    print("How many rooms does this room connect to?")
    rooms = input()
    if(int(rooms)>10):
        print("Thats too many, try again")
    else:
        break
roomFile.write("NumberOfConnections = "+rooms+"\n")
connections = 0

print("Is there a room to the North? (y/n)")
direction = input()
if(direction == 'y'):
    roomFile.write("NorthConnection = True\n")
    connections+=1
else:
    roomFile.write("NorthConnection = False\n")

print("Is there a room to the South? (y/n)")
direction = input()
if(direction == 'y'):
    roomFile.write("SouthConnection = True\n")
    connections+=1
else:
    roomFile.write("SouthConnection = False\n")

print("Is there a room to the East? (y/n)")
direction = input()
if(direction == 'y'):
    roomFile.write("EastConnection = True\n")
    connections+=1
else:
    roomFile.write("EastConnection = False\n")

print("Is there a room to the West? (y/n)")
direction = input()
if(direction == 'y'):
    roomFile.write("WestConnection = True\n")
    connections+=1
else:
    roomFile.write("WestConnection = False\n")

print("Is there a room to above? (y/n)")
direction = input()
if(direction == 'y'):
    roomFile.write("UpConnection = True\n")
    connections+=1
else:
    roomFile.write("UpConnection = False\n")

print("Is there a room to below? (y/n)")
direction = input()
if(direction == 'y'):
    roomFile.write("DownConnection = True\n")
    connections+=1
else:
    roomFile.write("DownConnection = False\n")

print("How many special connections are there?")
special = int(input())
for x in range (1,special+1):
    roomFile.write("Special"+str(x)+"Connection = True\n")
    connections+=1

print("How many items are in the room?")
items = input()
roomFile.write("NumberOfItems = "+items+"\n")
roomFile.write("\n")

for y in range (1,int(items)+1):
    roomFile.write(str(y))
    print("What is the item name?")
    itemName = input()
    roomFile.write("ItemName = "+itemName+"\n")
    print("What is the items description in the room?")
    inRoom = input()
    roomFile.write("ItemDescriptionInRoom = "+inRoom+"\n")
    
    print("What is the items description in inventory?")
    inInv = input()
    roomFile.write("ItemDescriptionInInv = "+inInv+"\n")
    roomFile.write("\n")


roomFile.write("<End>")
roomFile.close()