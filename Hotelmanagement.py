class Customer:
    def __init__(self,name,phone):
        self.name=name 
        self.phone=phone
    def __str__(self):
        return f"Name : {self.name} \n Phone : {self.phone}"
class Room:
    def __init__(self,r_no,room_type,price):
        self.r_no=r_no
        self.room_type=room_type
        self.price=price
        self.is_available=True
    def __str__(self):
        status="Available" if self.is_available else "Booked"
        return f"Room : {self.r_no}, Type : {self.room_type}, Price : ${self.price}/day is {status}. "
class Booking:
    def __init__(self,customer,room):
        self.customer=customer
        self.room=room
    def confirm_booking(self):
        if not self.room.is_available:
            print(f"Room : {self.room.r_no} is already booked .")
        else:
            self.room.is_available=False
            print(f" Booking is confirmed for Room : {self.room.r_no} for {self.customer.name}.")
    def checkout(self):
        if self.room.is_available:
            print(f"{self.customer.name} has checkedout from Room : {self.room.r_no} successfully. ") 
        else:
            print(f"Room : {self.room.r_no} is not booked.")
class Hotel:
    def __init__(self,hname):
        self.hname=hname
        self.rooms=[]
        self.bookings=[]
    def add_rooms(self,r_no,room_type,price):
        room=Room(r_no,room_type,price)
        self.rooms.append(room)
    def book_room(self,room_no,customer_name,phone):
        customer=Customer(customer_name,phone)
        for room in self.rooms:
            if room.r_no==room_no:
                booking=Booking(customer,room)
                booking.confirm_booking()
                self.bookings.append(booking)
                return 
        print("Room not found.")
    def checkout_room(self,room_no):
        for booking in self.bookings:
            if booking.room.r_no==room_no and not booking.room.is_available:
                booking.room.is_available=True
                booking.checkout()
                return
            print("booking not found .")
    def show_rooms(self):
        for r in self.rooms:
            print(r)
    
        

hotel = Hotel("Royal Palace")

hotel = Hotel("Royal Palace")

hotel.add_rooms(101, "Single", 100)
hotel.add_rooms(102, "Double", 150)
hotel.add_rooms(103, "Suite", 300)

hotel.show_rooms()
hotel.book_room(102, "Alice", "1234567890")
hotel.book_room(103, "Bob", "9876543210")

hotel.show_rooms()

hotel.checkout_room(102)
hotel.show_rooms()


