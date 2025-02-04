import pymysql
from pymysql import Error

try:
   db = pymysql.connect(host='localhost', user='root', password='1234')
except Error as e:
   print(e)
mc = db.cursor()
try:
   mc.execute('create database Amusement')
except:
   print()
mc.execute("use Amusement")
print('Amusement Park Ticket Booking System              '.center(155))


def MainMenu():
   while True:
       print('*' * 155)
       print("1. Customer menu                 ".center(155))
       print("2. Admin Menu                    ".center(155))
       print('*' * 155)
       print()
       I1 = input("Enter choice No. :")
       if I1 == "1":
           CustomerLogin()
           break
       elif I1 == "2":
           print()
           Pass = input("Enter admin password:")
           print()
           if Pass == "1234":
               AdminLogin()
               break
           else:
               print('Wrong password')
       else:
           print("Enter a valid option")

def CustomerLoginPrint():
   print('*' * 155)
   print('Customer Menu                '.center(155))
   print('1. Book Tickets              '.center(155))
   print('2. Check Booking             '.center(155))
   print('3. Edit Booking              '.center(155))
   print('4. Cancel Booking            '.center(155))
   print('5. Generate bill             '.center(155))
   print('6. Back to main menu         '.center(155))
   print('7. Exit                      '.center(155))
   print('*' * 155)

def CustomerLogin():
   CustomerLoginPrint()
   while True:
       print()
       i1 = input("Enter choice No. :")
       if i1 == "1":
           book()
           print()
           CustomerLoginPrint()
       elif i1 == '2':
           checkbookings()
           print()
           CustomerLoginPrint()
       elif i1 == '3':
           editbooking()
           print()
           CustomerLoginPrint()
       elif i1 == '4':
           cancelbooking()
           print()
           CustomerLoginPrint()
       elif i1 == '5':
           generatebill()
           print()
           CustomerLoginPrint()
       elif i1 == '6':
           MainMenu()
       elif i1 == '7':
           break
       else:
           print("Enter a valid option")
id=1
try:
   SQL = "SELECT * FROM booking"
   mc.execute(SQL)
   Rows = mc.fetchall()
   id = len(Rows) + 1
except:
   print()
def book():
   global id
   print()
   name = input('Enter name :')
   age = input('Enter Age (years) :')
   height = input('Enter height in cm :')
   phone = input('Enter mobile no. :')
   mail = input('Enter e-mail id :')
   day = input('Enter day for booking :')
   print()
   try:
       mc.execute("create table booking (ID int PRIMARY KEY,Name varchar(40),Age varchar(3),\
           Height varchar(4),Phone char(10),Mail varchar(50),Day varchar(10))")

   except:
       print()
   z = (id, name, age, height, phone, mail, day)
   ex = 'insert into booking values(%s,%s,%s,%s,%s,%s,%s);'
   mc.execute(ex, z)
   db.commit()
   print('AMUSEMENT PARK RIDES')
   print('R1-Ferris wheel', 'Price = 100 Rs')
   print('R2-Carousel', 'Price = 100 Rs')
   print('R3-Roller Coaster', 'Price = 100 Rs')
   print('R4-Bumpy cars', 'Price = 100 Rs')
   print('R5-Horror house', 'Price = 100 Rs')
   print('R6-Sky Rocket', 'Price = 100 Rs')
   print('R7-Mechanical Rodeo', 'Price = 100 Rs')
   print('R8-Cup and saucer', 'Price = 100 Rs')
   print('R9-Bungee', 'Price = 100 Rs')
   print("R10-Kid's Room", 'Price = 100 Rs')
   print()
   print('AMUSEMENT PARK TIME SLOTS')
   print('T1 : 10:30-11:00')
   print('T2 : 11:00-11:30')
   print('T3 : 11:30-12:00')
   print('T4 : 12:30-13:00')
   print('T5 : 13:30-14:00')
   print('T6 : 14:30-15:00')
   print('T7 : 15:30-16:00')
   print('T8 : 16:30-17:00')
   print()
   print('Write NR for taking no rides in any time slot')
   t1 = input('Enter ride code for T1 :')
   t2 = input('Enter ride code for T2 :')
   t3 = input('Enter ride code for T3 :')
   t4 = input('Enter ride code for T4 :')
   t5 = input('Enter ride code for T5 :')
   t6 = input('Enter ride code for T6 :')
   t7 = input('Enter ride code for T7 :')
   t8 = input('Enter ride code for T8 :')
   try:
       mc.execute(
           'create table TimeSlot(ID int PRIMARY KEY,T1 char(3),T2 char(3),T3 char(3),T4 char(3),T5 char(3),T6 char(3),T7 char(3),T8 char(3))')
   except:
       print()
   z1 = (id, t1.upper(), t2.upper(), t3.upper(), t4.upper(), t5.upper(), t6.upper(), t7.upper(), t8.upper())
   ex1 = 'insert into timeslot values(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
   mc.execute(ex1, z1)
   db.commit()
   print('Your id is :', id)

def checkbookings():
   print()
   i1 = int(input('Enter user id :'))
   print()
   mc.execute('select * from booking where id=%s', i1)
   r1 = mc.fetchall()
   for i in r1:
       print(i)
   mc.execute('select * from timeslot where id=%s', i1)
   r2 = mc.fetchall()
   for j in r2:
       print(j)

