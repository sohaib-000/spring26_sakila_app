# ============================================================
# Author: Ahmed Khan
# Team Member
# Date: 2026-05-02
# Purpose: Database configuration for Sakila Flask Application
# ============================================================

import os

class Config:
    """Base configuration class for the Sakila Flask application.
    Handles database connection strings and system timeouts.
    """
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db-primary')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here-change-this-in-production')
