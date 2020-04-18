#!/usr/bin/env python3

from aws_cdk import core

from resource_stacks.custom_vpc import CustomVpcStack
from resource_stacks.custom_ec2 import CustomEc2Stack
from resource_stacks.custom_ec2_with_instance_profile import CustomEc2InstanceProfileStack
from resource_stacks.custom_ec2_with_latest_ami import CustomEc2LatestAmiStack
from resource_stacks.custom_ec2_with_ebs_piops import CustomEc2PiopsStack
from resource_stacks.custom_parameters_secrets import CustomParametersSecretsStack
from resource_stacks.custom_iam_users_groups import CustomIamUsersGroupsStack
from resource_stacks.custom_iam_roles_policies import CustomRolesPoliciesStack
from resource_stacks.custom_s3_resource_policy import CustomS3ResourcePolicyStack
from resource_stacks.custom_sns import CustomSnsStack
from resource_stacks.custom_sqs import CustomSqsStack

# Import Serverless Stack resources
from serverless_stacks.custom_lambda import CustomLambdaStack
from serverless_stacks.custom_cloudwatch_loggroups import CustomLoggroupStack
from serverless_stacks.custom_lambda_src_from_s3 import CustomLambdaSrcFromS3Stack


# EC2 & VPC with Application LoadBalancer
from app_stacks.vpc_stack import VpcStack
from app_stacks.web_server_stack import WebServerStack

# VPC, EC2, ALB, RDS Stack
from app_db_stack.vpc_3tier_stack import Vpc3TierStack
from app_db_stack.web_server_3tier_stack import WebServer3TierStack
from app_db_stack.rds_3tier_stack import RdsDatabase3TierStack

from stacks_from_cfn.stack_from_existing_cfn_template import StackFromCloudformationTemplate

app = core.App()

env_prod = core.Environment(account="835800058584", region="us-east-1")

# Custom VPC Stack
# CustomVpcStack(app, "my-custom-vpc-stack", env=env_prod)

# Custom Ec2 Stack
# CustomEc2Stack(app, "my-web-server-stack", env=env_prod)

# Custom EC2 InstaceProfileStack
# CustomEc2InstanceProfileStack(app, "web-server-stack", env=env_prod)

# Custom EC2 Instace with Latest AMI Stack
# CustomEc2LatestAmiStack(app, "web-server-latest-ami-stack", env=env_prod)

# EC2 with Provisioned IOPS
# piops_stack = CustomEc2PiopsStack(app, "ec2-with-piops-stack")

# Application Stack ASG and ALB
# vpc_stack = VpcStack(app, "multi-tier-app-vpc-stack")
# ec2_stack = WebServerStack(
#     app, "multi-tier-app-web-server-stack", vpc=vpc_stack.vpc)

# Create SSM Parameter & AWS Secrets Manager Secrets
# params_secrets_stack = CustomParametersSecretsStack(
#     app,
#     "custom-parameters-secrets-stack",
#     description="Create SSM Parameter & AWS Secrets Manager Secrets"
# )

# Create IAM User & Groups
# iam_users_groups_stack = CustomIamUsersGroupsStack(
#     app,
#     "custom-iam-users-groups-stack",
#     description="Create IAM User & Groups"
# )

# Create IAM Roles & Policies
# custom_iam_roles_policies = CustomRolesPoliciesStack(
#     app,
#     "custom-iam-roles-policies-stack",
#     description="Create IAM Roles & Policies"
# )

# Create S3 Resource Policy
# custom_s3_resource_policy = CustomS3ResourcePolicyStack(
#     app,
#     "custom-s3-esource-policy-stack",
#     description="Create S3 Resource Policy"
# )

# Create 3Tier App with App Servers in ASG and Backend as RDS Database
# vpc_3tier_stack = Vpc3TierStack(app, "multi-tier-app-vpc-stack")
# app_3tier_stack = WebServer3TierStack(
#     app, "multi-tier-app-web-server-stack", vpc=vpc_3tier_stack.vpc)
# db_3tier_stack = RdsDatabase3TierStack(
#     app,
#     "multi-tier-app-db-stack",
#     vpc=vpc_3tier_stack.vpc,
#     asg_security_groups=app_3tier_stack.web_server_asg.connections.security_groups,
#     description="Create Custom RDS Database"
# )

# Resource Stack from pre-existing Cloudformation Template
# stack_from_cfn = StackFromCloudformationTemplate(app,
#                                                  "stack-from-pre-existing-cfn",
#                                                  description="Resource Stack from pre-existing Cloudformation Template"
#                                                  )

# Create SNS Topics & Add Email Subscriptions
# custom_sns = CustomSnsStack(
#     app,
#     "custom-sns-stack",
#     description="Create SNS Topics & Add Email Subscriptions"
# )

# Create SQS for microservices
# custom_sqs = CustomSqsStack(
#     app,
#     "custom-sqs-stack",
#     description="Create a fully managed message queues for microservices"
# )

# Create Serverless Event Processor using Lambda
# custom_lambda = CustomLambdaStack(
#     app,
#     "custom-lambda-stack",
#     description="Create Serverless Event Processor using Lambda"
# )

# Create Custom Cloudwatch Loggroups
# custom_loggroup = CustomLoggroupStack(
#     app,
#     "custom-loggroup-stack",
#     description="Create Custom Cloudwatch Loggroups"
# )

# Create Lambda Source Assets from S3
custom_lambda_src_from_s3 = CustomLambdaSrcFromS3Stack(
    app,
    "custom-lambda-src-from-s3-stack",
    description="Create Lambda Source Assets from S3"
)

# Stack Level Tagging
core.Tag.add(app, key="Owner",
             value=app.node.try_get_context('owner'))
core.Tag.add(app, key="OwnerProfile",
             value=app.node.try_get_context('github_profile'))
core.Tag.add(app, key="GithubRepo",
             value=app.node.try_get_context('github_repo_url'))
core.Tag.add(app, key="ToKnowMore",
             value=app.node.try_get_context('youtube_profile'))


app.synth()
