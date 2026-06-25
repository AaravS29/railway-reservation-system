import pymysql
import sys
# NDLS,ALJN,ETW,CNB,LKO
#password = input("Enter your mysql PASSWORD here :- ")
db=pymysql.connect(host="localhost",user="root",password="Mysql@1234")
cur=db.cursor()
cur.execute("create database IF NOT EXISTS railway_reservation;")
cur.execute("use  railway_reservation;")
cur.execute("create table IF NOT EXISTS users_information(user_name varchar (20)  , password varchar (10), name varchar (20));")
cur.execute("create table IF NOT EXISTS train_information(train_Code varchar (20), train_name varchar (20) , Route_number varchar (100) , Trains_speed varchar (100), AC_1  varchar (100) ,AC_2 varchar (100) ,AC_3 varchar (100), gerneral varchar (100) ); ")
cur.execute("create table IF NOT EXISTS Route(Route varchar (10) , Stations_Code varchar (100) , Time_duration varchar (100));")
cur.execute("create table IF NOT EXISTS booking(Station_from varchar (20) , station_to varchar (20) , date_time date);" )
cur.execute("create table IF NOT EXISTS Price(Train_Code varchar (20) ,AC_1_price  varchar (100) ,AC_2_price varchar (100) ,AC_3_price varchar (100) ,general_price varchar (100));")
def station():
    cur.execute("create table If not exists stations_details(Sno varchar (100) NOT NULL, Stations_Name  varchar (10),Stations_Code varchar (10) , Route integer (10), Distance varchar (20), PRIMARY KEY (Sno));")
    cur.execute("select * from stations_details")
    a = cur.fetchall()
    b = ()
    if a == b:
        cur.execute("insert into stations_details values('1','New Delhi' ,'NDLS',0,'0');")
        cur.execute("insert into stations_details values('2','Aligarh' ,'ALJN',1,'129');")
        cur.execute("insert into stations_details values('3','Etawah' ,'ETW',2,'299');")
        cur.execute("insert into stations_details values('4','Kanpur' ,'CNB',3,'437');")
        cur.execute("insert into stations_details values('5','Lucknow' ,'LKO',4,'511');")
        cur.execute("insert into Route values('1','NDLS,ALJN,ETW,CNB,LKO','6');")
        db.commit()
station()
# all the code to display the start
# to print -----***---
def lines():
    print(
        "--------------*********-------------********-------------*******------------------********----------------------********---------------******-------****----------")
def start():
    a = """

  ____       _      ___   _      __        __     _     __   __       ____    _____   ____    _____   ____   __     __     _      _____   ___    ___    _   _
 |  _ \     / \    |_ _| | |     \ \      / /    / \    \ \ / /      |  _ \  | ____| / ___|  | ____| |  _ \  \ \   / /    / \    |_   _| |_ _|  / _ \  | \ | | 
 | |_) |   / _ \    | |  | |      \ \ /\ / /    / _ \    \ V /       | |_) | |  _|   \___ \  |  _|   | |_) |  \ \ / /    / _ \     | |    | |  | | | | |  \| |
 |  _ <   / ___ \   | |  | |___    \ V  V /    / ___ \    | |        |  _ <  | |___   ___) | | |___  |  _ <    \ V /    / ___ \    | |    | |  | |_| | | |\  |
 |_| \_\ /_/   \_\ |___| |_____|    \_/\_/    /_/   \_\   |_|        |_| \_\ |_____| |____/  |_____| |_| \_\    \_/    /_/   \_\   |_|   |___|  \___/  |_| \_|

        """
    print(a)
    print("     Welcome To Railway Reservation")
    print(" ")
    print("     1. Log in ")
    print(" ")
    print("     2. Register")
    print(" ")
    print("     3. Developer Mode")
    print(" ")
    print("     4. Exist the program ")
    print(" ")
    while True:
        selection = input('Press the number to select from the option :- ')
        if selection == "1":
            lines()
            Log_in()
        elif selection == "2":
            lines()
            register()
        elif selection == "3":
            lines()
            Developer_Mode()
        elif selection == "4":
            lines()
            sys.exit()
        else:
            print("Enter the values from the option above")
