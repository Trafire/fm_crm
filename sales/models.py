from django.db import models


class SalesPerson(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cell_number = models.CharField(max_length=32)
    email_adress = models.CharField(max_length=200)
    salesperson_code = models.CharField(max_length=10)


class Client(models.Model):
    store_name = models.CharField(max_length=200)
    f2code_client = models.CharField(max_length=6)
    salesperson = models.ForeignKey(SalesPerson, on_delete=models.CASCADE)


class Results(models.Model):
    result = models.CharField(max_length=200)

    def __str__(self):
        return self.result


class ContactType(models.Model):
    contact_type = models.CharField(max_length=200)

    def __str__(self):
        return self.contact_type


class Calls(models.Model):
    date = models.DateTimeField()
    contact_type = models.ForeignKey(ContactType, on_delete=models.CASCADE)
    result = models.ForeignKey(Results, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.contact_type}ed and recieved {self.result}"



