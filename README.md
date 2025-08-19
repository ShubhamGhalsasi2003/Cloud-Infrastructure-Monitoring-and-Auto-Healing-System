#  Real-Time Cloud Infrastructure Monitoring & Auto-Healing System

This project is a real-time cloud infrastructure monitoring and recovery system built using **AWS CloudWatch**, **AWS Lambda**, and **Terraform**. It automatically detects if an EC2 instance is failing and heals it (reboot or restart) without human intervention.

---

## 🎯 Objective

Ensure high availability and self‑recovery of EC2 instances by monitoring system health and CPU usage, then auto‑repairing with AWS‑native services.

---

## ⚙️ What I Used

- **AWS EC2** – Linux virtual machine
- **AWS CloudWatch** – Metrics & alarms
- **AWS Lambda** – Auto‑reboot/restart logic
- **IAM Roles** – Permission management
- **Terraform** – Infrastructure as Code (IaC)

---

## 🛠️ Manual AWS Setup (before Terraform)

### 1️⃣ Launch an EC2 Instance
1. Open the EC2 console → **Launch Instance**  
2. Choose Amazon Linux 2 or Ubuntu AMI  
3. Select `t2.micro` (free tier)  
4. Add a tag → **Key:** `AutoHeal`, **Value:** `true`  
5. Allow SSH (port 22) in the security group  
6. Download the key pair (e.g., `my‑key.pem`)

### 2️⃣ Create an IAM Role for Lambda
1. IAM → Roles → **Create role**  
2. Trusted entity: **Lambda**  
3. Attach policies: `AmazonEC2FullAccess`, `CloudWatchFullAccess`  
4. Name it **LambdaAutoHealRole**


### 4️⃣ Deploy Lambda Function
1. Lambda → Create function → *Author from scratch*  
2. Name: **AutoHealInstance** | Runtime: *Python 3.x*  
3. Attach **LambdaAutoHealRole**  
4. Paste code from `lambda/autoheal_instance.py`  
5. (Optional) Set env vars `TAG_KEY=AutoHeal`, `TAG_VALUE=true`  
6. Add CloudWatch alarm trigger

---

## 🧱 Terraform Deployment

### Edit Variables
hcl
# terraform/variables.tf
variable "ami_id"       { default = "ami-xxxxxxxx" }  # your AMI
variable "instance_type"{ default = "t2.micro" }
variable "region"       { default = "us-east-1" }


### Provision Resources
bash
cd terraform/
terraform init
terraform plan
terraform apply


Terraform launches the EC2 instance, tags it, and sets up alarms.



## 📂 Project Structure

Cloud-Infrastructure-Monitoring/
├── alarms/
│   └── cloudwatch_alarms.json
├── lambda/
│   └── autoheal_instance.py
├── terraform/
│   ├── main.tf
│   ├── outputs.tf
│   └── variables.tf
└── README.md



## 🧪 Test the Auto‑Healing
1. Stop or terminate the EC2 instance manually.  
2. CloudWatch alarm fires → triggers Lambda.  
3. Lambda action reboots / replaces the instance.  
4. Verify recovery in EC2 console and Lambda CloudWatch logs.

---

## 🔧 Tool Summary

| Service   | Purpose                          |
|-----------|----------------------------------|
| EC2       | Compute workload                 |
| CloudWatch| Monitoring & alarms              |
| Lambda    | Remediation logic (Python)       |
| Terraform | Repeatable IaC provisioning      |

---

## 👨‍💻 Author
**Shubham Ghalsasi**  
B.Tech – Cloud Computing, MIT ADT University  
📫 ghalsasishubham@gmail.com

