import tkinter as t
import tkinter.messagebox
import pyodbc


class SQL_Login:
    def __init__(self):
        #Main window
        self.main_window = t.Tk()
        self.main_window.geometry("250x125")
        self.main_window.title("SQL Server Login")

        #Frames
        self.enter_login_frame = t.Frame(self.main_window)
        self.password_frame = t.Frame(self.main_window)
        self.login_frame = t.Frame(self.main_window)

        #Login
        self.login_label = t.Label(self.enter_login_frame, text = "Login:       ")
        self.login_entry = t.Entry(self.enter_login_frame, width = 20)
        self.login_label.pack(side = "left")
        self.login_entry.pack(side = "left")

        #Password
        self.pass_label = t.Label(self.password_frame, text = "Password:")
        self.pass_entry = t.Entry(self.password_frame, width = 20, show = "*")
        self.pass_label.pack(side = "left")
        self.pass_entry.pack(side = "left")

        #Login Button
        self.login_button = t.Button(self.login_frame, text = "Login", command = self.access_database, width = 20)
        self.login_button.pack(side = "top")

        #Pack Frames
        self.enter_login_frame.pack()
        self.password_frame.pack()
        self.login_frame.pack()

        #Loop
        t.mainloop()

    #Access Database Command
    def access_database(self):
        login = self.login_entry.get()
        password = self.pass_entry.get()
        
        self.main_window.destroy()
        
        preList = {}
        courseList = []
        
        
        login = "brendon_busker1"
        password = "MIS4322student"
        cn_str = (
            
        'Driver={SQL Server Native Client 11.0};' #data source driver
            
        'Server=MIS-SQLJB;' #server name
            
        'Database=School;' #database name
            
        'UID='+login+';'   #username
            
        'PWD='+password+';' #user password
            
        )
        
               
        #connect to server
        
        cn = pyodbc.connect(cn_str)

        cursor = cn.cursor()

        cursor.execute ('select name, budget from School.dbo.Department')

        data = cursor.fetchall()

        #print(data)

        
        for row in data:
            deptName = row[0]
            origBudget = row[1]
            
            preList = {"DeptName":deptName, "Original Budget":origBudget}
            courseList.append(preList)
            
        print(courseList)
            
        

        '''
        for row in data:
            courseID = row[0]
            name = row[1]
            credit = row[2]
            deptID = row[3]

            preList = {"CourseID":courseID, "Title":name, "Credit":credit, "DeptID":deptID}

            courseList.append(preList)

            print(preList)
        

        a = int(input("CourseID to search: "))

        for dictionary in courseList:
            if dictionary["CourseID"] == a:
                print(f'Title of the course: {dictionary["Title"]}')
                print(f'Credits for the course: {dictionary["Credit"]}')
                print(f'Dept ID for the course: {dictionary["DeptID"]}')
        '''




#Run GUI
SQL_server_login = SQL_Login()

'''
1)
Calculate the new budget for each department. Every department will be getting a 10% increase in their budget except for 
the Information Systems (IS) and Computer Science (CS) departments. The IS department gets a 20% increase and the 
CS department gets a 15 % increase. Create a well formatted report that shows each department name, their 
current budget, their new budget and the amount increased.



Dept Name				Original Budget		New Budget		Increse in Budget
Engineering				$350,000.00			$385,000.00		$35,000.00
English					$120,000.00			$132,000.00		$12,000.00
Economics				$200,000.00			$220,000.00		$20,000.00
Mathematics				$250,000.00			$275,000.00		$25,000.00
Information Systems		$375,000.00			$450,000.00		$75,000.00
Computer Science		$310,500.00			$357,075.00		$46,575.00



****I did the exercises in the seperate py files****
'''






'''
2)
Display First Name, Last Name and corresponding personal and work email
for STUDENTS ONLY using Person and Contact_Info tables as shown below (only first row shown):


firstname	lastname	Personal Email					Work Email
Gytis		Barzdukas	josephine_darakjy@darakjy.org	ezekiel@chui.com
Peggy		Justice		art@venere.org					wkusko@yahoo.com
Yan			Li			lpaprocki@hotmail.com			bfigeroa@aol.com
Laura		Norman		donette.foller@cox.net			ammie@corrio.com
Nino		Olivotto	simona@morasca.com				francine_vocelka@vocelka.com

'''








'''
3)
Display First Name, Last Name and corresponding home,cell and work phone numbers
for instructors only using Person and Contact_Info tables as shown below (only first 2 rows shown):

FirstName	LastName		Home_Phone		Cell_Phone		Work_Phone
Kim			Abercrombie		(504) 621-8927	(410) 621-8927	(313) 621-8927
Fadi		Fakhouri		(810) 292-9388	(215) 292-9388	(815) 292-9388

'''



