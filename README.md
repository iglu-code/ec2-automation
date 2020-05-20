# ec2-automation

This repository contains two lambda functions that start and stop an EC2 instance on a schedule.

## Template parameters

* InstanceId: The ID of the instance to schedule.

## TODO

* Add parameter for the schedule values.

## Deploy the template

Build the functions.

```shell
$ sam build

Building resource 'StartEc2Instance'
Running PythonPipBuilder:ResolveDependencies
Running PythonPipBuilder:CopySource
Building resource 'StopEc2Instance'
Running PythonPipBuilder:ResolveDependencies
Running PythonPipBuilder:CopySource

Build Succeeded

Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml

Commands you can use next
=========================
[*] Invoke Function: sam local invoke
[*] Deploy: sam deploy --guided
```

Deploy the template


```shell
$ sam deploy --template-file .aws-sam/build/template.yaml \
--stack-name STACK_NAME \
--s3-bucket BUCKET_NAME \
--s3-prefix STACK_NAME \
--region REGION \
--capabilities CAPABILITY_IAM \
--no-fail-on-empty-changeset \
--profile PROFILE
```

Example

```shell
$ sam deploy --template-file .aws-sam/build/template.yaml \
--stack-name automate-demo-server-start-stop \
--s3-bucket iglu-deployments-london \
--s3-prefix automate-demo-server-start-stop \
--region eu-west-2 \
--capabilities CAPABILITY_IAM \
--no-fail-on-empty-changeset \
--profile iglu


        Deploying with following values
        ===============================
        Stack name                 : automate-demo-server-start-stop
        Region                     : eu-west-2
        Confirm changeset          : False
        Deployment s3 bucket       : iglu-deployments-london
        Capabilities               : ["CAPABILITY_IAM"]
        Parameter overrides        : {}

Initiating deployment
=====================
Uploading to automate-demo-server-start-stop/ef88f873cc3b2f4ce79249c286054d5b  418 / 418.0  (100.00%)
Uploading to automate-demo-server-start-stop/7074fb0d45eb506e4e59f8d93e945d85  420 / 420.0  (100.00%)
Uploading to automate-demo-server-start-stop/f9e45fad50b352226782a187d439cd93.template  1773 / 1773.0  (100.00%)

Waiting for changeset to be created..

CloudFormation stack changeset
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Operation                                                    LogicalResourceId                                            ResourceType                                               
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
* Modify                                                     StartEc2InstanceCronEveryDay8amPermission                    AWS::Lambda::Permission                                    
* Modify                                                     StartEc2InstanceCronEveryDay8am                              AWS::Events::Rule                                          
* Modify                                                     StartEc2Instance                                             AWS::Lambda::Function                                      
* Modify                                                     StopEc2InstanceCronEveryDay10pmPermission                    AWS::Lambda::Permission                                    
* Modify                                                     StopEc2InstanceCronEveryDay10pm                              AWS::Events::Rule                                          
* Modify                                                     StopEc2Instance                                              AWS::Lambda::Function                                      
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Changeset created successfully. arn:aws:cloudformation:eu-west-2:886033307210:changeSet/samcli-deploy1589964928/96d14195-bb83-4e3f-bd0a-61c2d20f4049


2020-05-20 09:55:38 - Waiting for stack create/update to complete

CloudFormation events from changeset
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ResourceStatus                                ResourceType                                  LogicalResourceId                             ResourceStatusReason                        
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
UPDATE_IN_PROGRESS                            AWS::Lambda::Function                         StartEc2Instance                              -                                           
UPDATE_IN_PROGRESS                            AWS::Lambda::Function                         StopEc2Instance                               -                                           
UPDATE_COMPLETE                               AWS::Lambda::Function                         StartEc2Instance                              -                                           
UPDATE_COMPLETE                               AWS::Lambda::Function                         StopEc2Instance                               -                                           
UPDATE_COMPLETE_CLEANUP_IN_PROGRESS           AWS::CloudFormation::Stack                    automate-demo-server-start-stop               -                                           
UPDATE_COMPLETE                               AWS::CloudFormation::Stack                    automate-demo-server-start-stop               -                                           
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Successfully created/updated stack - automate-demo-server-start-stop in eu-west-2
```