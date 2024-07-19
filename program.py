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
TODO:
    Section---Research: 
    1. Ohm's Law
    2. Trig limits
    3. Rate and time
    4. Logic gates
    5. Temperature equations
    6. The science of black holes
    7. Bitwise Operators
'''

###################### Functions ########################
def convertBinaryToBoolean(bits: int) -> list:    
    """
    Convert a binary literal into a boolean list

    Args:
        bits (int): Any binary literal

    Returns:
        list: Boolean
    """
    
    # Convert the binary literal to a binary string and remove the '0b'
    binary_string = bin(bits)[2:]
    
    # Convert each bit to a boolean and create the boolean list
    boolean_list = [bit == '1' for bit in binary_string]
    
    return boolean_list

#TODO: Create a convert boolean list into binary function
####################### Classes #########################



class Node_Double:
    """
    A basic structure for all the objects in this World.
    This stucture has double inputs [One In, One Out].
    
    Attributes
    ----------
    dataValues : Any(String, Array, Integer, Boolean, Double)
    next : node
    previous : node
    
    Methods
    -------
    __str__() -> String :
        Return the data values within of the node.
    """
    def __init__(self, dataValues=None):
        self.dataValues = dataValues
        self.previous = None
        self.next = None
        
    def __str__(self) -> str:
        """_summary_
           Return all properties of the node class
        Returns:
            str: dataValues, previous, next
        """
        return f'{self.dataValues}, {self.previous}, {self.next}'
        

#TODO: Make Single Input Node Class
#TODO: Make Single Output Node Class

class Computer:
    
    """
    Create a computer based off of for elements, 
    A CPU, a set amount of RAM, a set amount of storage,
    and a operating system.
    
    TODO:
    Explain and break down how to computer when function,
    input, and output Data [Binary]
    """
    
    def __init__(self, cpu, ram, storage, os):
        self.cpu = cpu 
        self.ram = ram
        self.storage = storage
        self.os = os

################### Test Program ##################        
e1 = Node_Double('Mon')
e2 = Node_Double('Wed')
e3 = Node_Double('Tue')

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