
provider "aws" {
  region = "us-west-2"
}

resource "aws_key_pair" "etl_key" {
  key_name   = "etl-key"
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "aws_security_group" "etl_sg" {
  name = "etl-sg"
  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port = 5432
    to_port = 5432
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port = 8080
    to_port = 8080
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "etl" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = aws_key_pair.etl_key.key_name
  vpc_security_group_ids = [aws_security_group.etl_sg.id]
  tags = { Name = "ETL-Server" }
}

resource "aws_db_instance" "postgres" {
  identifier        = "etl-db"
  engine            = "postgres"
  instance_class    = "db.t3.micro"
  username          = "postgres"
  password          = "postgrespassword"
  allocated_storage = 20
  skip_final_snapshot = true
  publicly_accessible = true
  vpc_security_group_ids = [aws_security_group.etl_sg.id]
}
