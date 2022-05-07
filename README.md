# Python Redis Ping

This is a simple script that pings a Redis connection to ensure that it can connect to
it.

## Getting Started

### Locally (Docker)

```bash
docker-compose up -d
docker exec -it redis-ping_app_1 sh
pip install -r requirements.txt
python main.py
# If you see "True" in the output, then your Python app connected to the Redis instance successfully 🎉
```

### AWS Lambda

Create an AWS Lambda function, then follow the
[AWS Docs - Deploy Python Lambda functions with .zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html#python-package-create-package-with-dependency)

In a nutshell, first you need to run the local docker setup. Once you're inside the
docker container, run the following:

```bash
pip install -r requirements.txt --target ./package
```

Now from a terminal on your host OS (outside the docker container), run the
following:

```bash
cd package
zip -r ../deployment-package.zip .
cd ..
zip -g deployment-package.zip main.py
aws lambda update-function-code --function-name FUNCTION_NAME_HERE --zip-file fileb://deployment-package.zip
```

Finally, From the AWS Console, make sure of the following:

1. The Lambda function's Runtime Settings > Handler is set to "main.lambda_handler".
2. You set the environment variables for your Redis host from Configuration > Environment Variables.

And that's it! Do a test run of your Lambda Function from the AWS Console and examine
the logs. If you see `True`, then your lambda function is connected to your Redis
instance successfully.
