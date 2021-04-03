class bus():
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getinfo(self):
        print(self.name)
        print(self.fare)
        print(self.seats)

    def booked(self,select):
        self.select=select
        booked=[]
        booked.append(select)
        print(booked)
    
    def book(self,user):
        self.user=user
        
        if self.user>self.seats:
            print("seat is unavailabe")
    
        elif self.seats>0:
            print("seats are availabe")
            self.seats=self.seats-user
                
        else:
            print("no seats")
        
        
    
    
        
                

            
        

b=bus("Akash travels",1000,40)
b.getinfo()
user=int(input("Please select number of seats\n"))
select_seat=int(input("Please select seat number\n"))
b.book(user)
b.booked(select_seat)
b.getinfo()