# make table borders
'''
make_table_symbol = "|"
def make_table(b):
    c = make_table_symbol + " " + b + " "
    return c
def add(b):
    b = b+4
    d = b * "-"
    print(d)
'''
# Log in screen
def Log_in():
    cur.execute("select * from users_information;")
    a = cur.fetchall()
    b = ()
    if a == b:
        print("There is no account here please register Yourself first")
        register()
    else:
        while True:
            print("\n")
            print("Please Enter your Username And Password Here:-")
            print("\n ")
            user_name = input("  Enter your Username :- ")
            print(" ")
            password = input("  Enter your password here :- ")
            for i in a:
                if i[0] == user_name:
                    if i[1] == password:
                        print("\n")
                        print("                               Login Successful!             ")
                        print("\n")
                        lines()
                        print("\n\n")
                        welcome = """
                        1. Change your Details\n
                        2. Deleted Your account\n
                        3. PNR Status \n 
                        4. Book Tricket \n 
                        5. Log out \n
                        6. Exit The program \n
                        """
                        while True:
                            print('Welcome', i[2],'To the Railway Reservation \n\n',welcome)
                            selection = input('Press the number to select from the option :- ')
                            if  selection == "1":
                                users(user_name)
                                while True:
                                    print("Notes:- You can only change your name and password")
                                    column = input("Enter the column to modify:-")
                                    if column == "user name" or column == "USER NAME" or column == "User Name":
                                        To = input("To :-")
                                        a = "UPDATE users_information SET name = %s where user_name = %s;"
                                        cur.execute(a, (To, user_name))
                                        db.commit()
                                        lines()
                                        users(user_name)
                                        break
                                    elif column == "Password" or column == "PASSWORD" or column == "PASSWORD":
                                        To = input("To :-")
                                        a = "UPDATE users_information SET password = %s where user_name = %s;"
                                        cur.execute(a, (To, user_name))
                                        db.commit()
                                        lines()
                                        users(user_name)
                                        break
                                    else:
                                        print("incorrect enter correct value!!")
                                print("Done!")
                                continue
                            elif selection == "2":
                                options = input("Are you sure to deleted your account")
                                if options == "yes" or options == "YES" or options =="Yes":
                                    cur.execute("delete from users_information where user_name = %s;",(user_name))
                                    db.commit()
                                    print("\n    successfully deleted your account!!    \n")
                                    lines()
                                    start()
                                else:
                                    break
                            elif selection == "3":
                                lines()
                            elif selection == "4":
                                lines()
                                booking()
                            elif selection == "5":
                                print("successfully logout")
                                lines()
                                start()
                            elif selection == "6":
                                lines()
                                sys.exit()
                            else:
                                print("Enter the values from the option above")
            print("\n Password or User name is incorrect \n")

def dash():
    a = "-"
    return a
def pipe():
    a = "|"
    return a
def booking():
    a = """
                                            Welcome To The Booking Area. 

                                                                                                                   -------------------------------
     * To Enter The Station Name Enter There Station Code.                                                         |       Station Names         |                                                  
                                                                                                                   -------------------------------
                                Routes:-                                                                           |       New Delhi (NDLS)      |
                                                                                                                   |       Aligarh   (ALJN)      |
    NEW DELHI ---->  Aligarh -----> Etawah ----> Kanpur -----> LUCKNOW                                             |       Etawah    (ETW)       |  
                                or                                                                                 |       Kanpur    (CNB)       | 
    LUCKNOW -----> Kanpur ---> Etawah ----> Aligarh ------> NEW DELHI                                              |       Lucknow   (LKO)       |                                                                       
                                                                                                                   -------------------------------

    """
    print(a)
    From = input("   1.From :- ")
    print(" ")
    To = input("   2.To :- ")
    print(" ")
    Date = input("   3.Date of the travel :- ")
    print(" ")
    Month = input(   "4.Month of the travel :- ")
    print(" ")
    year = input("   5.Year of the travel :- ")
    Date = Date +"-"+ Month +"-"+  year
    print(" ")
    options = input("Press space and then enter to Search:- ")
    if options  == "1":
        cur.execute("select * from stations_details;")
        e = cur.fetchall()
        for i in e:
            if From in i:
                Station_to_value = i[3]
                Station_to_distance = i[4]
            if To in i:
                Station_From_value = i[3]
                Station_From_distance = i[4]
        value = int(Station_to_value)- int(Station_From_value)
        distance = int(Station_to_distance) - int(Station_From_distance)
        cur.execute("select * from Route;")
        a = cur.fetchall()
        for i in a:
            if To in i[1] and From in i[1] :
                route = i[0]
        cur.execute("select * from train_information")
        f = cur.fetchall()
        Train_code = []
        for i in f:
            if route in i:
                Train_code.append(i[0])
        j = -1
        l = []
        for g in Train_code:
            j +=1
            l.append(j)
            Trains_display(j,g,Date,distance,value,To,From)
            print(" \n\n\n\n")
        a = """
        1.Press this number to Search the train
        2.Press this to Exit This
        """
        print(a)
        selection = input("Enter here :-")
        if selection == "1":
            selection = input("\n\n Enter the number for the Train to search \n\n")
            if int(selection) in l:
                Train_code = Train_code[int(selection)-1]
                booking_train(Train_code,distance,value)
            else:
                print("\n please enter again \n")
        elif selection == "2":
            lines()
            start()
        else:
            print("\n please enter again \n")
    else:
        lines()
        Log_in()
