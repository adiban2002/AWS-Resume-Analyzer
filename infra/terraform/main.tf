################################
# S3 FRONTEND BUCKET
################################

resource "aws_s3_bucket" "frontend_bucket" {

  bucket = var.frontend_bucket_name

  force_destroy = true

  tags = {
    Name        = "resume-analyzer-frontend"
    Environment = "dev"
  }

  lifecycle {
    prevent_destroy = true
  }
}

################################
# S3 STORAGE BUCKET
################################

resource "aws_s3_bucket" "storage_bucket" {

  bucket = var.storage_bucket_name

  force_destroy = true

  tags = {
    Name        = "resume-analyzer-storage"
    Environment = "dev"
  }

  lifecycle {
    prevent_destroy = true
  }
}

################################
# DYNAMODB TABLE
################################

resource "aws_dynamodb_table" "resume_analysis" {

  name         = var.dynamodb_table_name
  billing_mode = "PAY_PER_REQUEST"

  hash_key = "analysis_id"

  attribute {
    name = "analysis_id"
    type = "S"
  }

  tags = {
    Name        = "resume-analysis-table"
    Environment = "dev"
  }

  lifecycle {
    prevent_destroy = true
  }
}

################################
# EC2 INSTANCE
################################

resource "aws_instance" "api_server" {

  ami           = var.ec2_ami
  instance_type = var.ec2_instance_type

  tags = {
    Name        = "resume-analyzer-api"
    Environment = "dev"
  }

  lifecycle {
    prevent_destroy = true
  }
}

################################
# CLOUDFRONT CDN
################################

resource "aws_cloudfront_distribution" "cdn" {

  enabled = true

  origin {
    domain_name = aws_s3_bucket.frontend_bucket.bucket_regional_domain_name
    origin_id   = "s3-origin"

    s3_origin_config {
      origin_access_identity = ""
    }
  }

  default_cache_behavior {

    target_origin_id       = "s3-origin"
    viewer_protocol_policy = "redirect-to-https"

    allowed_methods = [
      "GET",
      "HEAD"
    ]

    cached_methods = [
      "GET",
      "HEAD"
    ]

    forwarded_values {

      query_string = false

      cookies {
        forward = "none"
      }
    }
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }

  tags = {
    Name        = "resume-analyzer-cdn"
    Environment = "dev"
  }
}