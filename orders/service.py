from django.core.mail import send_mail


def send_mess(user_email):
    send_mail(
        'test@gmail.com',
        [user_email],
        fail_silently=False
    )