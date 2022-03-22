from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs
)


class AwsCdkPocStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # queue = sqs.Queue(
        #     self, "AwsCdkPocQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        # topic = sns.Topic(
        #     self, "AwsCdkPocTopic"
        # )

        # topic.add_subscription(subs.SqsSubscription(queue))
        
        lambda_role = iam.Role(scope=self, id='cdk-lambda-role',
                                assumed_by =iam.ServicePrincipal('lambda.amazonaws.com'),
                                role_name='cdk-lambda-role',
                                managed_policies=[
                                    #iam.ManagedPolicy.from_aws_managed_policy_name(
                                    #    'service-role/AWSLambdaVPCAccessExecutionRole'),
                                    iam.ManagedPolicy.from_aws_managed_policy_name(
                                        'service-role/AWSLambdaBasicExecutionRole')
                                ])
        
        cdk_lambda = _lambda.Function(
            self, 'cdk-lambda-test',
            runtime=_lambda.Runtime.PYTHON_3_9,
            function_name='cdk-lambda-test',
            description='Lambda function deployed using AWS CDK Python',
            code=_lambda.Code.from_asset('./resources'),
            handler='hellolambda.lambda_handler',
            role=lambda_role,
            environment={
                'NAME': 'cdk-lambda-test'
            }
        )
