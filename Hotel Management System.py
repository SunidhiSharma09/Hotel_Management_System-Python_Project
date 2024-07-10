#!/usr/bin/env python
# coding: utf-8

# ---------------------------------------------------------------HOTEL MANAGEMENT SYSTEM---------------------------------------------------------------------------

# In[ ]:





# In[1]:


# Connected to SQL Server.
import pyodbc

connection=pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-THH90DU;"
    "Database=AnCasa;"
    "Trusted_Connection=yes;"
)

cursor=connection.cursor()

# To select all data from the table 'rooms' of connected database.

cursor.execute("SELECT * FROM rooms")
cursor.fetchall()


# In[2]:


import pyodbc

connection=pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-THH90DU;"
    "Database=AnCasa;"
    "Trusted_Connection=yes;"
)

cursor=connection.cursor()

# To create a table 'bookings' in SQL Database to store all the booking records.

cursor.execute(
    '''
    CREATE TABLE bookings (
    Booking_Id int,
    Room_Number int ,
    Name varchar(30),
    Check_In_Date date,
    Check_Out_Date date
    )'''
)

connection.commit()


# In[ ]:





# In[ ]:


import pyodbc

connection=pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-THH90DU;"
    "Database=AnCasa;"
    "Trusted_Connection=yes;"
)

cursor=connection.cursor()

# To create a table 'food_orders' in SQL Database to store all the food ordered records.

cursor.execute('''create table food_orders(
Room_No int,
Booking_Id int,
Order_Id int,
Order_Date date,
Food_Items varchar(30),
Quantity int,
Total int)'''
)

connection.commit()


# In[ ]:





# In[ ]:


# MAIN PROGRAM FOR HOTEL MANAGEMENT SYSTEM.


# In[26]:


#Function to view room amenities.

def room_info():
    while True:
        print('To see the room amenities available')
        print('----------------------------------------------------------------------------------------------------------------------------------------------------')
        print('')
        type=input("Enter room type:")
        print('')
        
        if type.lower()=="basic":
            print('------Amenities Available are-------')
            print('1.House Keeping')
            print('2.Toiletries and Towels')
            print('3.Telivision and Telephone')
            print('4.Coffee and Tea Making Kit')
            print('')
            
        elif type.lower()=="standard":
            print('------Amenities Available are------')
            print('1.House Keeping')
            print('2.Toiletries')
            print('3.Towels,Bathrobes and Slippers')
            print('4.Telivision and Telephone')
            print('5.Free Wifi')
            print('6.Coffee and Tea Making Kit')
            print('7.Free Breakfast')
            print('')
            
        elif type.lower()=="delux":
            print('------Amenities Available are------')
            print('1.House Keeping')
            print('2.Toiletries')
            print('3.Towels,Bathrobes and Slippers')
            print('4.Personal Care Products')
            print('5.Telivision and Telephone')
            print('6.Free Wifi')
            print('7.Premium Coffee and Tea Making Kit')
            print('8.Free Breakfast')
            print('9.Free Parking')
            print('10.Gym or Fitness Centre access')
            print('11.Refrigerator-Mini Bar')
            print('12.Snacks Basket')
            print('13.Borrowing Closet')
            print('14.Personalized Books and Movies')
            print('15.Personalized Plant Set-up')
            print('')
            
        choice=input('Do you want to enter more?(Y/N):')
        print('')
        if choice.upper()=='N':
            break

#Function to view rooms available

def view_available_rooms():
    import pyodbc
    
    connection=pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-THH90DU;"
        "Database=AnCasa;"
        "Trusted_Connection=yes;"
    )
    
    cursor=connection.cursor()

    print('---------------------------------------------------Rooms Available---------------------------------------------------------------------------------')
    print('')
    cursor.execute("select*from rooms where Availability_Status='Available'")
    for i in cursor.fetchall():
        print(f"Room No.:{i[0]} | Room Type:{i[1]} | Price:Rs.{i[2]}/night")
    print('')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------')

    info=input('Do you want to get room amenities information?(Y/N)')
    print('')
    if info.upper()=='Y':
       room_info()
    else:
        print('')


#Function to book a room.

