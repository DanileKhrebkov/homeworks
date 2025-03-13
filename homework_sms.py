import logging
from datetime import datetime

# Настройка логов
logging.basicConfig(filename='notifications.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def send_email(message):
    print(f"Sending email: {message}")
    logging.info(f"Email sent: {message}")

def send_sms(message):
    print(f"Sending SMS: {message}")
    logging.info(f"SMS sent: {message}")

def send_notification(notification_type, callback, message):
    if notification_type not in ["email", "sms"]:
        print("Unknown notification type")
        logging.error(f"Unknown notification type: {notification_type}")
        return
    callback(message) # Вызов колбэка для отправки уведомления

# Пример использования
send_notification("email", send_email, "Hello! This is an email notification.")
send_notification("sms", send_sms, "Hello! This is an SMS notification.")
send_notification("push", send_email, "This should not be sent.")  # Неизвестный тип