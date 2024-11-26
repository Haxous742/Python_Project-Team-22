import CSV_Handler as csvh

class Device:

    device_details = {}
     #format = {"device_id" : {"name" : <> , "type" : <>, "status" : <> , "attributes" :{"attribute1" : "status","attribute2":"status"}}}

    def __init__(self ):
        pass

    def unique_device():
        pass


class Bulb(Device):

    def __init__(self ,name):
        self.name = name
        self.device_id = 
        self.type = "bulb"
        self.status = "on"

        #attributes

        self.Brightness = 0
        self.Warmth = "Low"             #warmth options : [Low , Medium , High]
        self.Colour = "White"           #colour options : [White , Yellow , red , green ,blue]

    def updateStatus(self, status):
        self.status = status
    
    def updateBrightness(self , update):
        self.Brightness = update
    
    def updateWarmth(self , update):
        self.Warmth = update

    def updateColour(self , update):
        self.Colour = update

    #write preset func here (turns on automatically at a certain time)


class Security_camera(Device):

    def __init__(self,name):
        self.name = name
        self.device_id = ''
        self.type = "Security_camera"
        self.status = "on"

    #attributes

        self.Resolution = 'FHD'         #reolution options : [SD , HD , FHD]
        self.RecordingStatus = ""       #RecordingStatus opts : []


    def updateStatus(self, status):
        self.status = status
    
    def updateResolution(self , update):
        self.Resolution = update
    
    def updateRecordingStatus(self , update):
        self.RecordingStatus = update

    #write preset func here (automaticallly  turn on recording at a certain time)



class Thermostat(Device):

    def __init__(self,name):
        self.name = name
        self.device_id = 
        self.type = "Thermostat"
        self.status = "on"

    #attributes

        self.Temperature =  24         #temperature settings : [int bw 16 to 30]
        self.Mode = "cool"                 #thermo mode opts : [Heat , cool ,fan]


    def updateStatus(self, status):
        self.status = status
    
    def updateTempature(self , update):
        self.Tempature = update
    
    def updateMode(self , update):
        self.Mode = update

    #write preset func here



class Garagedoor(Device):

    def __init__(self,name):
        self.name = name
        self.device_id = 
        self.type = "Gargedoor"
        self.status = "on"

    #attributes

        self. =                 #Garagedoor settings : 
        self. =                 #garagedoor mode opts : 


    def updateStatus(self, status):
        self.status = status
    
    def update(self , update):
        self. = update
    
    def update(self , update):
        self. = update

    #write preset func here



