# DemoEchoShowSkillWithServerless
A demo of an Amazon Echo Show Skill made with the Serverless Framework. For more information, checkout my blog post here: https://luisgarcia.me/

NOTE:
Make sure to re-populate the skill id in the following files
- DemoShow/lambda/serverless.yml
- DemoShow/ask-resources.json
Make sure to repopulate the lambda endpoint in the file:
- DemoShow/skill-package/skill.json
```
...
"manifest": {
     "apis": {
       "custom": {
+        "endpoint": {
+          "uri": "arn:aws:lambda:{region}:{account}:function:{functionName}"
+        },
         "interfaces": [
...
```