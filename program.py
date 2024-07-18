'''
    A node that represents a spacecraft
    that is located on the edge of a black hole
    in space.
    
    ***** Main Elements *****
    * Space Ship
    * Ship Computer
    * Space Network
    * The black hole
    
    ---------------------------------------------
        
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

    Ship Traits:
    Weight
    Armour 
        
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

'''
    Section---Research: 
    1. Ohm's Law
    2. Trig limits
    3. Rate and time
    4. Logic gates
    5. Temperature equations
    6. The science of black holes
'''


####################### Classes #########################



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