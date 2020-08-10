from django.core.mail import send_mail
from django.template import loader

from pre_term.settings import *


def send_email_activate(username, receive, u_token):
    subject = '%s BooMPlay Active' % username

    from_email = EMAIL_HOST_USER

    recipient_list = [receive, ]

    data = {
        'username': username,
        'activate_url': 'http://{}:{}/web/activate/?u_token={}'.format(SERVER_HOST, SERVER_PORT, u_token),
    }

    html_message = loader.get_template('user/activate.html').render(data)

    send_mail(subject=subject, message="", html_message=html_message, from_email=from_email,
              recipient_list=recipient_list)
