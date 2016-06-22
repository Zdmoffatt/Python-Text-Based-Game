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
Special2Connection  = <boolean>
Special3Connection  = <boolean>
Special4Connection  = <boolean>
Special5Connection  = <boolean>

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









































roomFile.close()