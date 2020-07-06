class reservation:
    def __init__(self,time,start,destination,traintype,seats):
        self.time=time
        self.start=start
        self.destination=destination
        self.traintype=traintype
        self.seats=seats
    def print(self):
        print( self.time,self.start,self.destination,self.traintype,self.seats)