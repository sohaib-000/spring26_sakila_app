# ============================================================
# Author: Sohaib Shahid
# Date: 2026-05-02
# Description: Configuration file for Sakila Flask Application
# Team Member: Ahmed Khan
# Date: 2026-05-02
# Purpose: Database configuration for Sakila Flask Application
# ============================================================

import os

class Config:
    """Base configuration class for the Sakila Flask application.
    Handles database connection strings and system timeouts.
    """
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')
    CONNECTION_TIMEOUT = max(1, int(os.environ.get('CONNECTION_TIMEOUT', '30')))
    HEALTH_CHECK_INTERVAL = max(1, int(os.environ.get('HEALTH_CHECK_INTERVAL', '10')))
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here-change-this-in-production')
