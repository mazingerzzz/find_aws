# find_aws
Find instances IP and statut from LB, beanstalk or instance name


Usage:

``` 
-p --profile : Specify your aws profile (.aws/credentials)

-l --loadbalancer : Specify ELB name (full or partial, @ for all)

-b --beanstalk : Specify environment name (full or partial, @ for all)

-e --export : Path to ansible hosts file to export results when using -l or -b (it overwrite the file)

-r --region : Specify your aws region (default eu-west-1)

"ip" : Get instance details

nothing: List all instances
```

![1](https://cloud.githubusercontent.com/assets/10193614/19148628/f3ffeed2-8bbd-11e6-9596-a71f14d5d8e8.png)
![2](https://cloud.githubusercontent.com/assets/10193614/19148632/f665a5b8-8bbd-11e6-86f6-45e060ac9458.png)
![3](https://cloud.githubusercontent.com/assets/10193614/19148634/f79c33d4-8bbd-11e6-904a-01cf069beec1.png)
