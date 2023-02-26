from django.db import models
from django.contrib.auth.models import User
import datetime
from ethiopian_date.ethiopian_date import EthiopianDateConverter
def ConvertDate():
    today_date =EthiopianDateConverter.date_to_ethiopian(datetime.date.today())
    if(len(str(today_date[1])) < 2 ):
        return f"{today_date[0]}-0{today_date[1]}-{today_date[2]}"
    else:
        return f"{today_date[0]}-{today_date[1]}-{today_date[2]}"

# Create your models here.
class Schedule(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=25)
    work =models.CharField(max_length=179)
    grade= models.CharField(max_length=10,blank=True)
    date =models.DateField(default=ConvertDate,blank=True)
