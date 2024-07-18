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