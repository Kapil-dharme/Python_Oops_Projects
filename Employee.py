class Employee :
    emplist=[]
    def __init__(self,name1,age1,salary1):
        self.name1=name1
        self.age1=age1
        self.salary1=salary1

    def employeeinfo(self):
        print("Employee Name =",self.name1)
        print("Employee Age =",self.age1)
        print("Employee Salary =",self.salary1)

class Employee_Manager(Employee):
    def add_emp (self):
        n=input("Enter Name : ")
        a=int(input("Enter Age : "))
        s=int(input("Enter Salary : "))
        
        self.emplist.append(n)
        self.emplist.append(a)
        self.emplist.append(s)
        print("Employee data added to the database✅")
    
    def empdetails (self):
          print(self.emplist)

    def empdelete (self):
        empage=int(input("Enter Age : "))
        idx=0
        id=0
        i=1
        while(i<=len(self.emplist)):
            if (empage in self.emplist):
                if (empage==self.emplist[idx]):
                    self.emplist.count(empage)
                    if self.emplist.count(empage)>1:
                        empnam= input("Enter Name :")
                        while (i<=len(self.emplist)):
                            if empnam==self.emplist[id]:
                                del self.emplist[id:id+3]                               
                                print("Deleting data...")
                                print("Data successfully removed✅")
                                print(self.emplist)   
                                break
                            id+=1
                        break    
                    else:
                        self.emplist.remove(self.emplist[idx-1])
                        self.emplist.remove(self.emplist[idx])         
                        self.emplist.remove(self.emplist[idx-1])
                        print("Deleting data...")
                        print("Data successfully removed✅")
                        print(self.emplist)   
                        break
                idx+=1
            else:
                print("Database do not have such type of data.")
                break

    def findemp (self):
        empname=input("Enter Name : ")
        idx1=0
        i=1
        while (i<=len(self.emplist)):
            if (empname in self.emplist):
                if (self.emplist[idx1]==empname):
                    print("Employee Name =",empname)          
                    print("Employee Age =",self.emplist[idx1+1])
                    print("Employee Salary =",self.emplist[idx1+2])
                    break
                idx1+=1
            else:
                print("Database do not have such type of data.")
                break
        
    def updatesalary (self):
        nam=input("Enter Name : ")
        idx2=0
        i=1
        while (i<=len(self.emplist)):
            if (nam in self.emplist):
                if (nam==self.emplist[idx2]):
                    update=int(input("Enter the the updated salary : "))
                    print("Updating salary...")
                    self.emplist.remove(self.emplist[idx2+2])                          
                    self.emplist.insert(idx2+2,update)
                    print("Salary updated successfully✅")
                    print(self.emplist)                          
                    break
                idx2+=1
            else:
                print("Database do not have such type of data.")
                break

class frontend_manager(Employee):
    def menu (self):
        print("PROGRAM CHOICES :- ")
        print("1)For adding Employee to the database please press 1 :")
        print("2)For knowing Employee details please press 2 :")
        print("3)For finding Employee details by their name please press 3 :")
        print("4)For updating Employee salary please press 4 :")
        print("5)For deleting Employee details please press 5 :")
        
        while True:
            press=int(input("Enter your choice : "))
            if(press==1):
                Employee_Manager.add_emp(self)
            elif(press==2):
                Employee_Manager.empdetails(self)
            elif(press==3):
                Employee_Manager.findemp(self)
            elif(press==4):
                Employee_Manager.updatesalary(self)
            elif(press==5):
                Employee_Manager.empdelete(self)
            else:
                print("Please enter a valid choice.")
                continue


e1=frontend_manager("kapil",18,50000)
e1.menu()
