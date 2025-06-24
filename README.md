# Real-Time Cloud Infrastructure Monitoring & Auto-Healing System

## Overview
A robust AWS-based solution that monitors EC2 instances and auto-heals them upon failure using CloudWatch and Lambda.

## Components
- EC2 instance tagged for auto-healing
- CloudWatch alarms for CPU and status checks
- Lambda function to reboot instances
- Terraform for infrastructure as code

## Deployment Steps
1. Update `variables.tf` with your AMI ID.
2. Run `terraform init && terraform apply` in the `terraform/` folder.
3. Deploy Lambda function manually or use CI/CD pipeline.

## Author
Shubham Ghalsasi