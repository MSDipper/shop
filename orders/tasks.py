from config.celery import app
from django.core.mail import send_mail
from .models import Order


@app.task
def order_created(order_id):
    """ Задача для отправки уведомления по электронной почте при успешном создании заказа. """
    order = Order.objects.get(id=order_id)
    subject = 'Номер заказа. {}'.format(order_id)
    message = 'Дорогой {},\n\nВы успешно разместили заказ.\
                Идентификатор вашего заказа {}.'.format(order.first_name,
                                             order.id)
    mail_sent = send_mail(subject,
                          message,
                          'batsaev0507@gmail.com',
                          [order.email])
    return mail_sent