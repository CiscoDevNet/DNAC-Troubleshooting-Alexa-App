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
     Look at video recording of working Alexa App --  
     https://www.youtube.com/watch?v=b2_WrI7Ov30&index=2&list=PL5kAIXUXmL1DkErkeJWrMHtQltjuc-YsX&t=0s
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
	*AWS CLI need to be installed from https://aws.amazon.com/cli/
		example - pip install awscli
		This is needed to upload app to aws account 
		example - aws lambda update-function-code --function-name dnac --zip-file fileb://index.zip
	*Ngrok need to be installed from https://ngrok.com/download
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
		
		 _______________________________________________________________________________________	
		|  Files              | Descriptions 						        |
		|_____________________|_________________________________________________________________|
		| dnac_config.py      |	contains the dnac cluster information				|
		|		      | please change according to your dnac ip info, 			|
		|		      | username and password  						|
		|		      |	Example -							|
		|		      |	BONAGARA-M-F0XJ:dnac-templates bonagara$ cat dnac_config.py 	|
		|		      | DNAC=os.environ.get('DNAC','192.168.117.29')			|
		|		      | DNAC_PORT=os.environ.get('DNAC_PORT',8080)			|
		|		      |	DNAC_USER=os.environ.get('DNAC_USER','admin')			|
		|		      |	DNAC_PASSWORD=os.environ.get('DNAC_PASSWORD','Maglev123')|	| 						|		      |									|	
		|_____________________|_________________________________________________________________|
		|dnac.py	      | contains the dnac helper functions      |			|						|		      |									|
		|_____________________|_________________________________________________________________|
		|deplytemplate.py     | contains the deploy POST API of template programmer which does  |
		|		      | actual provisioning to WLC's  via dnac cluster and you can      |
		|		      | start the python flask server by invoking ./deploytemplate.py   |
		|   		      | also you can change the WLC IP address and AP name inside       |       
		|		      | ndeploytemplate.py payload variable                             |
		|		      | Example -                                                       |
		|		      | BONAGARA-M-F0XJ:dnac-templates bonagara$ ./deploytemplate.py    |
		|		      |	                                                                |
		|_____________________|_________________________________________________________________|
		
		
	3. Go to directory -- Alexa-DNAC-Intent/code in the git cloned repo folder and modify the ngrok server information 
		as mentioned below  
	   ______________________________________________________________________________________________________________________
	  |	cd /Users/bonagara/Downloads/alexa-app/DNAC-APP-DEV/DNAC-AppDev/DNAC Troubleshooting App/alexa-app/		 |
	  |	cd ./Alexa-DNAC-Intent/code											 |
	  |     vi lambda_function.py												 |
	  |     please change below server proxy and port information according to your ngrok daemon				 |
	  |     DNAC_PROXY = "f76fd944.ngrok.io"										 |
	  |     DNAC_PROXY_PORT = "80"												 |
	  |______________________________________________________________________________________________________________________|
	
  	 4. zip the entire code folder and run the aws CLI as mentioned below
	         _______________________________________________________________________________________________
		|												|
		|   	execute below commands from terminal							|
		|	cd /Users/bonagara/Downloads/alexa-app/Alexa-DNAC-Intent/code				|
		|	zip --recurse-paths ../index.zip *							|
		|	cd ..											|
		|	aws lambda update-function-code --function-name dnac --zip-file fileb://index.zip	|
		|												|
		|_______________________________________________________________________________________________|
		

How to play with DNAC Alexa App -
--------------------------------

	1. Power ON Alexa echo spot
	2. Connect to Wireless SSID of your network, so that it gets internet conenction 
	3. Play with Alexa with few commands like Alexa Good Morning :) and make sure its connected to Internet and respond back with 		   greeting	
	4. Ask Alexa with DNAC voice commands like "Alexa Genie" and she will respond back with "Welcome to DNAC Alexa Intent Library 	   	      1.0"
	5. Goto Console or telnet of WLC and execute below CLI to verify whether blinking status is on or off for particular AP
	
	   BONAGARA-M-F0XJ:ashutosh bonagara$ telnet 172.20.228.71
	   Trying 172.20.228.71...
	   Connected to 172.20.228.71.
	   Escape character is '^]'.
	   (Cisco Controller) 
	   User: admin
	   Password:********
	   (Cisco Controller) >
	   (Cisco Controller) >
	   (Cisco Controller) >
	   (Cisco Controller) >
	   (Cisco Controller) >show ap led-flash APCC16.7EDB.6C5E

	   Led Flash........................................ Disabled
	
	6. Ask Alexa with DNAC Voice commands like "Alexa LED ON" and she will respond back with provisioning status and blinking status   	      AP on the floor
	   Goto Console or telnet of WLC and execute below CLI to check whether blinking status is on 
	   (Cisco Controller) >
	   (Cisco Controller) >
	   (Cisco Controller) >
	   (Cisco Controller) >show ap led-flash APCC16.7EDB.6C5E

	   Led Flash........................................ Enabled for 60 secs, 59 secs left




Any additional help you need? 

	None (for now)
