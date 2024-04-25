import sqlite3
con=sqlite3.Connection("piyu")
cur=con.cursor()


# cur.execute('create table operator(op_id int,name varchar(25),address varchar(25),phone int, email varchar(30))')
# cur.execute('create table route(route_id int,station varchar(30),s_id int)')
# cur.execute('create table Bus (Bus_id int,Type varchar(15),capacity int,fare int,route_id int,op_id int)')
# cur.execute('create table Runs(Bus_id int,journey_date date,seat_available int)')
# cur.execute('Drop table Booking')
# cur.execute('create table Booking(ref_id INTEGER PRIMARY KEY,Mobile int,Name varchar(15),sex char(1),age int,Bus_id int, journey_date date,Ticket int,Fare INT,FromSt varchar(25),ToSt varchar(25))')
# cur.execute('DELETE from Booking')
# cur.execute('insert into operator values (1,"Kamla Bus","Guna",123456789,"operator@kamlabus.com"),(2,"Bamla bus","ragogarh",987654321,"abcd@gmail.com") ')
# cur.execute('insert into route values (1,"guna",1),(1,"Raghogarh",2) ')
# cur.execute('insert into bus values (1,"AC 2x2",50,500,1,1),(2,"AC 3x2",25,300,1,2) ')
# cur.execute('insert into runs values (1,"02/12/2022",45),(1,"04/12/2022",20) ')
# cur.execute('Alter table operator ADD PRIMARY KEY(op_id)')

con.commit()
con.close()
