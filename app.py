import smtplib
import sys
import csv


class SmtpAuth():
    def __init__(self, host: str, port: int = 587, use_tls: bool = False) -> None:
        self.host = host
        self.port = port
        self.use_tls = use_tls

    def request(self, user: str, password: str) -> bool:
        with smtplib.SMTP(host=self.host, port=self.port) as smtp:

            if self.use_tls:
                smtp.starttls()

            smtp.login(user, password)


if __name__ == '__main__':
    args = sys.argv
    host = args[1]
    csv_file = args[2]

    smtp_auth = SmtpAuth(host)

    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                smtp_auth.request(row[0], row[1])
                print(row[0], 'success')
            except Exception as e:
                print(row[0], str(e))
