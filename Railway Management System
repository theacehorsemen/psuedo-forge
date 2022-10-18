'''
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='raunak01')
if mydb.is_connected():
    print('Connected Successfully to the Server')
mycur=mydb.cursor()
mycur.execute('create database railway;')
def table_creation_railway():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='raunak01',database='railway')
    cursor=mydb.cursor()
    mydb.autocommit=True
    s1="create table railway(name varchar(100),phno varchar(15)  primary key,age int(4),gender varchar(50),from_f varchar(100),to_t varchar(100),date_d varchar(20))"
    cursor.execute(s1)
table_creation_railway()

def table_creation_user_accounts():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='raunak01',database='railway')
    cursor=mydb.cursor()
    mydb.autocommit=True
    s1="create table user_accounts(fname varchar(100),lname varchar(100),user_name varchar(100) ,password varchar(100) primary key, phno varchar(15),gender varchar(50),dob varchar(50),age varchar(4))"
    cursor.execute(s1)
table_creation_user_accounts()
'''
def menu():
    ch=int(input('WELCOME\nPLEASE SELECT 1(if YES) or 2(if NO) to continue:'))
    while ch==1:
        print('WELECOME TO ONLINE RAILWAY RESERVATION SYSTEM')
        print('Type-in the corresponding numbers to start : \n')
        from tabulate import tabulate
        a=[1,'SIGN IN']
        b=[2,'SIGN UP']
        c=[3,'DELETE ACCOUNT']
        d=[4,'EXIT']
        data=[a,b,c,d]
        print(tabulate(data,headers=['Choice Numbers','Options'],tablefmt='fancy_grid',numalign='center',stralign='left'))
        ch1=int(input('ENTER YOUR CHOICE:'))
        if ch1==1:
            a=signinchecking()
            if a==True:
                print('WELCOME to IRCTC Online Reservation Platform \n')
                print133()
                main()
            else:
                continue
        elif ch1==2:
            a=signupchecking()
            if a==True:
                ("ALL SET UP\n WELCOME to IRCTC Online Reservation Platform")
                print62()
                main()
            else:
                print('PLEASE CHOOSE ANOTHER PASSORD AND TRY AGAIN.')
                continue
        elif ch1==3:
            c=checking_2()
            if c==True:
                print('ACCOUNT DELETED')
                continue
            else:
                print('YOUR PASSWAORD OR USER_NAME IS INCORRECT')
                continue
        elif ch1==4:
            print('THANK YOU')
            print133()
            break
        else:
            print('ERROR 404:PAGE NOT FOUND')
            print62()
            break
        main()

def print133():
    print("*-"*133)
def print62():
    print('_-'*62)

def main():
    print('1.yes')
    print('2.no')
    c=int(input("do you want to continue or not:"))
    while (c==1):
        from tabulate import tabulate
        a=[1,'TICKET BOOKING']
        b=[2,'TICKET CHECKING']
        c=[3,'TICKET CANCELLING']
        d=[4,'ACCOUNT DETAILS']
        e=[5,'LOG-OUT']
        table1=[a,b,c,d,e]
        print(tabulate(table1,headers=['Choice Numbers','Options'],tablefmt='fancy_grid',numalign='center',stralign='left'))
        ch=int(input('enter ur choice:'))
        if ch==1:
            ticket_booking()
        elif ch==2:
            ticket_checking()
        elif ch==3:
            ticket_cancelling()
        elif ch==4:
            accountchecking()
        elif ch==5:
            print('THANK YOU')
            break
        else:
            print('WRONG INPUT')
        
def signinchecking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='raunak01',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        c1="select fname,lname from user_accounts where password='{}'".format(b)
        cursor.execute(c1)
        data1=cursor.fetchall()[0]
        data1=list(data1)
        data1=data1[0]+' '+data1[1]
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)[0]
        if data==a:
            print('Hello',data1)
            return True
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')
from datetime import date
def calculateAge(birthDate):
    today = date.today()
    age = today.year-birthDate.year-((today.month, today.day)<(birthDate.month, birthDate.day))
    age1=str(age)
    return age

