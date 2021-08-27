"""
Data Aggregation Code :
This program collect the data from different directories. 
Plus, it allows you to format the names of files.

"""

import os

class Count:
    """
    Class for just counting.
    """
    value=0
    def act(self):
        Count.value+=1
        return Count.value
    def reset(self):
        Count.value = 0
    def getValue(self):
        return Count.value

class Path:

    Source = "C:/Users/wsChoe/Desktop/from/"

    img_Repository = "C:/Users/wsChoe/Desktop/to/img/"
    label_Repository = "C:/Users/wsChoe/Desktop/to/label/"

    def getObjSource(self,obj):
        return Path.Source + str(obj) + "/"

    def img_source(self,obj):
        return Path.Source + str(obj) + "/img"
    def label_source(self,obj):
        return Path.Source + str(obj) + "/label"

    def img_repository(self):
        return Path.img_Repository
    def label_repository(self):
        return Path.label_Repository

# Value Setting
DEBUG = False
ct = Count()
path = Path()
objs = ["mouse"]

# image & label process
for obj in objs:
    # Process setting
    source = path.getObjSource(obj)
    img_source = source + "img/"
    label_source = source + "label/"
    img_names = os.listdir(img_source)
    label_names = os.listdir(label_source)
    count = 0

    # acting
    for img_name in img_names:
        
        number = ct.act()
        length = len(img_name)
        label_name = img_name[:length-4] + ".txt"
        
        if DEBUG == False:
            #img & label renaming
            os.rename(img_source+img_name, path.img_repository() + obj + "-" + str(number) + ".jpg" )
            os.rename(label_source+label_name ,path.label_repository() + obj + "-" + str(number) + ".txt")
        else:
            print(source)
            print(img_source)
            print(label_source)
            print(img_names)
            print(label_names)
            print(img_source+img_name)
            print(path.img_repository() + obj + "-" + str(number) + ".jpg")
            print(label_source+label_name)
            print(path.label_repository() + obj + "-" + str(number) + ".txt")
    print(obj + " is done.")
        