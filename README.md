Hotel Management System

The objective of this project is to simplify the hotel operations by automating the major aspects of hotel management which include checking the availability of rooms, room amenities, 
check-in, check-out, ordering food, and viewing all the booking record.

Code Architecture:

1. Database Connectivity (`pyodbc` Setup):
▪ The `pyodbc` library is used to connect Python applications to SQL Server using 
ODBC (Open Database Connectivity).
2. Creating Tables:
▪ Two tables are created for storing data:
i. `bookings`: Stores booking details such as `Booking_Id`, `Room_Number`, 
`Name`, `Check_In_Date`, and `Check_Out_Date`.
ii. ‘food_orders`: Stores food order details including `Room_No`, `Booking_Id`, 
`Order_Id`, `Order_Date`, `Food_Items`, `Quantity`, `Total`.
▪ Two tables are there in the database to retrieve information:
i. ‘rooms’: Storing room details such as ‘Room_Number’, ‘Room_Type’, 
‘Price_per_night’, ‘Availability_Status’.
ii. ‘menu’: Storing food items details such as ‘Dish_Type’, ’Dish’, ‘Price’


The tables created and their relationship is as shown below-

![Screenshot (603)](https://github.com/SunidhiSharma09/Python_Projects/assets/167216512/664c5a5b-ee7c-4471-b18d-67345553b008)

3. Functionalities:
   
▪ Room Management:
- Fetches and displays available rooms from the ‘rooms’ table (`view_available_rooms()` 
 function).
- Allows users to view room amenities based on room type (`room_info()` function).
 
▪ Booking Management:
- Allows users to book a room (`book_room()` function), generating a unique 
 `Booking_Id` and store details in the ‘bookings’ table.
- Marks room Availability status as `Booked` in the `rooms` table upon successful 
 booking.

▪ Food Order Management :
 - Facilitates food ordering for guests (`restaurant()` function), retrieving food item 
 details from the ‘menu’ table and storing the order in the ‘food_orders’ table, 
 associating orders with specific bookings (`Booking_Id`).
- Also allows modification of food orders (addition/removal of items).
  
▪ Check-out Process:
 - Manages the check-out process (`checkout_room()` function), calculating total 
 charges including room stay and food orders.
- Updates the `rooms` table to mark room Availability status as `Available` after 
 check-out.

▪ Viewing All Bookings:
- Displays all booking records (`view_all_bookings()` function) by retrieving data from 
 the ‘bookings’ table, sorted by check-in date, offers a comprehensive view of the 
 current reservations.
 
▪ User Interface (`home()` function):
 - Serves as the home page for users to interact with different functionalities.
 - Provides error handling and input validation to ensure smooth operation
