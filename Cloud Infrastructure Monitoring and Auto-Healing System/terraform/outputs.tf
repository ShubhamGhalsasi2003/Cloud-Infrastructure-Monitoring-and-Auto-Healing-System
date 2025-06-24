output "instance_id" {
  value = aws_instance.web.id
}

output "lambda_function_name" {
  value = aws_lambda_function.autoheal.function_name
}