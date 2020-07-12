from django.db import models


# Create your models here.
class address(models.Model):
    name = models.CharField(max_length=1050)
    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
    )

    pincode = models.CharField(
        "pin / Postal code",
        max_length=12,
    )

    city = models.CharField(
        "City",
        max_length=124,
    )
    state = models.CharField(
        "sate",
        max_length=35,
    )

    def __str__(self):
        return f'{self.address1} {self.address2},{self.city},{self.state}-{self.pincode}'#self.address1 + ' ' + self.address2 + self.city

    class Meta:
        verbose_name_plural = 'address'


class delivery_agent(models.Model):
    agent_name = models.CharField(max_length=150)
    agent_address = models.ForeignKey(address, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.agent_name

    class Meta:
        verbose_name_plural = 'Delivery Agent'



class dealer(models.Model):
    name = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=14)
    address = models.ForeignKey(address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class customer(models.Model):
    name = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=15)
    address = models.ForeignKey(address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class product(models.Model):
    product_name = models.CharField(max_length=5000)
    price = models.CharField(max_length=15)
    unit = models.CharField(max_length=5000)

    def __str__(self):
        return self.product_name


class payment(models.Model):
    name = models.ForeignKey(customer, on_delete=models.CASCADE)
    cash = 'cash'
    cheque = 'cheque'
    card = 'card'
    UPI = 'UPI'
    online = 'online'

    PAYMENT_CHOICES = [
        (cash, 'cash'),
        (cheque, 'cheque'),
        (card, 'card'),
        (UPI, 'UPI'),
        (online, 'online')
    ]

    payment_type = models.CharField(
        max_length=10,
        choices=PAYMENT_CHOICES,
        default=cash,
    )
    date = models.DateField()
    amount_paid = models.CharField(max_length=150)
    paid = 'UPI'
    pending = 'ONL'

    status_CHOICES = [
        (paid, 'Success'),
        (pending, 'pending'),
    ]
    status = models.CharField(
        max_length=3,
        choices=status_CHOICES,
        default=pending
    )
    pending_amount = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return 'of ' + self.name.name


class order(models.Model):
    customer = models.ForeignKey(customer, models.CASCADE)
    product = models.ForeignKey(product, models.CASCADE)
    quantity = models.CharField(max_length=5000)
    pack1 = 'P1'
    pack2 = 'P2'
    pack3 = 'P3'
    pack4 = 'P4'
    pack5 = 'P5'

    QUANTITY_CHOICES = [
        (pack1, '250 g'),
        (pack2, '500 g'),
        (pack3, '750 g'),
        (pack4, '1 KG'),
        (pack5, '2 KG')
    ]
    unit = models.CharField(
        max_length=3,
        choices=QUANTITY_CHOICES,
        default=pack5, )
    amount = models.CharField(max_length=150)
    order_date = models.DateField()
    supplied_date = models.DateField()

    def __str__(self):
        return self.customer.name


class expense(models.Model):
    agent_name = models.ForeignKey(delivery_agent, on_delete=models.CASCADE)
    shipping = 'shipping'
    fuel = 'fuel'

    expense_CHOICES = [
        (fuel, 'fuel'),
        (shipping, 'shipping')
    ]

    expense_category = models.CharField(
        max_length=8,
        choices=expense_CHOICES,
        default=shipping,
    )
    amount = models.CharField(max_length=5000)
    date = models.DateField()
    paid_on = models.DateField(blank=True)

    def __str__(self):
        return self.agent_name.agent_name
