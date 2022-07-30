from django.conf import settings
from django.core.mail import send_mail
from django.template import loader


def send(subject, to_email, template_name):
    html_template = loader.get_template(f'{template_name}.html')
    html_message = html_template.render()

    txt_template = loader.get_template(f'{template_name}.txt')
    text_message = txt_template.render()

    send_mail(
        subject=subject,
        message=text_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        html_message=html_message
    )
