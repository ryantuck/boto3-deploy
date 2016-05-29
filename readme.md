# boto3-based deployment for datapipes

```
cd lambda
pip install -r requirements.txt -t pkg
```

## todo

- add vpc config for lambda (easy)
- make iam role/policy creation more robust (attach multiple policies, etc)
- delete stuff that's not managed by configuration
- optional deployment for single role, etc versus deploying everything
