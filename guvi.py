from enum import Flag
import re

def checkemailid(emailid):
  regex = r'\b\A[A-Za-z][A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  if(re.fullmatch(regex, emailid)):
    print("Valid Email ID")
    return emailid
  else:
    print("Invalid Email ID")
    return False

def checkpwd(password):
  flag = 0
  while flag == 0:
    if (len(password)<5) or (len(password)>16):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[!#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        return password
        break
  if flag ==-1:
    print("Please enter an valid Password" "\n" "Your Password must have minimum one special character, one numerical digit, one uppercase and one lowercase")
    return False

def getdetails():
    print("Please Provide")
    emailid = input("Email ID: ")
    g=0
    if checkemailid(emailid) == False:
      print("Please enter valid Email ID")
      g=g+1
               
    else:
      password = input("Password: ")
      if checkpwd(password) == False:
        #print("Please enter an valid Password" "\n" "Your Password must have minimum one special character, one numerical digit, one uppercase and one lowercase")
        g=g+1
         
    if g==0:
      file1 = open("User Data.txt","a")
      L = [emailid,password,"\n"]     
      file1.writelines(L)
      print("Registration is Successful") 

def get_existing_users(Emailid, Password):
  V = Emailid+Password
  p=0
  with open("User Data.txt") as f:
    for line in f:
      if V in line:
        p=1
    if p==1:
      print("Logged Successfully")
    else:
      print("Not Registered, Please Register")
    
def checkdetails():
  print("Please Provide")
  Emailid = input("Email ID: ")
  Password = input("Password: ")
  get_existing_users(Emailid, Password)

def checkuser(Forgotid):
  with open("User Data.txt") as f:
    c=0
    for line in f:
      if Forgotid in line:
        c=1
    if c==1:
      print("Please provie a new password")
      Newpwd = input("Password: ")
      if checkpwd(Newpwd)==True:
       file1 = open("User Data.txt","a")
       N = [Forgotid,Newpwd,"\n"]     
       file1.writelines(N)
       print("Password is updated")
    else:
      print("Email ID not registered, Please Register")
      
def forgotpwd():
  print("Please Provide")
  Forgotid = input("Email ID: ")
  checkuser(Forgotid)

print("Please select one of the options from below:")
choice = int(input("Registration-----1 \n" "Login------------2 \n" "Forgot Password--3 \n"))
if choice == 1:
  getdetails()
elif choice == 2:
  checkdetails()
elif choice == 3:
  forgotpwd()
else:
    print("Entered wrong option")