def booking_train(Train_code,distance,e):
    print("\n\n")
    print("NOTE :- Price give below is per Tricket !!!")
    print("\n\n")
    if e < 0:
        distance = str(distance)
        distance = distance[1:]
        distance = int(distance)
    cur.execute(
        "select Train_Code , AC_1_price * %s , AC_2_price * %s, AC_3_price * %s, General_price * %s from price  where Train_Code = %s;",
        (distance, distance, distance, distance, Train_code))
    value = cur.fetchall()
    print(dash() * 117)
    print(
        pipe() + pipe() + "   Train Code        " + pipe() + pipe() + "     AC-1 Price      " + pipe() + pipe() + "     AC-2 Price      " + pipe() + pipe() + "     AC-3 Price      " + pipe() + pipe() + "      General        " + pipe() + pipe())
    print(dash() * 117)
    for i in value:
        b1 = str(i[0])
        b2 = str(i[1])
        b3 = str(i[2])
        b4 = str(i[3])
        b5 = str(i[4])
        e = "                     "
        a1 = int((len(e) - len(b1)) / 2) * " "
        a2 = int((len(e) - len(b2)) / 2) * " "
        a3 = int((len(e) - len(b3)) / 2) * " "
        a4 = int((len(e) - len(b4)) / 2) * " "
        a5 = int((len(e) - len(b5)) / 2) * " "
        if len(b1) % 2 == 0:
            b1 = b1 + " "
        if len(b2) % 2 == 0:
            b2 = b2 + " "
        if len(b3) % 2 == 0:
            b3 = b3 + " "
        if len(b4) % 2 == 0:
            b4 = b4 + " "
        if len(b5) % 2 == 0:
            b5 = b5 + " "
        print(
            pipe() + pipe() + a1 + b1 + a1 + pipe() + pipe() + a2 + b2 + a2 + pipe() + pipe() + a3 + b3 + a3 + pipe() + pipe() + a4 + b4 + a4 + pipe() + pipe() + a5 + b5 + a5 + pipe() + pipe())
    print(dash() * 117)
    print("\n\n")
    selection = input("Enter Yes to continue")
    if selection == "YES" or selection == "Yes" or selection == "yes":
        classes = input("1. which Class you want ? :-")
        Ticket  = input("2. How many ticket do you want? :- ")
        print("\n\n")



def Trains_display(j,g,date,distance,value,Station_to,Station_from):
    cur.execute("select Train_name from train_information where train_Code = %s;",g)
    Trains_name = cur.fetchall()
    Trains_name = Trains_name[0][0]
    cur.execute("select Trains_speed from train_information where train_Code = %s;", g)
    Trains_speed = cur.fetchall()
    Trains_speed = int(Trains_speed[0][0])
    if value > 0:
        final_times = int(distance) / Trains_speed
        o = type(0.1)
        if type(final_times) == o  and int(final_times) < 1:
            final_times = final_times * 60
            final_times = int(final_times)
            final_times =str(final_times)
            duration = final_times +" min "
            time_start = "12:00"
            if len(final_times) == 2:
                final_times = "12:"+ str(final_times)
            else:
                final_times = "12:" + final_times
        else:
            final_times = int(final_times)
            final_times = str(final_times)
            duration = final_times
            time_start = "12:00"
            if len(final_times) == 2:
                final_times = "1" + final_times + ":00"
            else:
                final_times = str(int(final_times) + 12)
                final_times = final_times + ":00"
    else:
        distance = str(distance)
        distance = distance[1:]
        final_times = int(distance) / Trains_speed
        o = type(0.1)
        if type(final_times) == o  and int(final_times) < 1:
            final_times = final_times * 60
            final_times = int(final_times)
            final_times =str(final_times)
            duration = final_times +"minutes"
            time_start = "00:00"
            if len(final_times) == 2:
                final_times = "00:" + final_times
            else:
                final_times = "00:" + final_times
        else:
            final_times = int(final_times)
            final_times = str(final_times)
            duration = final_times
            time_start = "00:00"
            if len(final_times) == 2:
                final_times = final_times + ":00"
            else:
                final_times = "0" + final_times + ":00"

    # spaces
    space = "                                                                                                    "
    a1 = "To book The tickets and More details about the Seats and Coaches Press "
    b1 = "                "
    b2 = "       "
    # all the space
    Trains_name1 = int((len(space) - (len(Trains_name)+len("                  ") + len(g))) / 2) * " "
    c1 = int((len(space) - (len(time_start)+len("        ")+len(Station_from)+len("      ")+len(date)+len("      ")+len("----")+len(final_times)+len("----")+len("          ")+len(final_times)+len("       ")+len(Station_to)+len("      ")+len(date)))/ 2) * " "
    # if
    if len(Trains_name) % 2 == 0:
        Trains_name = Trains_name + " "
    # this actual screen print
    print(" ")
    print(" ")
    print("                            ",dash()*104,"\n")
    print("                            ","||"+Trains_name1+str(Trains_name) +"                  "+str(g)+Trains_name1+"||","\n")
    print("                            ",dash()*104,"\n")
    print("                            ","||"+c1+time_start+"        "+Station_from+"      "+date+"      "+"----"+duration+"----"+"         "+final_times+"      "+Station_to+"       1"
                                                                                                                                                                                "1"
                                                                                                                                                                                "   "+date+c1 +"||","\n")
    print("                            ",dash()*104,"\n")
    print("                            ","||",b1,a1,j,b2,"||","\n")
    print("                            ",dash()*104)
    print("")
    print("")