def book_room():
    import datetime
    import random
    import pyodbc
    
    connection=pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-THH90DU;"
        "Database=AnCasa;"
        "Trusted_Connection=yes;"
    )
    
    cursor=connection.cursor()

    print('--------------------------------------------------------------TO CHECK-IN---------------------------------------------------------------------------')
    print('')
    while True:
        rn=input("Enter Room Number:")
        cursor.execute(f"select Room_Number from rooms where Room_Number={rn}")
        room= cursor.fetchone()
        if room :
                cursor.execute(f"select Availability_Status from rooms where Room_Number={rn}")
                for r in cursor.fetchall()[0]:
                    if r=='Available':
                        cursor.execute(f" select Availability_Status,Room_Type,Price_per_night from rooms where Room_Number={rn}")
                        for j in cursor.fetchall():
                            print(f"{j[0]}")
                            print(f"Room_Type-{j[1]}")
                            print(f"Price/night is Rs.{j[2]}")
                            rt=j[1]
                        bi=random.randint(1000,9999)
                        print('BookingId:',bi)
                        try:
                            guest=int(input('Enter number of guest (max.3/room):'))
                            for g in range(guest):
                                name=input('Enter Name:')
                                cin=input('Enter Check-In Date(YYYY-MM-DD):')
                                cursor.execute(
                                          ''' insert into bookings( Booking_Id,Room_Number,Room_Type, Name,Check_In_Date) values(?,?,?,?,?)''',
                                                        bi,rn,rt,name,cin)
                                connection.commit()
                            cursor.execute(f"update rooms set Availability_Status='Booked' where Room_Number={rn}")
                            connection.commit()
                            cursor.execute(f"select*from rooms where Room_Number={rn}")
                            for k in cursor.fetchall():
                                print('')
                                print(f"Room No.:{k[0]}-{k[1]},Status-{k[3]}")
                            print('Booking Successful!!!')
                            print('')
                        except:
                            print('Invalid Input.')
                    elif r=='Booked':
                        print('Room Not Available.')
                        print('')
                 
        else:
                print('')
                print('Invalid Room Number.')
                
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
        choice1=input('Do you want to enter more?(Y/N)')
        print('')
        if choice1.upper()=='N':
           break


# Function to order food from the hotel.

def restaurant():

    import random
    import pyodbc
    
    connection=pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-THH90DU;"
        "Database=AnCasa;"
        "Trusted_Connection=yes;"
    )
    
    cursor=connection.cursor()

    print('--------------------------------------------------------------TO ORDER FOOD-------------------------------------------------------------------------')
    print('')
    while True:
        rno=int(input('Enter a Room Number:'))
        cursor.execute(f"select Room_Number from rooms where Room_Number={rno}")
        room=cursor.fetchone()
        if room:
            cursor.execute(f"select Availability_Status from rooms where Room_Number={rno}")
            for i in cursor.fetchall()[0]:
                if i=='Booked':
                    cursor.execute(f"select distinct(Room_Number), Booking_Id, Check_In_Date from bookings where Room_Number={rno} and Check_In_Date=(select max(Check_In_Date) from bookings where Room_Number={rno} )")
                    for all in cursor.fetchall():
                        print('Room Number:',all[0],' ','Booking Id:',all[1],' ','Check-in Date:',all[2])
                        bid=all[1]
                    oid=random.randint(1000,9999)
                    print('')
                    print('Order Id:',oid)
                    od=input('Enter Order Date(YYYY-MM-DD):')
                    cost=0
                    print('')
                    while True:
                        order=input('Enter Food Item:').title()
                        cursor.execute(f"select Dish, Price from menu where Dish='{order}' ")
                        o=cursor.fetchone()
                        if o:
                            qty=int(input('Enter Quantity:'))
                            total=(qty*o[1])
                            cost=cost+total
                            cursor.execute(f"insert into food_orders(Room_No,Booking_Id,Order_Id,Order_Date,Food_Items,Quantity,Total) values(?,?,?,?,?,?,?)",
                                           rno,bid,oid,od,order,qty,total)
                            connection.commit()
                        else:
                            print('Item not available or inavalid input.')
                        choice=input('Do you want to enter more dish?(Y/N):')
                        if choice.upper()=='N':
                            print('')
                            break
                                
                              
                    while True:
                        final=input('Do you want to remove anything?(Y/N)')
                        if final.upper()=='Y':
                            item=input('Enter Food Item to remove:').title()
                            q=int(input('Enter Quantity:'))
                            cursor.execute(f"select Quantity from food_orders where Order_Id={oid} and Food_Items='{item}'")
                            for qty in cursor.fetchall()[0]:
                                if qty>1 and q<qty:
                                    cursor.execute(f"update food_orders set Quantity= Quantity-{q} where  Order_Id={oid} and Food_Items='{item}' ")
                                    connection.commit()
                                else:
                                    cursor.execute(f"delete food_orders where  Order_Id={oid} and Food_Items='{item}' ")
                                    connection.commit()
                                cursor.execute(f"select Price from menu where  Dish ='{item}' ")
                                for p in cursor.fetchall()[0]:
                                    removed=p*q
                                cost=cost-removed
        
                        else:
                             break
                                  
                    print('')
                    print('Your Final Order is:')
                    cursor.execute(f"select Food_Items, Quantity from food_orders where Room_No={rno} and Order_Id={oid}")
                    for f in cursor.fetchall():
                            print('Food_Items:',f[0],' ','Quantity:',f[1])

                        
                    print('')
                    print('Total Bill: Rs',cost)
                    print('')
                else:
                    print('')
                    print('Room not booked.')

        else:
            print('')
            print('Invalid Room Number')
                    
        print('----------------------------------------------------------------------------------------------------------------------------------------------------')
        choice1=input('Do you want to enter more order?(Y/N):')
        print('')
        if choice1.upper()=='N':
            break

#Function to check-out.

