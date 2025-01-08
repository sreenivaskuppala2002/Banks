from django.db import models

# Create your models here.\

class Banks(models.Model):
    bank_name=models.CharField(max_length=100)
    def __str__(self):
        return self.bank_name
    
class Branch(models.Model):
    bank=models.ForeignKey(Banks,related_name='branches',on_delete=models.CASCADE)
    branch=models.CharField(max_length=100)
    IFSC=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.branch} - {self.bank.bank_name}"
    




