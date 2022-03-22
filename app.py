#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_poc.aws_cdk_poc_stack import AwsCdkPocStack


app = cdk.App()
AwsCdkPocStack(app, "aws-cdk-poc")

app.synth()
