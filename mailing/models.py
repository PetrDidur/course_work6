from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Client(models.Model):
    """
    Клиент сервиса:
    контактный email,
    ФИО,
    комментарий.
    """
    email = models.EmailField(max_length= 150, verbose_name='email'),
    full_name = models.CharField(max_length=50, verbose_name='ФИО'),
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return f'{self.full_name} - {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mailing(models.Model):
    """
    Рассылка (настройки):
    время рассылки;
    периодичность: раз в день, раз в неделю, раз в месяц;
    статус рассылки: завершена, создана, запущена.
    """

    def __str__(self):
        return f'{self.client, self.message_theme, self.send_time}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

    message_theme = models.CharField(max_length='300', verbose_name='тема письма'),
    message_text = models.TextField(verbose_name='текст письма'),

    send_time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время рассылки'),

    daily = models.BooleanField(verbose_name='ежедневно', default=False, **NULLABLE),
    weekly = models.BooleanField(verbose_name='еженедельно', default=False, **NULLABLE),
    monthly = models.BooleanField(verbose_name='ежемесячно', default=False, **NULLABLE),

    is_finished = models.BooleanField(verbose_name='завершена', default='False', **NULLABLE),
    is_created = models.BooleanField(verbose_name='создана', default=False, **NULLABLE),
    is_started = models.BooleanField(verbose_name='запущена', default=False, **NULLABLE),

    client = models.ForeignKey(Client, verbose_name='клиент', on_delete=models.CASCADE)