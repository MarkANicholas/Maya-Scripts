import json
from json.decoder import JSONDecodeError
import os
print("JsonUtils")

class JsonUtils(object):
    def __init__(self):
        self.saveData = None
        self.loadedData = None

    def append(self, data, path, overwrite=False):
        #check if there is a file at the path
        if os.path.exists(path):
            #check if the file is empty
            with open(path, 'r') as readFile:
                try:
                    self.saveData = json.load(readFile)
                except JSONDecodeError:
                    #if the file is an empty json, write to it instead of erroring.
                    with open(path, 'w') as openFile:
                        json.dump(data, openFile)
                    return
                if len(self.saveData) != 0:
                    #check data with the same key exists
                    dataExists = self.checkDataExists(data, path)
                    if (dataExists):
                        if overwrite==True:
                            self.saveData.update(data)
                        else:
                            raise Exception ("Data of this name already exists at this path, overwrite flag not enabled")                            
                    else:
                        self.saveData.update(data)
                else:
                    self.saveData.update(data)

            with open(path, 'w') as openFile:
                json.dump(self.saveData, openFile)                
        else:
            raise Exception ("Path does not exist")

    def save(self, data, path):
        #Main save function, should decide if the file is appended or not
        if data != None and path != None:
            if not os.path.exists(path):
                with open(path, "w+") as newFile:
                    json.dump(data, newFile)
            else:
                self.append(data, path)
        else:
            raise Exception ("data or path was None")

    def load(self, file):
        with open(file, 'r') as readFile:
            self.loadedData = json.load(readFile)
            return self.loadedData

    def checkDataExists(self, data, path):
        for jsonKey in self.saveData:
            for dataKey in data:
                if jsonKey==dataKey:
                    print("key value exists already: {} matches {}".format (jsonKey, dataKey))
                    return True
        return False        
        

testData={"Key":"Value"}
filepath =r"C:/Code/maya/outputTests/test.json"
filepath = filepath.strip()

util = JsonUtils()
util.save(testData, filepath)
