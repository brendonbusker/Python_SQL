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

cursor.execute ('select name, budget from School.dbo.Department')

data = cursor.fetchall()


#Work
print('Dept Name'.ljust(25), 'Original Budget'.ljust(20), 'New Budget'.ljust(15), 'Increase in Budget'.ljsut(30))

for row in data:
    name = row[0]
    old_budget = float(row[1])

    if name == 'Information Systems':
        new_budget = old_budget * 1.2

    elif name == "Computer Science":
        new_budget = old_budget * 1.15

    else:
        new_budget = old_budget * 1.1
    
    increase = new_budget - old_budget

    print(f"{row[0].ljust(25)} {old_budget:,.2f} {new_budget:20,.2f} {increase:14,.2f}")