def checkout_room():
    import datetime
    import pyodbc
    
    connection=pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-THH90DU;"
        "Database=AnCasa;"
        "Trusted_Connection=yes;"
        )
        
    cursor=connection.cursor()

    print('--------------------------------------------------------------TO CHECK-OUT-------------------------------------------------------------------------')
    print('')
    while True:
             rno=int(input('Enter Room Number to Check-Out:'))
             print('')
             cursor.execute(f"select Room_Number from rooms where Room_Number={rno}")
             co=cursor.fetchone()
             if co:
                 cursor.execute(f"select Availability_Status from rooms where Room_Number={rno}")
                 for i in cursor.fetchall()[0]:
                    if i=='Booked':
                         cursor.execute(f"select * from bookings where Room_Number={rno} and Check_In_Date=(select max(Check_In_Date) from bookings where Room_Number={rno} )")
                         for all in cursor.fetchall():
                             print('Booking ID:',all[0],' ','Room Number:',all[1],' ','Room Type:',all[2],' ','Name:',all[3],' ','Check-in Date:',all[4])
                             bid=all[0]
                         print('')
                         print('          ----------------------------------------------------FOOD ORDERED---------------------------------------------------------------')
                         cursor.execute(f"select * from food_orders where  Room_No={rno} and Booking_Id={bid}")
                         for j in cursor.fetchall():
                             print('Order Id:',j[2],' ','Order Date:',j[3],' ','Food Item:',' ',j[4],' ','Qty-',j[5],' ','Cost:',j[6])
                         print('')
                         cursor.execute(f"select sum(total) as Total_Food_bill from food_orders where Room_No={rno} and Booking_Id={bid}")
                         for k in cursor.fetchall():
                             if k[0] is None:
                                 fb=0
                                 print('No Food Ordered.')
                             else:
                                 fb=k[0]
                                 print('Total Food Bill is: Rs',k[0])
                         print('')
                         cout=(input('Enter Check-Out Date(YYYY-MM-DD):'))
                         date2=datetime.datetime.strptime(cout,'%Y-%m-%d')
                         date1=datetime.datetime.strptime(all[4],'%Y-%m-%d')
                         diff=(date2-date1).days
                         print('Stay Duration:',diff,'days')
                         cursor.execute(f" select Price_per_night from rooms where Room_Number={rno}")
                         for i in cursor.fetchall():
                              rc=i[0]*diff
                              print("Total Room Charge is Rs ",i[0]*diff)
                         print('')
                         print('Your Total Payment is Rs',fb+rc)
                         cursor.execute(f"update bookings set Check_Out_Date='{date2}' where Booking_Id={bid}")
                         connection.commit()
                         cursor.execute(f"update rooms set Availability_Status='Available' where Room_Number={rno}")
                         connection.commit()
                         print('')
                         print(f"Room No.-{rno} Successfully Checked-Out.")
                    else:
                        print('Room Currently Not Booked.')
                    
             else:
                 print('Invalid Room Number.')
    
        
             print('---------------------------------------------------------------------------------------------------------------------------------------------------')
             choice2=input('Do you want to enter more?(Y/N)')
             print('')
             if choice2.upper()=='N':
                 break

#Function to view all bookings

def view_all_bookings():
    import pyodbc
        
    connection=pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-THH90DU;"
        "Database=AnCasa;"
        "Trusted_Connection=yes;"
            )
            
    cursor=connection.cursor()
    cursor.execute("select*from bookings order by Check_In_Date")
    print('-------------------------------------------------------------ALL BOOKING RECORD-------------------------------------------------------------------')
    print('')
    print('Booking_Id  Room_Number    Room_Type        Name              Check-In_Date        Check-Out_Date')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------')
    for all in cursor.fetchall():
        print(all[0],'         ',all[1],'        ',all[2],'     ',all[3],'         ',all[4],'           ',all[5])
        print('--------------------------------------------------------------------------------------------------------------------------------------------------')
      

#Function for Home Page

def home():
    while True:
        print('')
        print('******************************************************WELCOME TO HOTEL ANCASA***********************************************************************')
        print('')
        print('****************************************************************************************************************************************************')
        print('')
        print('Press 1. To View Available Rooms')
        print('Press 2. To Know Room Amenities Available')
        print('Press 3. To Check-In')
        print('Press 4. To Order Food')
        print('Press 5. To Check-Out')
        print('Press 6. To View All Bookings')
        print('Press 7. To Exit')
        print('')
        print('****************************************************************************************************************************************************')
        print('')

        try:
            choice=int(input('Enter your choice:'))
            print('')
            if choice==1:
                    view_available_rooms()
                
            elif choice==2:
                    room_info()
                
            elif choice==3:
                    book_room()
    
            elif choice==4:
                   restaurant()
                
            elif choice==5:
                    checkout_room()
                
            elif choice==6:
                    view_all_bookings()
                       
            elif choice==7:
                    break
    
            else:
                print('Invalid Input.')

        except:
             print('Invalid Input.')

home()


# ###### 

# In[ ]:





# In[ ]:




