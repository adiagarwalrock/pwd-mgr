from django.db import models

# Create your models here.
class Email(models.Model):
    email = models.EmailField(max_length=255, blank=False, null=False, default="abc@example.com", unique=True)
    alias = models.CharField(max_length=255, blank=False, null=False, default="")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)


class Service(models.Model):
    service = models.CharField(max_length=255, blank=False, null=False, default="", unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.service)


class Password(models.Model):
    password = models.CharField(max_length=255, blank=False, null=False, default="")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.password)


class Username(models.Model):
    username = models.CharField(max_length=255, blank=False, null=False, default="")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)


class PasswordService(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    password = models.ForeignKey(Password, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    username = models.ForeignKey(Username, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.password) + " | " + str(self.service)