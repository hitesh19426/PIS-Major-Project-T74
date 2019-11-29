import smtplib  
from datetime import datetime
from loc import *
now=datetime.now()
dt_string=now.strftime("%d-%m-%Y %H:%M:%S")  

s = smtplib.SMTP('smtp.gmail.com', 587) 

s.starttls() 

s.login("sushant19450@iiitd.ac.in", "SG20016240") 

add = address()
l1='Dear Owner,\n'
l2='Your Driver is feeling sleepy.\nHere are the details: \n'
l3='Driver Name:	pata_nahi \nVehicle No:	private\n' 
l4='Current Date and Time:	'+dt_string+ "\n"
l5='Coordinates of Driver:	' + str(add[0][0]) + " , " + str(add[0][1]) + "\n"
l6="Location of driver:	" + str(add[1])
message1 = l1+l2+l3+l4+l5+l6

from twilio.rest import Client 
  
# Your Account Sid and Auth Token from twilio.com / console 
account_sid = 'ACdbb4690fd1122bad33b7180e6436f50f'
auth_token = '400ae167a63a5fe5923a501bb1d72d66'
  
client = Client(account_sid, auth_token) 
  
''' Change the value of 'from' with the number  
received from Twilio and the value of 'to' 
with the number in which you want to send message.'''
message = client.messages.create( 
                              from_='+12056274766', 
                              body =message1, 
                              to ='+919654664580'
                          ) 
  
print(message.sid) 
s.sendmail("sushant19450@iiitd.ac.in", "sushantG2001@gmail.com", message1) 

s.quit() 