# add details to the Stations
# create new log in
def register():
    print(" ")
    print("                 Please Enter The Details For The Registration Process.             ")
    print(" ")
    user_name = input("   1. User Name :-  ")
    name = input("   2. Name :- ")
    while True:
        password = input("   3. Password :-   ")
        confirm_password = input("   4. Confirm Password :-  ")
        if confirm_password == password:
            break
        else:
            print("Password and Confirm password not Matched. ")
    cur.execute("insert into users_information values(%s, %s,%s)",(user_name,password,name))
    db.commit()
    print(" ")
    print("SUCCESSFUL DONE THE REGISTRATION!!!")
    print(" ")
    a = """ 
            1. To Go Back To Main Page 
            2. Exit The program
        """
    print(a)
    while True:
        selection = input('Press the number to select from the option :- ')
        if selection == "1":
            lines()
            start()
        elif selection == "2":
            lines()
            sys.exit()
        else:
            print("Enter the values from the option above")
# developer Mode
def welcome_screen_dev():
    print("Options to Edit :-")
    print("   1. Trains Details")
    print("   2. Users Details")
    print("   3. Stations Details")
    print("   4. Prices Details")
    a = """   5. To Go Back To Main Page
   6. Exit The program
            """
    print(a)

def Developer_Mode():
    while True:
        print("")
        username = input("Enter your developer User Id :- ")
        print("")
        password = input("Enter your password here :- ")
        if username == "Railway":
            if password == "1234":
                devleoper()
        else:
            print("Password Is Incorrect. Please Try Again")
def devleoper():
    print(" \n Welcome User To the developer Mode \n ")
    while True:
        welcome_screen_dev()
        selection = input('Press the number to select from the option :- ')
        if selection == "1":
            lines()
            train_details()
            Trains_welcome()
        elif selection == "2":
            lines()
            User_details()
        elif selection == "3":
            lines()
            Station_details()
            station_welcome()
        elif selection == "4":
            lines()
            Price_details()
            Price_welcome()
        elif selection == "5":
            lines()
            start()
        elif selection == "6":
            lines()
            sys.exit()
        else:
            print("Enter the values from the option above")
