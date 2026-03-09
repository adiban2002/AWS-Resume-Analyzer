variable "aws_region" {
  default = "ap-south-1"
}

variable "frontend_bucket_name" {
  default = "resume-analyzer-frontend-aditya"
}

variable "storage_bucket_name" {
  default = "aws-resume-analyzer-storage"
}

variable "dynamodb_table_name" {
  default = "resume-analysis"
}

variable "ec2_instance_type" {
  default = "t2.micro"
}

variable "ec2_ami" {
  description = "AMI for EC2 instance"
  type        = string
}

variable "sagemaker_execution_role" {
  description = "IAM role ARN for SageMaker"
  type        = string
}

variable "sagemaker_image" {
  description = "Docker image in ECR for inference"
  type        = string
}