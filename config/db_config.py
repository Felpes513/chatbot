import os

db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', '2210'),
    'database': os.getenv('DB_NAME', 'chatbotbd')
}
