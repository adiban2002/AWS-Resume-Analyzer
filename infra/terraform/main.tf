################################
# S3 FRONTEND BUCKET
################################

resource "aws_s3_bucket" "frontend_bucket" {

  bucket = var.frontend_bucket_name

  tags = {
    Name = "resume-analyzer-frontend"
  }
}

################################
# S3 STORAGE BUCKET
################################

resource "aws_s3_bucket" "storage_bucket" {

  bucket = var.storage_bucket_name

  tags = {
    Name = "resume-analyzer-storage"
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
    Name = "resume-analysis-table"
  }
}

################################
# EC2 INSTANCE
################################

resource "aws_instance" "api_server" {

  ami           = "ami-051a31ab2f4d498f5"
  instance_type = var.ec2_instance_type

  tags = {
    Name = "resume-analyzer-test-instance"
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
  }

  default_cache_behavior {

    target_origin_id = "s3-origin"

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

  # REQUIRED BLOCK
  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }
}
################################
# SAGEMAKER ENDPOINT CONFIG (DISABLED)
################################

# resource "aws_sagemaker_endpoint_configuration" "endpoint_config" {
#
#   name = "resume-analyzer-endpoint-config"
#
#   production_variants {
#
#     variant_name           = "AllTraffic"
#     model_name             = aws_sagemaker_model.resume_model.name
#     instance_type          = "ml.t2.medium"
#     initial_instance_count = 1
#   }
# }

################################
# SAGEMAKER ENDPOINT (DISABLED)
################################

# resource "aws_sagemaker_endpoint" "resume_endpoint" {
#
#   name                 = "resume-analyzer-endpoint"
#   endpoint_config_name = aws_sagemaker_endpoint_configuration.endpoint_config.name
# }