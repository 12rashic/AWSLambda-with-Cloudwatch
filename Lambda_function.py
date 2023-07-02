import json
import boto3

def lambda_handler(event , context)
#TODO 
Subject= "Alert : your AWS Instance is stooped !"
client= boto3.Client("ses")
body = """
       <br>
	   This is to inform you that your EC2 Instance
	   named "Prodcution Instance" is either stopped or 
	   is pending. Kindly have a look.
	   
msg ={"Subject : {"Data" : Subject} , "Body" :{"Html " {"Data" : body}}}
response = client.send_email(Source = "12rashic@gmail.com" , Destination={"ToAddresses" " ["12rashic@gmail.com]} , Message =msg}
print("sent")	   