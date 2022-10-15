from django.db import models
from django.contrib.auth.models import User
import datetime


class TypeChoices(models.TextChoices):
    CRANE = 'Парк кранов'
    LIFT_TRUCK = 'Парк погрузчиков'
    AUTOTOWER = 'Парк автовышек'


class Customer(models.Model):
    phone = models.CharField(
        max_length=15,
        verbose_name='Номер телефона заказчика',
        null=True,
        blank=True
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.user.phone} / {self.user.first_name} {self.user.last_name}'


class Performer(models.Model):
    fio = models.CharField(
        max_length=255,
        verbose_name='ФИО',
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=15,
        verbose_name='Номер телефона заказчика',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.phone} / {self.fio}'


class Transport(models.Model):
    class StatusChoices(models.TextChoices):
        FREE = 'FREE', 'Cвободен'
        IN_WORK = 'IN_WORK', 'В работе'
        ON_THE_WAY = 'ON_THE_WAY', 'В пути'

    type = models.CharField(
        max_length=255,
        verbose_name='Тип ТС',
        choices=TypeChoices.choices,
        null=True,
        blank=True
    )
    characteristic = models.CharField(
        max_length=255,
        verbose_name='Характеристика ТС',
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Наименование ТС',
        null=True,
        blank=True
    )
    plate_number = models.CharField(
        max_length=255,
        verbose_name='Номер ТС',
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=255,
        verbose_name='Статус ТС',
        choices=StatusChoices.choices,
        default=StatusChoices.FREE
    )
    performer = models.ForeignKey(
        Performer,
        on_delete=models.SET_NULL,
        verbose_name='Водитель ТС',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        verbose_name='Активно ли ТС',
        default=True
    )

    def __str__(self):
        return f'{self.characteristic} / статус - {self.status}'


class Reservation(models.Model):
    class StatusChoices(models.TextChoices):  # TODO: прописать статусы заявок
        IN_SEARCH = 'In the search process', 'В процессе поиска'
        VEHICLE_FOUND = 'Vehicle found', 'Транспортное средство найдено'
        CLOSED = 'Closed', 'Закрыто'

    transport = models.ForeignKey(
        Transport,
        on_delete=models.SET_NULL,
        verbose_name='Забронированный транспорт',
        null=True,
        blank=True
    )
    type = models.CharField(
        max_length=255,
        verbose_name='Тип ТС',
        choices=TypeChoices.choices,
        null=True,
        blank=True
    )
    characteristic = models.CharField(
        max_length=255,
        verbose_name='Характеристика ТС',
        null=True,
        blank=True
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Заказчик',
        null=True,
        blank=True
    )
    begin_date = models.DateField(
        verbose_name='Дата начала брони',
        default=datetime.date.today
    )
    end_date = models.DateField(
        verbose_name='Дата окончания брони',
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=255,
        verbose_name='Статус Брони',
        choices=StatusChoices.choices,
        default=StatusChoices.IN_SEARCH
    )

    def __str__(self):
        return f'{self.characteristic} / {self.end_date}-{self.end_date}'
