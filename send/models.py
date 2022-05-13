

#from phonenumber_field.modelfields import PhoneNumberField

from django.core.validators import RegexValidator
from django.utils import timezone
from django.db import models

class Distribution(models.Model):
    date_time_start = models.DateTimeField(verbose_name='Start mailing')
    date_time_end = models.DateTimeField(verbose_name='Start mailing')
    text = models.CharField(max_length=150)
    mobile_codes = models.CharField('Operator code', max_length=50, blank=True)
    tags = models.CharField('Tags', max_length=50, blank=True)

    @property
    def to_send(self):
        now = timezone.now()
        if self.date_time_start <= now <= self.date_time_end:
            return True
        else:
            return False

    @property
    def sent_messages(self):
        return len(self.messages.filter(status='sent'))

    @property
    def messages_to_send(self):
        return len(self.messages.filter(status='proceeded'))

    @property
    def unsent_messages(self):
        return len(self.messages.filter(status='failed'))

    def __str__(self):
        return f'Рассылка {self.id} от {self.date_time_start}'

    class Meta:
        verbose_name = 'Distribution'
        verbose_name_plural = 'Distributions'


class Client(models.Model):
    phone_regex = RegexValidator(regex=r'^7\w{10}$')
    phone_number = models.PositiveIntegerField(verbose_name='phone_number', validators=[phone_regex])
    #phone_number = PhoneNumberField()
    phone_operator = models.CharField(max_length=50, verbose_name='phone_operator')
    #phone_operator = PhoneNumberField()
    teg = models.CharField(verbose_name='tag', max_length=50, blank=True)
    time_zone = models.TimeField(verbose_name='time_zone', max_length=10)
    def __str__(self):
        return f'Client {self.id} phone_number {self.phone_number}'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'



class Message(models.Model):
    SENT = "sent"
    PROCEEDED = "proceeded"
    FAILED = "failed"

    STATUS_CHOICES = [
        (SENT, "Sent"),
        (PROCEEDED, "Proceeded"),
        (FAILED, "Failed"),
    ]

    date_time_start_message = models.DateTimeField(auto_now_add=True)
    status_message = models.CharField(max_length=50, choices=STATUS_CHOICES)
    distribution = models.ForeignKey(to=Distribution, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)


    def __str__(self):
        return f'Message {self.id} text {self.distribution} for {self.client}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'









