import pyaztro
import requests

def horiscope(date , zodicsign):
    date = date.lower()
    taurus = pyaztro.Aztro(sign=zodicsign, day=date)
    taurus.description
    return taurus.description
def fetch_conversion_factor(source,target):

    url = "https://free.currconv.com/api/v7/convert?q={}_{}&compact=ultra&apiKey=9aa0c54f5ad4c460c36d".format(source,target)

    response = requests.get(url)
    response = response.json()

    return response['{}_{}'.format(source,target)]
if __name__ == '__main__':
    import smtplib, ssl

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "my@gmail.com"  # Enter your address
    receiver_email = "your@gmail.com"  # Enter receiver address
    password = input("Type your password and press enter: ")
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)