def Price_details():
    print("\n                                                    PRICES DETAILS                    \n")
    cur.execute("select * from price;")
    value = cur.fetchall()
    print(dash() * 117)
    print(
        pipe() + pipe() + "   Train Code        " + pipe() + pipe() + "     AC-1 Price      " + pipe() + pipe() + "     AC-2 Price      " + pipe() + pipe()+ "     AC-3 Price      " + pipe() + pipe() + "      General        "+ pipe()+pipe())
    print(dash() * 117)
    for i in value:
        b1 = str(i[0])
        b2 = str(i[1])
        b3 = str(i[2])
        b4 = str(i[3])
        b5 = str(i[4])
        e = "                     "
        a1 = int((len(e) - len(b1)) / 2) * " "
        a2 = int((len(e) - len(b2)) / 2) * " "
        a3 = int((len(e) - len(b3)) / 2) * " "
        a4 = int((len(e) - len(b4)) / 2) * " "
        a5 = int((len(e) - len(b5)) / 2) * " "
        if len(b1) % 2 == 0:
            b1 = b1 + " "
        if len(b2) % 2 == 0:
            b2 = b2 + " "
        if len(b3) % 2 == 0:
            b3 = b3 + " "
        if len(b4) % 2 == 0:
            b4 = b4 + " "
        if len(b5) % 2 == 0:
            b5 = b5 + " "
        print(
            pipe() + pipe() + a1 + b1 + a1 + pipe() + pipe() + a2 + b2 + a2 + pipe() + pipe() + a3 + b3 + a3 + pipe() + pipe() + a4 + b4 + a4 + pipe() + pipe()+ a5 + b5 + a5 + pipe() + pipe())
    print(dash() * 117)
def User_details():
    print("\n                                                    USER DETAILS                    \n")
    cur.execute("select * from users_information;")
    value = cur.fetchall()
    print(dash()*71)
    print(pipe()+pipe()+"    User ID          "+pipe()+pipe()+"    Password         "+pipe()+pipe()+"    User Name        "+pipe()+pipe())
    print(dash() * 71)
    for i in value:
        b1 = str(i[0])
        b2 = str(i[1])
        b3 = str(i[2])
        e = "                     "
        a1 = int((len(e) - len(b1))/2) * " "
        a2 = int((len(e) - len(b2)) / 2) * " "
        a3 = int((len(e) - len(b3)) / 2) * " "
        if len(b1) % 2 == 0:
            b1 = b1 + " "
        if len(b2) % 2 == 0:
            b2 = b2+ " "
        if len(b3) % 2 == 0:
            b3 = b3+ " "
        print(pipe()+pipe()+a1+b1+a1+pipe()+pipe()+a2+b2+a2+pipe()+pipe()+a3+b3+a3+pipe()+pipe())
    print(dash() * 71)
    a = """
    1. Go back to Developer Mode
    2. Log out
    3. Exit The code
    """
    print(a)
    while True:
        selection = input('Press the number to select from the option :- ')
        if selection == "1":
            lines()
            devleoper()
        elif selection == "2":
            print("\nsuccessfully logout\n")
            lines()
            start()
        elif selection == "3":
            sys.exit()
        else:
            print("Enter the values from the option above")
def Station_details():
    print("\n                                                  STATIONS DETAILS                   \n")
    cur.execute("select * from stations_details;")
    value = cur.fetchall()
    print(dash() * 95)
    print(pipe()+pipe()+"          Sno        "+pipe()+pipe()+"   Stations Name     "+pipe()+pipe()+"    Stations Code    "+pipe()+pipe()+"      Route          "+pipe()+pipe())
    print(dash() * 95)
    for i in value:
        b1 = str(i[0])
        b2 = str(i[1])
        b3 = str(i[2])
        b4 = str(i[3])
        e = "                     "
        a1 = int((len(e) - len(b1))/2) * " "
        a2 = int((len(e) - len(b2)) / 2) * " "
        a3 = int((len(e) - len(b3)) / 2) * " "
        a4 = int((len(e) - len(b4)) / 2) * " "
        if len(b1) % 2 == 0:
            b1 = b1 + " "
        if len(b2) % 2 == 0:
            b2 = b2+ " "
        if len(b3) % 2 == 0:
            b3 = b3+ " "
        if len(b4) % 2 == 0:
            b4 = b4 + " "
        print(pipe()+pipe()+a1+b1+a1+pipe()+pipe()+a2+b2+a2+pipe()+pipe()+a3+b3+a3+pipe()+pipe()+a4+b4+a4+pipe()+pipe())
    print(dash() * 95)
def Price_welcome():
    a = """
       1. Edit The Table
       2. Go back to Developer Mode
       3. Log out
       4. Exit The code
       """
    while True:
        print(a)
        selection = input('Press the number to select from the option :- ')
        if selection == "1":
            while True:
                lines()
                Price_details()
                a = """
                   1. Modify In the Table
                   2. Deleted Records
                   3. Create Records
                   4. To Developer Mode 
                   5. Log out
                   """
                print(a)
                while True:
                    selection = input('Press the number to select from the option :- ')
                    if selection == "1":
                        Modify_Prices()
                        lines()
                        break
                    elif selection == "2":
                        deletion_Prices()
                        lines()
                        break
                    elif selection == "3":
                        creations_Prices()
                        break
                    elif selection == "4":
                        lines()
                        print("\n")
                        devleoper()
                    elif selection == "5":
                        lines()
                        print("\nsuccessfully logout\n")
                        lines()
                        start()
                    else:
                        print("Enter the values from the option above")
        elif selection == "2":
            lines()
            print("\n")
            devleoper()
        elif selection == "3":
            lines()
            print("\nsuccessfully logout\n")
            lines()
            start()
        elif selection == "4":
            sys.exit()
        else:
            print("Enter the values from the option above")
