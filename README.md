# Real-Time Cloud Infrastructure Monitoring & Auto-Healing System

This project is a real-time cloud monitoring system that automatically detects and recovers failed EC2 instances using AWS services. I used CloudWatch to monitor the instance's health and CPU usage. When a problem is detected, a Lambda function is triggered to reboot or replace the EC2 instance without manual effort. I also automated the entire infrastructure using Terraform, making it easy to deploy and manage. This system helps maintain high availability and reduces downtime with minimal human involvement.

