cd code 
zip --recurse-paths ../index.zip *
cd .. 
aws lambda update-function-code --function-name dnac --zip-file fileb://index.zip

