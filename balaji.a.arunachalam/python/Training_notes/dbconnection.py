"""This is DataBase connection """

from imapla.dpapi import connect
a= connect(host="",port="",auth_mechnaism="",kerboroes_service_name="hive",use_ssl=True,ca_cert="")
a.exeucte(query)
b=a.fetchall()

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

import cx_oracle
a=cx_oracle.makedsn(host,port,,service_name="")
b = cx_oracle.connect(user="",password="",dsn=a)
c=b.cursor()
c.execute(query)

import pymssql
a=pymssql.connect(server="",user="",password="",database="")
b=a.cursor()
b.execute()

import teradata
udaExec = teradata.UdaExec (appName="HelloWorld", version="1.0",
        logConsole=False)

session = udaExec.connect(method="odbc", system="server_name",
        username="PRODRUN", password="PRODRUN",authentication="LDAP")
b=session.cursor()
b.execute()

