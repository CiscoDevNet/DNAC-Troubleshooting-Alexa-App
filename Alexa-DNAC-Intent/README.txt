
Zip in the "code" directory:

zip --recurse-paths ../index.zip *



Commit code to lambda function.

aws lambda update-function-code --function-name dnac --zip-file fileb://index.zip






