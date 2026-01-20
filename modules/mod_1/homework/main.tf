terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.8.0"
    }
  }
}

# Connect to gcp using ADC (identity verification)
provider "google" {
  project = var.project
  region  = var.region
  zone    = var.zone
}

# This data source gets a temporary token for the service account
data "google_service_account_access_token" "default" {
  provider               = google
  target_service_account = "terraform-proxy@project-791f23ef-cd77-4fab-a72.iam.gserviceaccount.com"
  scopes                 = ["https://www.googleapis.com/auth/cloud-platform"]
  lifetime               = "3600s"
}

# This second provider block uses that temporary token and does the real work
provider "google" {
  alias        = "impersonated"
  access_token = data.google_service_account_access_token.default.access_token
  project      = var.project
  region       = var.region
  zone         = var.zone
}


resource "google_storage_bucket" "data-lake-bucket" {
  name     = "dataeng-hw1-bucket"
  location = var.location

  storage_class               = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 7 // days
    }
  }

  force_destroy = true
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id = "sample_data"
  project    = var.project
  location   = var.location
}
