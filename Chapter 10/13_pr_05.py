'''
1 2 3 4 5 6 7 8 9 10
'''

# class Train:
#     def __init__(self, name, fare, seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats

#     def getStatus(self):
#         print("************")
#         print(f"The name of the train is {self.name}")
#         print(f"The seats available in the train are {self.seats}")
#         print("************")

#     def fareInfo(self):
#         print(f"The price of the ticket is: Rs {self.fare}")

#     def bookTicket(self):
#         if(self.seats>0):
#             print(f"Your ticket has been booked! Your seat number is {self.seats}")
#             self.seats = self.seats - 1
#         else:
#             print("Sorry this train is full! Kindly try in tatkal")

#     def cancelTicket(self, seatNo):
#         pass

# intercity = Train("Intercity Express: 14015", 90, 2)
# intercity.getStatus() 
# intercity.bookTicket()
# intercity.bookTicket()
# intercity.bookTicket()
# intercity.getStatus()


class Train:
    def __init__(self,name,seats,fair):
        self.name = name
        self.seats = seats
        self.fair = fair

    def getStatus(self):
        print("*****************")
        print(f"The train name is {self.name}")
        print(f"The no. of seats available is {self.seats}")
        print("*****************")

    def fairInfo(self):
        print(f"The fair of is train is {self.fair}")

    def bookTickets(self):
        if(self.seats>0):
            print(f"your ticket is booked , your ticket no. is {self.seats}")
            self.seats = self.seats - 1
        else:
            ("Train is full")
    
intercity = Train("intercity express:1431",4,90)
intercity.getStatus()
intercity.bookTickets()
intercity.bookTickets()
intercity.getStatus()