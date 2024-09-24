import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email(message):
    """Переменные для почты"""
    SENDER = os.getenv("SENDER")
    PASSWORD = os.getenv("PASSWORD")
    RECIPIENT = os.getenv("RECIPIENT")
    # хост и порт
    print(SENDER,RECIPIENT)
    # server = smtplib.SMTP("smtp.gmail.com", 587)
    server = smtplib.SMTP("smtp.mail.ru", 587)
    server.starttls()
    try:
        """блок отправки сообщения"""
        server.login(SENDER, PASSWORD)
        msg = MIMEText(message)  # Переменная для форматирования письма на кириллице
        # msg["Subject"] = "Tema for message"
        # server.sendmail(SENDER,RECIPIENT,f"Subject:Tema message!\n{message}")# (отправитель, получатель, сообщение)можно без темы(для англ букв)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())  # для кириллици
        return "Done"
    except Exception as _ex:
        """Ответ в случае не выполнения блока try"""
        return f"{_ex}\nCheck your login and PASSWORD!"


def main():
    message = input("Введите текст сообщения: ")
    print(send_email(message=message))


if __name__ == '__main__':
    main()