def signupchecking():#function for making a new account from scratch 
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='raunak01',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    f=input("FIRST NAME:")
    l=input("LAST NAME:")
    name=f+" "+l
    a=input('USER NAME:')
    b=input('PASS WORD:')
    c=input('RE-ENTER YOUR PASS WORD:')
    for i in range(1):
        ph=str(input("PHONE NUMBER:"))
        if (len(ph)==10):
            if (ph.isnumeric()):
                if ph[0] in ['7','8','9']:
                    print('Valid')
                else:
                    print('Not Valid')
                    menu()
            else:
                print('Not valid')
                menu()
        else:
            print('Not Valid')
            menu()
    print(' M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
    gen=input('ENTER YOUR GENDER:')
    print("ENTER YOR DATE OF BIRTH")
    d=input("DD:")
    o=input("MM:")
    p=input("YYYY:")
    dob=d+'/'+o+'/'+p
    age=calculateAge(date(int(p),int(o),int(d)))
    print('You are',age,'years old')
    v={'m':'MALE','f':'FEMALE','n':'NOT TO MENTION'}
    if b==c:
        try:
            c1="insert into user_accounts values('{}','{}','{}','{}','{}','{}','{}','{}')".format(f,l,a,b,ph,v[gen],dob,age)
            cursor.execute(c1)
            print('WELCOME',name)
            return True
        except:
            print('PASSWORD ALREADY EXISTS')
            return False
    else:
        print('BOTH PASSWORDS ARE NOT MATCHING')

def checking_2():#deleting a pre-existing account
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='raunak01',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)
        if data[0]==a:
             print('IS THIS YOUR ACCOUNT')
             s1="select user_name from user_accounts where password='{}'".format(b)
             c1="select fname,lname from user_accounts where password='{}'".format(b)
             cursor.execute(c1)
             data1=cursor.fetchall()[0]
             data1=list(data1)
             data1=data1[0]+' '+data1[1]
             cursor.execute(s1)
             data=cursor.fetchall()[0]
             data=list(data)
             if data[0]==a:
                 x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
                 s1="select fname,lname,phno,gender,dob,age from user_accounts where password='{}'".format(b)
                 cursor.execute(s1)
                 data=cursor.fetchall()[0]
                 data=list(data)
                 from tabulate import tabulate
                 a=[x[0],data[0]]
                 b=[x[1],data[1]]
                 c=[x[2],data[2]]
                 d=[x[3],data[3]]
                 e=[x[4],data[4]]
                 f=[x[5],data[5]]
                 data2=[a,b,c,d,e,f]
                 print(tabulate(data2,tablefmt='grid',numalign='center',stralign='left'))
                 print('1.yes')
                 print('2.no')
                 vi=int(input('enter your choice:'))
                 if vi==1:
                     b1="delete from user_accounts where password = '{}'".format(b)
                     cursor.execute(b1)
                     return True
                 elif vi==2:
                     print('SORRY,RETRY(if you want)')
                 else:
                     print('ERROR 404:PAGE NOT FOUND')
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')

def error():
    print('ERROR: You did not mention XXXX Departure of Arrival destination XXXX')
