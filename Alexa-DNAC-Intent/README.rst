# Alexa - NuLED Lights Learning Lab at CLEUR


This is the lamba function for the Alexa Intent to turn off, on and set 3 different colors to the NuLED ligths.

Essentially we have written 2 of the four functions, one to turn off the ligths and the other to turn the light color to Blue. One you have played with the 2 functionalities, you can expand the functionality to change the color to RED, GREEN and WHITE.

*         1. The functions are as follows:
*         2. LightsOFF() - Code present
*         3. SetColorBlue() - Code present
*         4. SetColorRed() - Stub
*         5. SetColorGreen() - Stub
*         6. SetColorWhite() - Stub

## Steps and Configuration Involved:

* Install the AWS CLI. - We have already installed this on your Mac. if it is not, please install using the pip/pip3 command:

> pip install awscli

* Configure AWS CLI for your account:

> aws configure

Enter your Access Key, Secret, Default region name as "us-east-1" and none

> aws lambda list-functions

* Try installing your Lambda Function on AWS:

Now, assuming you have downloaded this repo, simply use the publish shell script provided to install your lambda function.

> ./publish.sh

* Modify your Lambda function and republish:

> cd into the "code" directory and edit the "lambda_function.py". 
>
>  May of to edit LIGHT_ID = "NLCB0435D000F5A"




