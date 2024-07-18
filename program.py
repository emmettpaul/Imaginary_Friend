'''
    A node that represents a spacecraft
    that is located on the edge of a black hole
    in space.
    
    Types of spacecraft:
        Space Stations
        Space ships
        Resident Living stations
        Satelite
            Telescope
            Antenna
            * Drone (Has it one class)
                Explorer
        Drone

            
        
    Main Elements of A spacecraft
    Onboard Computer
        CPU/s
        RAM
        Storage
        Power
        * System
            Architecture
                Gates
                CPU
                Aritmetic Unit
                Resistor
                Transistor
                Capacitor
                Digital to Analog Convertor
                Analog to Digital Convertor
            * Conventional
            * Quantum
            
    Control
    Antenna
                
        
    
'''
class node:
    def __init__(self, dataValues=None):
        self.dataValues = dataValues
        self.previous = None
        self.next = None
        
        
e1 = node('Mon')
e2 = node('Wed')
e3 = node('Tue')

e1.next = e3
e3.previous = e1
e3.next = e2
e2.previous = e3

thisvalue = e1

while thisvalue:
    print(thisvalue.dataValues)
    thisvalue = thisvalue.next
    

thisvalue = e2
print()
while thisvalue:
   
    print(thisvalue.dataValues)
    thisvalue = thisvalue.previous