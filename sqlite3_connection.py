# connect sqlite3 database with python.

import sqlite3

# create database
connection = sqlite3.connect("District_details.db")

# # create table
# table = connection.execute("create table Osmanabad1 ('Sr.NO.' int, 'Village_name' text)")

# add records in table

connection.execute("insert into Osmanabad1 values(1, 'Keshegaon')")
connection.execute("insert into Osmanabad1 values(2, 'Chikhali')")

# commit changes

connection.commit()

# show details

show = connection.execute("select * from Osmanabad1")
print(show.fetchall())