def ticket_booking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='raunak01',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    num=int(input('Enter the number of ticket you would like to reserve: '))
    for i in range(num):
        f_nm=input('Enter first name: ')
        l_nm=input('Enter last name: ')
        nm=f_nm+' '+l_nm
        age=int(input('Enter your age:'))
        for i in range(1):
            print("                                     Make sure the Number you enter is a Valid 10 digit Phone Number\n")
            phno=str(input("Enter Your PHONE NUMBER:"))
            if (len(phno)==10):
                if (phno.isnumeric()):
                    if phno[0] in ['7','8','9']:
                        print('Valid')
                    else:
                        print('Not Valid: REDIRECTING TO THE PORTAL')
                        main()
                else:
                    print('Not valid: REDIRECTING TO THE PORTAL')
                    main()
            else:
                print('Not Valid: REDIRECTING TO THE PORTAL')
                main()
        print(' M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
        gender=input('Enter your gender:')
        Gender=gender.upper()
        from tabulate import tabulate
        b=['*NOTE*']
        a=['Make Sure You enter both the Departure and arrival destination in Proper Sentance Case']
        data=[b,a]
        print(tabulate(data,tablefmt='fancy_grid',numalign='center',stralign='left'))
        print('Want to see all the trains available?\n OR Enter the Destination yourself?')
        print('1. Yes: Want to see all the trains')
        print("2. No: I'll Enter the Destination Myself")
        asja=int(input('Enter the Choice (1/2): '))
        if asja==1:
            s="select * from railwayinfo;"
        elif asja==2:
            global fr
            global to
            fr=input('Enter your Departure destination:')
            to=input('Enter your Arrival destination:')
            s="select * from railwayinfo where from_where='{}' and to_where='{}'".format(fr,to)
        cursor.execute(s)
        recrd=cursor.fetchall()
        sp=''
        head=['Train Name','Train Number','Train From','Train to','Chaircar available','Sleeper available']        
        print(head[0],'\t','\t',head[1],'\t',head[2],'\t',head[3],'\t',head[4],'\t',head[5])
        for j in recrd:
            print(j[0],'\t','\t',j[1],'\t',j[2],'\t',j[3],'\t',j[4],'\t',j[5])
        print('\n')
    #Now when you enter the train number it automatically takes it 'from' and 'to' destination:
        if asja==1:
            train=int(input('Enter the Required train Number from the data available:'))
            strain='select from_where,to_where from railwayinfo where trainno={}'.format(train)
            cursor.execute(strain)
            rec=cursor.fetchall()
            fr=rec[0][0]
            to=rec[0][1]
        elif asja==2:
            train=int(input('Enter the Required train Number from the data available:'))
            strain='select from_where,to_where from railwayinfo where trainno={}'.format(train)
            cursor.execute(strain)
            rec=curson.fetchall()
            fr=rec[0][0]
            to=rec[0][1]
        sha='select cc,sl1 from railwayinfo where trainno={}'.format(train)
        cursor.execute(sha)
        record=cursor.fetchall()
        #allowing users to enter their seating class by themselves(if available)
        print('Select the seating class: \n')
        print('1. Chair car(CC)')
        print('2. Sleeper car (SL1)\n')
        seating=int(input('enter your Choice Number: '))
        if seating==1:
            seat='SLEEPER'
            if record[0][0]==0:
                print('SORRY, LOOKS LIKE ALL THE SEATS IN CHAIR-CAR CATAGORY ARE BOOKED')
                print('RE-DIRECTING TO THE MENU...')
                main()
            elif record[0][0]==0:
                s2="update railwayinfo set cc=cc-1 where trainno={}".format(train)
                cursor.execute(s2)
        elif seating==2:
            seat='CHAIR CAR'
            if record[0][1]==0:
                print('SORRY, LOOKS LIKE ALL THE SEATS IN SLEEPER CATAGORY ARE BOOKED')
                print('RE-DIRECTING TO THE MENU...')
                main()
            elif record[0][1]!=0:
                s3="update railwayinfo set sl1=sl1-1 where trainno={}".format(train)
                cursor.execute(s3)
        print('Date of reservation: ')
        date1=input('Enter date(dd):')
        date2=input('Enter month(mm):')
        date3=input('Enter year(yyyy):')
        date=date1+"/"+date2+"/"+date3
        a={'M':'MALE','F':'FEMALE','N':'NOT TO MENTION'}
        v=a[Gender]
        s1="insert into railway values('{}','{}',{},'{}',{},'{}','{}','{}','{}')".format(nm,phno,age,v,train,seat,fr,to,date)
        cursor.execute(s1)
        print(i+1,'TICKET BEEN BOOKED')
    print('YOUR TICKETS HAVE BEEN BOOKED SUCCESSFULLY')
    print62()
def ticket_cancelling():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='raunak01',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    print('1.yes')
    print('2.no')
    ch=int(input("ARE YOU SURE you want to continue Deleting your TICKET? or not: "))
    if ch==1:
        phno=input('enter your phone number:')
        s1="delete from railway where phno=phno"
        cursor.execute(s1)
        print('YOUR TICKET HAS BEEN CANCELLED')
        print62()
    elif ch==2:
        print('THANK YOU')
        print62()
    else:
        print('ERROR 404:PAGE NOT FOUND')

def ticket_checking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='raunak01',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    print('TYPE IN YOUR CHOICE-->')
    print('1. YES')
    print('2. NO')
    ch=int(input("Do you want to continue CHECKING YOUR PNR STATUS or not:"))

    if ch==1:
        phno=input('Enter your Registered Mobile/Phone number:')
        try:
            s1="select * from railway where phno='{}'".format(phno)
            cursor.execute(s1)
            data=cursor.fetchall()[0]
            Data=list(data)
            a=['NAME','PHONE NUMBER','AGE','GENDER','TRAIN NO','SEAT IN (CLASS)','STARTING POINT','DESTINATION','DATE OF DEPARTURE']
            print('\n')
            print('Following is the PNR Status\n')
            print(a[0],':',Data[0].upper())
            print(a[1],':',Data[1])
            print(a[2],':',Data[2])
            print(a[3],':',Data[3].upper())
            print(a[4],':',Data[4])
            print(a[5],':',Data[5].upper())
            print(a[6],':',Data[6].upper())
            print(a[7],':',Data[7].upper())
            print(a[8],':',Data[8])
        except:
            print('TICKET DOES NOT EXISTS')
    elif ch==2:
        print('THANK YOU')
    elif ch!=2 and ch!=1:
        print('ERROR 404:PAGE NOT FOUND')
    print62()
    
def accountchecking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='raunak01',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        c1="select fname,lname from user_accounts where password='{}'".format(b)
        cursor.execute(c1)
        data1=cursor.fetchall()[0]
        data1=list(data1)
        data1=data1[0]+' '+data1[1]
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)
        if data[0]==a:
            
            x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
            s1="select fname,lname,phno,gender,dob,age from user_accounts where password='{}'".format(b)
            cursor.execute(s1)
            data=cursor.fetchall()[0]
            data=list(data)
            print('\n')
            print("Following are Your IRCTC Account Details: ")
            print('\n')
            print(x[0],':::',data[0])
            print(x[1],':::',data[1])
            print(x[2],':::',data[2])
            print(x[3],':::',data[3])
            print(x[4],':::',data[4])
            print(x[5],':::',data[5],'\n')
            print('If you want To make changes in these parameter, \nDelete your Account and Sign Up with a new Account with your Changes \nOR WAIT FOR FUTURE UPDATES.')
            print60()
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')

menu()
