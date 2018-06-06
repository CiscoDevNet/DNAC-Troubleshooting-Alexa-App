APP TITLE - 
-----------	
ALEXA DNAC AP troubleshooting App

BRIEF DESCRIPTION:
------------------
	The App will enable the customers to configure the blinking for given AP on the floor via DNAC Sample Alexa App 
Problem:
--------
      During the Fabric deployment of sites - floor, we noticed lots of APs not part of Fabric domain 
      and it's difficult for network admin to find the problematic AP's on the floor and ask contractor 
      to replace it or shut it down       
Solution:
---------
     This App will allow the users to configure the blinking LED Flash on APs for certain amount of time 
     and its configurable 1 min , 5 min definite secs or indefinite default as 60 secs       
APP DOMAIN/APIs USED:
--------------------- 
     TemplateProgrammer API - deploy and deploystatus API
How will the APP be Packaged? 
-----------------------------
	It will be packaged as an alexa app
Prerequisites:
------------- 
Required Lab Devices - 
--------------------- 
	Amazon Alexa Echo dot device 
    	Cisco DNAC Appliance  
	Cisco WLC Controller 55xx/35xx/85xx
	Cisco APs
Assumption - 
------------- 
	Login to DNAC, Add WLC Devices to Inventory, Create Project for Blinking AP via Template Programmer UI and 
	Create Template for Blinking AP inside Project Blinking AP
	Template CLI Contents :
		config ap led-state enable $apname
		config ap led-state flash $duration $apname  
	1.AWS CLI need to be installed from https://aws.amazon.com/cli/
		example - pip install awscli
		This is needed to upload app to aws account 
		example - aws lambda update-function-code --function-name dnac --zip-file fileb://index.zip
	2.Ngrok need to be installed from https://ngrok.com/download
		run below commands from terminal
		$ ./ngrok http 3000
How to build -
--------------- 
	1. git clone app project from https://github.com/CiscoDevNet/DNAC-Troubleshooting-Alexa-App.git
  	   example - 	
  		1.1 git clone https://github.com/CiscoDevNet/DNAC-Troubleshooting-Alexa-App.git
   		1.2.go to /Users/bonagara/Downloads/alexa-app/DNAC-APP-DEV/DNAC-AppDev/DNAC Troubleshooting App  
	2. go to folder alexa-app/dnac-templates after cloning of repo and start server after changing the dnac config files \
   	   according to your network 
   	   example - /Users/bonagara/Downloads/alexa-app/DNAC-APP-DEV/DNAC-AppDev/DNAC Troubleshooting App/alexa-app/dnac-templates/
	     BONAGARA-M-F0XJ:alexa-app bonagara$ cd dnac-templates/
             BONAGARA-M-F0XJ:dnac-templates bonagara$ ls
             	deploytemplate.py	
             	dnac.py		
             	dnac_config.py
		Notes:
		*dnac_config.py -- contains the dnac cluster information, please change according to your dnac ip info, 
		username and password  
		Example -
	    	BONAGARA-M-F0XJ:dnac-templates bonagara$ cat dnac_config.py 
	    	DNAC=os.environ.get('DNAC','192.168.117.29')
	    	DNAC_PORT=os.environ.get('DNAC_PORT',8080)
            	DNAC_USER=os.environ.get('DNAC_USER','admin')
            	DNAC_PASSWORD=os.environ.get('DNAC_PASSWORD','Maglev123')
	        *dnac.py -- contains the dnac helper functions 
		*deplytemplate.py -- contains the deploy POST API of template programmer which does actual provisioning to WLC's  
		via dnac cluster and you can start the python flask server by invoking ./deploytemplate.py , also you can change 
		the WLC IP address and AP name inside deploytemplate.py payload variable
		Example - 
		BONAGARA-M-F0XJ:dnac-templates bonagara$ ./deploytemplate.py 
 		* Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)
		TOKEN : {'controller_ip': '192.168.117.29', 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1YWZkYTZmMThhYTEyYzAwODNiOTVkOTMiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVhZmRhNmYxOGFhMTJjMDA4M2I5NWQ5MiJdLCJ0ZW5hbnRJZCI6IjVhZmRhNmYwOGFhMTJjMDA4M2I5NWQ5MCIsImV4cCI6MTUyNzg5MjQ1MywidXNlcm5hbWUiOiJhZG1pbiJ9.J1e9tAsaEM9TdcsMfzmP1oLX10W0IVon2-HbL34yEUQ'}
		LED ON : Posting to https://192.168.117.29/api/v1/template-programmer/template/deploy
		BODY: Posting {"targetInfo": [{"id": "172.20.228.71", "params": {"apname": "APCC16.7EDB.6C5E", "duration": "60"}, "type": "MANAGED_DEVICE_IP"}], "templateId": "bfb3ea5f-61a0-4ca4-9d57-5fd8dc03e41a"}
		202
		{'deploymentId': '2c72b5b6-8978-41db-87f3-326dd52179eb', 'startTime': '', 'endTime': '', 'duration': '0 seconds'}
		Waiting for deploymentId 2c72b5b6-8978-41db-87f3-326dd52179eb
		127.0.0.1 - - [01/Jun/2018 14:34:13] "POST /api/v1/setPowerLevelLow HTTP/1.1" 200 -
		4. Go to directory -- Alexa-DNAC-Intent/code in the git cloned repo folder and modify the ngrok server information 
		as mentioned below  
	   	Example - 
	        cd /Users/bonagara/Downloads/alexa-app/DNAC-APP-DEV/DNAC-AppDev/DNAC Troubleshooting App/alexa-app/Alexa-DNAC-Intent/code
	        vi lambda_function.py
	        please change below server proxy and port information according to your ngrok daemon
	        DNAC_PROXY = "f76fd944.ngrok.io"
	        DNAC_PROXY_PORT = "80"	
  	        5. zip the entire code folder and run the aws CLI as mentioned below
	        Example -    
	        zip --recurse-paths ../index.zip *
                aws lambda update-function-code --function-name dnac --zip-file fileb://index.zip
	        6. Attaching video link as well for quick demo of it --  
              https://www.youtube.com/watch?v=b2_WrI7Ov30&index=2&list=PL5kAIXUXmL1DkErkeJWrMHtQltjuc-YsX&t=0s


Any additional help you need? 

	None (for now)