def station_welcome():
    a = """
    1. Edit The Table
    2. Go back to Developer Mode
    3. Log out
    4. Exit The code
    """
    while True:
        print(a)
        selection = input('Press the number to select from the option :- ')
        if selection == "1":
            while True:
                lines()
                Station_details()
                a = """
                1. Modify In the Table
                2. Deleted Records
                3. Create Records
                4. To Developer Mode 
                5. Log out
                """
                print(a)
                while True:
                    selection = input('Press the number to select from the option :- ')
                    if selection == "1":
                        Modify_table_stations()
                        lines()
                        break
                    elif selection == "2":
                        deletion_stations()
                        lines()
                        break
                    elif selection == "3":
                        creations_Stations()
                        break
                    elif selection == "4":
                        lines()
                        print("\n")
                        devleoper()
                    elif selection == "5":
                        lines()
                        print("\nsuccessfully logout\n")
                        lines()
                        start()
                    else:
                        print("Enter the values from the option above")
        elif selection == "2":
            lines()
            print("\n")
            devleoper()
        elif selection == "3":
            lines()
            print("\nsuccessfully logout\n")
            lines()
            start()
        elif selection == "4":
            sys.exit()
        else:
            print("Enter the values from the option above")
# program start from here
def Trains_welcome():
    a = """
    1. Edit The Table
    2. Go back to Developer Mode
    3. Log out
    4. Exit The code
    """
    while True:
        print(a)
        selection = input('Press the number to select from the option :- ')
        if selection == "1":
            while True:
                lines()
                train_details()
                a = """
                1. Modify In the Table
                2. Deleted Records
                3. Create Records
                4. To Developer Mode 
                5. Log out
                """
                while True:
                    print(a)
                    selection = input('Press the number to select from the option :- ')
                    if selection == "1":
                        Modify_table_Trains()
                        lines()
                        break
                    elif selection == "2":
                        deletion_trains()
                        lines()
                        break
                    elif selection == "3":
                        creations_Trains()
                        break
                    elif selection == "4":
                        lines()
                        print("\n")
                        devleoper()
                    elif selection == "5":
                        lines()
                        print("\nsuccessfully logout\n")
                        lines()
                        start()
                    else:
                        print("Enter the values from the option above")
        elif selection == "2":
            lines()
            print("\n")
            devleoper()
        elif selection == "3":
            lines()
            print("\nsuccessfully logout\n")
            lines()
            start()
        elif selection == "4":
            sys.exit()
        else:
            print("Enter the values from the option above")
def Modify_Prices():
    while True:
        Sno = input("Enter the Code value of the record to be modify :-")
        column = input("Enter the column:-")
        To = input("To :-")
        print("NOTE :- you can't modify the Train Code")
        if column == "AC-1 Price" or column == "AC-1 PRICE" or column == "ac-1 price":
            a = "UPDATE stations_details SET AC_1_price = %s where Train_Code = %s;"
            cur.execute(a, (To, Sno))
            db.commit()
            break
        elif column == "AC-2 Price" or column == "AC-2 PRICE" or column == "ac-2 price":
            a = "UPDATE stations_details SET AC_2_price = %s where Train_Code = %s;"
            cur.execute(a, (To, Sno))
            db.commit()
            break
        elif column == "General Price" or column == "GENERAL PRICE" or column == "general price":
            a = "UPDATE stations_details SET general_price = %s where Train_Code = %s;"
            cur.execute(a, (To, Sno))
            db.commit()
            break
        else:
            print("incorrect enter correct value!!")
    print("Done!")
def Modify_table_stations():
    while True:
        Sno = input("Enter the Sno value of the record to be modify :-")
        column = input("Enter the column:-")
        To = input("To :-")
        if column == "Route" or column == "STATIONS NAME" or column == "stations name":
            a = "UPDATE stations_details SET Stations_name = %s where Sno = %s;"
            cur.execute(a, (To, Sno))
            db.commit()
            break
        elif column == "Stations Code" or column == "STATIONS CODE" or column == "stations code":
            a = "UPDATE stations_details SET Stations_Code = %s where Sno = %s;"
            cur.execute(a, (To, Sno))
            db.commit()
            break
        elif column == "Route" or column == "ROUTE" or column == "route":
            a = "UPDATE stations_details SET Route = %s where Sno = %s;"
            cur.execute(a, (To, Sno))
            db.commit()
            break
        else:
            print("incorrect enter correct value!!")
    print("Done!")