def editbooking():
   print()
   ui = input('Enter user id :')
   print()
   print('1.Edit User information')
   print('2.Edit Ride selections')
   print()
   i2 = int(input('Enter choice number :'))
   print()
   if i2 == 1:
       mc.execute('select * from booking where id=%s', ui)
       for i in mc:
           print(i)
       print('\nName , Age , Height , Phone , Mail ,Day\n')
       while True:
           edit1 = input('Enter key for what you want to change (enter stop for no more changes):')
           if edit1.lower() == 'name':
               n = input('Enter changed name :')
               mc.execute('update booking set name=%s where id=%s', (n, ui))
               db.commit()
           elif edit1.lower() == 'age':
               a = input('Enter age :')
               mc.execute('update booking set age=%s where id=%s', (a, ui))
               db.commit()
           elif edit1.lower() == 'height':
               h = input('Enter changed height')
               mc.execute('update booking set height=%s where id=%s', (h, ui))
               db.commit()
           elif edit1.lower() == 'phone':
               p = input('Enter changed phone number :')
               mc.execute('update booking set phone=%s where id=%s', (p, ui))
               db.commit()
           elif edit1.lower() == 'mail':
               m = input('Enter changed mail :')
               mc.execute('update booking set mail=%s where id=%s', (m, ui))
               db.commit()
           elif edit1.lower() == 'day':
               d = input('Enter other day :')
               mc.execute('update booking set day=%s where id=%s', (d, ui))
               db.commit()
           else:
               break
   elif i2 == 2:
       mc.execute('select * from timeslot where id=%s',ui)
       for i in mc:
           print(i)
       print('T1 , T2 , T3 , T4 , T5 , T6 , T7 ,T8 ')
       while True:
           edit1 = input('Enter key for what you want to change (enter stop for no more changes):')
           if edit1.upper() == 'T1' :
               s1 = input(('Enter ride code for T1:'))
               mc.execute('update timeslot set t1=%s where id=%s', (s1.upper(), ui))
               db.commit()
           elif edit1.upper() == 'T2':
               s2 = input('Enter ride code for T2:')
               mc.execute('update booking set t2=%s where id=%s', (s2.upper(), ui))
               db.commit()
           elif edit1.upper() == 'T3':
               s3 = input('Enter ride code for T3:')
               mc.execute('update booking set t3=%s where id=%s', (s3.upper(), ui))
               db.commit()
           elif edit1.upper() == 'T4':
               s4 = input('Enter ride code for T4:')
               mc.execute('update booking set t4=%s where id=%s', (s4.upper(), ui))
               db.commit()
           elif edit1.upper() == 'T5':
               s5 = input('Enter ride code for T5:')
               mc.execute('update booking set t5=%s where %s', (s5.upper(), ui))
               db.commit()
           elif edit1.upper() == 'T6':
               s6 = input('Enter ride code for T6:')
               mc.execute('update booking set t6=%s where %s', (s6.upper(), ui))
               db.commit()
           elif edit1.upper() == 'T7':
               s7 = input('Enter ride code for T7:')
               mc.execute('update booking set t7=%s where %s', (s7.upper(), ui))
               db.commit()
           elif edit1.upper() == 'T8':
               s8 = input('Enter ride code for T8:')
               mc.execute('update booking set t8=%s where %s', (s8.upper(), ui))
               db.commit()
           else:
               break


def cancelbooking():
   print()
   ui = input('Enter user id :')
   print()
   mc.execute('select * from booking where id=%s', ui)
   for i in mc:
       print(i)
   print()
   de = input('Cancel booking (y/n):')
   if de in ('nN'):
       print()
   else:
       mc.execute('delete from booking where id=%s', ui)
       db.commit()
       mc.execute('delete from timeslot where id=%s', ui)
       db.commit()


def generatebill():
   print()
   ui = input('Enter user id :')
   s = 0
   p1 = 100
   p2 = 100
   p3 = 100
   p4 = 100
   p5 = 100
   p6 = 100
   p7 = 100
   p8 = 100
   p9 = 100
   p10 = 100
   print()
   mc.execute('select * from timeslot where id=%s', ui)
   r = mc.fetchall()
   for j in r:
       for i in j:
           if i == 'R1':
               s += p1
           elif i == 'R2':
               s += p2
           elif i == 'R3':
               s += p3
           elif i == 'R4':
               s += p4
           elif i == 'R5':
               s += p5
           elif i == 'R6':
               s += p6
           elif i == 'R7':
               s += p7
           elif i == 'R8':
               s += p8
           elif i == 'R9':
               s += p9
           elif i == 'R10':
               s += p10
   print('Your Total Bill is :', s)


def AdminLoginPrint():
   print('*' * 155)
   print('Admin Menu                 '.center(155))
   print('1. Check Scheduled Bookings'.center(155))
   print('2. View customer details   '.center(155))
   print('3. Edit booking            '.center(155))
   print('4. Clear System            '.center(155))
   print('5. Back to main menu       '.center(155))
   print('6. Exit                    '.center(155))
   print("*" * 155)
def AdminLogin():
   print()
   AdminLoginPrint()
   while True:
       print()
       i = input("Enter Choice No. :")
       if i == "1":
           SchBookings()
           print()
           AdminLoginPrint()
       elif i == '2':
           checkbookings()
           print()
           AdminLoginPrint()
       elif i == '3':
           editbooking()
           print()
           AdminLoginPrint()
       elif i=='4' :
           ClearSystem()
           print()
           AdminLoginPrint()
       elif i == '5':
           MainMenu()
           print()
           AdminLoginPrint()
       elif i == '6':
           break
       else:
           print("Enter a valid option")


def SchBookings():
   mc.execute('select * from booking')
   r3 = mc.fetchall()
   for i in r3:
       print(i)
def ClearSystem():
   mc.execute('delete from booking')
   db.commit()
   mc.execute('delete from timeslot')
   db.commit()

#mc.execute('drop tables booking')
#mc.execute('drop table timeslot')
#mc.execute('show tables')

# mc.execute()

MainMenu()