# find_aws
Find instances IP and statut from LB, beanstalk or instance name


Usage:

``` 
-p --profile : Specify your aws profile (.aws/credentials)

-l --loadbalancer : Specify ELB name (full or partial, @ for all)

-b --beanstalk : Specify environment name (full or partial, @ for all)

-r --region : Specify your aws region (default eu-west-1)

"ip" : Get instance details
```

nothing: List all instances
