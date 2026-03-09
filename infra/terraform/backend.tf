terraform {
  backend "s3" {
    bucket = "resume-analyzer-terraform-state-aditya"
    key    = "infra/terraform.tfstate"
    region = "ap-south-1"
  }
}