def Modify_table_Trains():
    while True:
        column = input("Enter the column:-")
        if column == "Train Code" or column == "TRAIN CODE" or column == "train code":
            Code = input("Enter Train Name of the record to be modify ")
            To = input("To :-")
            a = "UPDATE train_information SET train_Code = %s where train_name = %s;"
            cur.execute(a, (To, Code))
            db.commit()
            break
        elif column == "Route No" or column == "ROUTE NO" or column == "route no":
            Code = input("Enter the Train Code of the record to be modify :-")
            To = input("To :-")
            a = "UPDATE train_information SET Route_number = %s where train_Code = %s;"
            cur.execute(a, (To, Code))
            db.commit()
            break
        elif column == "Train Name" or column == "TRAIN NAME" or column == "train name":
            Code = input("Enter the Train Code  of the record to be modify :-")
            To = input("To :-")
            a = "UPDATE train_information SET train_name = %s where train_Code = %s;"
            cur.execute(a, (To, Code))
            db.commit()
            break
        elif column == "Train Speed" or column == "TRAIN SPEED" or column == "train speed":
            Code = input("Enter the Train Code  of the record to be modify :-")
            To = input("To :-")
            a = "UPDATE train_information SET Trains_speed  = %s where train_Code = %s;"
            cur.execute(a, (To, Code))
            db.commit()
            break
        elif column == "AC-1" or column == "Ac-1" or column == "ac-1":
            Code = input("Enter AC-1 of the record to be modify ")
            To = input("To :-")
            a = "UPDATE train_information SET AC_1 = %s where train_name = %s;"
            cur.execute(a, (To, Code))
            db.commit()
            break
        elif column == "AC-2" or column == "Ac-2" or column == "ac-2":
            Code = input("Enter AC-2 of the record to be modify ")
            To = input("To :-")
            a = "UPDATE train_information SET AC_2 = %s where train_name = %s;"
            cur.execute(a, (To, Code))
            db.commit()
            break
        elif column == "AC-3" or column == "Ac-3" or column == "ac-3":
            Code = input("Enter AC-3 of the record to be modify ")
            To = input("To :-")
            a = "UPDATE train_information SET AC_3 = %s where train_name = %s;"
            cur.execute(a, (To, Code))
            db.commit()
            break
        elif column == "General" or column == "general" or column == "GENERAL":
            Code = input("Enter General of the record to be modify ")
            To = input("To :-")
            a = "UPDATE train_information SET gerneral = %s where train_name = %s;"
            cur.execute(a, (To, Code))
            db.commit()
            break
        else:
            print("incorrect enter correct value!!")
    print("Done!")
def deletion_stations():
    Sno = input("Enter the Sno value of the record to be REMOVED :-")
    a = "delete from stations_details where Sno = %s;"
    cur.execute(a, (Sno))
    db.commit()
    print("done")
def deletion_trains():
    Code = input("Enter the train code value of the record to be REMOVED :-")
    a = "delete from train_information where train_Code = %s;"
    cur.execute(a, (Code))
    db.commit()
    print("done")
def deletion_Prices():
    Code = input("Enter the train code value of the record to be REMOVED :-")
    a = "delete from price where Train_Code = %s;"
    cur.execute(a, (Code))
    db.commit()
    print("done")

def creations_Stations():
    Sno = input("   1. Sno")
    Stations_name = input("   2. Station Name:-  ")
    Station_code = input("   3. Station Code :- ")
    Route = input("   4. Route :- ")
    cur.execute("insert into stations_details values(%s, %s,%s,%s)", (Sno,Stations_name,Station_code,Route))
    db.commit()
    print("done!")
def creations_Prices():
    Stations_code = input("   2. Station Code:-  ")
    Station_AC_1 = input("   3. Price for AC-1 :- ")
    Station_AC_2 = input("   3. Price for AC-2 :- ")
    Station_AC_3 = input("   3. Price for AC-3 :- ")
    Station_general = input("   3. Price for General :- ")
    cur.execute("insert into price values(%s,%s,%s,%s,%s)", (Stations_code,Station_AC_1,Station_AC_2,Station_AC_3,Station_general))
    db.commit()
    print("done!")
