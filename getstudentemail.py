import pyodbc

#Login and connect
login = 'brendon_busker1'
password = 'MIS4340student'

cn_str = (
            
        'Driver={SQL Server Native Client 11.0};' #data source driver
            
        'Server=MIS-SQLJB;' #server name
            
        'Database=School;' #database name
            
        'UID='+login+';'   #username
            
        'PWD='+password+';' #user password
            
        )


cn = pyodbc.connect(cn_str)

cursor = cn.cursor()

cursor.execute ('exec getStudentEmail')

data = cursor.fetchall()


#Work
print('First Name'.ljust(18), 'Last Name'.ljust(18), 'Personal Email'.ljust(28), 'Work Email'.ljust(28))

for row in data:
    print(row[0].ljust(18), row[1].ljust(18), row[2].ljust(28), row[3].ljust(28))

