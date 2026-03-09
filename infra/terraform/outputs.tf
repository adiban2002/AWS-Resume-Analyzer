output "frontend_bucket" {
  value = aws_s3_bucket.frontend_bucket.bucket
}

output "storage_bucket" {
  value = aws_s3_bucket.storage_bucket.bucket
}

output "dynamodb_table" {
  value = aws_dynamodb_table.resume_analysis.name
}

output "ec2_public_ip" {
  value = aws_instance.api_server.public_ip
}

output "cloudfront_domain" {
  value = aws_cloudfront_distribution.cdn.domain_name
}