def creations_Trains():
    Code = input("   2. Trains Code")
    Trains_name = input("   3. Trains Name:-  ")
    Route_number = input("   4. Route No :- ")
    Speed = input("   4. Speed of the Train :-")
    Ac_1 = input("   2. No of Seat in AC-1 :-")
    Ac_2 = input("   2. No of Seat in AC-2 :-")
    Ac_3 = input("   2. No of Seat in AC-3 :-")
    Ac_4 = input("   2. No of Seat in General :-")
    cur.execute("insert into train_information values(%s, %s,%s,%s,%s, %s,%s,%s)", (Code,Trains_name,Route_number,Speed,Ac_3,Ac_2,Ac_4,Ac_1))
    db.commit()
    print("done!")
def train_details():
    print("\n                                                  Trains DETAILS                   \n")
    cur.execute("select * from Train_information;")
    value = cur.fetchall()
    print(dash() * 96*2)
    print(
        pipe() + pipe() + "       Train Code    " + pipe() + pipe() + "     Trains Name     " + pipe() + pipe() + "       Route No      " + pipe() + pipe()  + "   Speed Of Train    " + pipe() + pipe()  + "         AC-1        " + pipe() + pipe()+  "        AC-2         " + pipe() + pipe()  + "        AC-3         " + pipe() + pipe()+"       General       " + pipe() + pipe())
    print(dash() * 96*2)
    for i in value:
        b1 = str(i[0])
        b2 = str(i[1])
        b3 = str(i[2])
        b4 = str(i[3])
        b5 = str(i[4])
        b6 = str(i[5])
        b7 = str(i[6])
        b8 = str(i[7])
        e = "                     "
        a1 = int((len(e) - len(b1)) / 2) * " "
        a2 = int((len(e) - len(b2)) / 2) * " "
        a3 = int((len(e) - len(b3)) / 2) * " "
        a4 = int((len(e) - len(b4)) / 2) * " "
        a5 = int((len(e) - len(b5)) / 2) * " "
        a6 = int((len(e) - len(b6)) / 2) * " "
        a7 = int((len(e) - len(b7)) / 2) * " "
        a8 = int((len(e) - len(b8)) / 2) * " "
        if len(b1) % 2 == 0:
            b1 = b1 + " "
        if len(b2) % 2 == 0:
            b2 = b2 + " "
        if len(b3) % 2 == 0:
            b3 = b3 + " "
        if len(b4) % 2 == 0:
            b4 = b4 + " "
        if len(b5) % 2 == 0:
            b5 = b5 + " "
        if len(b6) % 2 == 0:
            b6 = b6 + " "
        if len(b7) % 2 == 0:
            b7 = b7 + " "
        if len(b8) % 2 == 0:
            b8 = b8 + " "
        print(pipe() + pipe() + a1 + b1 + a1 + pipe() + pipe() + a2 + b2 + a2 + pipe() + pipe() + a3 + b3 + a3 + pipe() +pipe()+  a4 + b4 + a4 + pipe() +pipe()+ a5 + b5 + a5 + pipe() + pipe() + a6 + b6 + a6 + pipe() + pipe() + a7 + b7 + a7 + pipe() +pipe()+  a8 + b8 + a8 + pipe() +pipe())
    print(dash() * 96*2)
def users(user):
    print("\n                                                    USER DETAILS                    \n")
    cur.execute("select * from users_information where user_name = %s;",(user))
    value = cur.fetchall()
    print(dash() * 71)
    print(
        pipe() + pipe() + "    User ID          " + pipe() + pipe() + "    Password         " + pipe() + pipe() + "    User Name        " + pipe() + pipe())
    print(dash() * 71)
    for i in value:
        b1 = str(i[0])
        b2 = str(i[1])
        b3 = str(i[2])
        e = "                     "
        a1 = int((len(e) - len(b1)) / 2) * " "
        a2 = int((len(e) - len(b2)) / 2) * " "
        a3 = int((len(e) - len(b3)) / 2) * " "
        if len(b1) % 2 == 0:
            b1 = b1 + " "
        if len(b2) % 2 == 0:
            b2 = b2 + " "
        if len(b3) % 2 == 0:
            b3 = b3 + " "
        print(
            pipe() + pipe() + a1 + b1 + a1 + pipe() + pipe() + a2 + b2 + a2 + pipe() + pipe() + a3 + b3 + a3 + pipe() + pipe())
    print(dash() * 71)
while True:
    start()


