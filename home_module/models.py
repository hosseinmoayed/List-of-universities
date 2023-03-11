from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.




class Country(models.Model):
    name = models.CharField(max_length=200 , verbose_name='نام کشور')



class City(models.Model):
    name = models.CharField(max_length=200 , verbose_name='نام شهر')
    country = models.ForeignKey(Country , on_delete=models.CASCADE)


class University(models.Model):
    class Type_options(models.TextChoices):
        private = 'private' , 'خصوصی'
        non_private = 'non_private' , 'غیرخصوصی'

    city = models.ForeignKey(City , on_delete=models.CASCADE)
    name = models.CharField(max_length=200 , verbose_name='نام دانشگاه')
    acronym = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='image/uni_logo' , null=True , blank=True , verbose_name='لوگو')
    type = models.CharField(max_length=50, choices=Type_options.choices, verbose_name="نوع")
    overview = models.TextField()
    established_year = models.DateField(verbose_name='سال تاسیس')
    number_of_students = models.IntegerField(verbose_name='تعداد کل دانشجو')
    number_of_international_students = models.IntegerField(verbose_name='تعداد کل دانشجویان بین المللی')
    url_uni_address = models.URLField(verbose_name='لینک سایت دانشگاه')
    acceptance_rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)] , verbose_name='ریت پذیرش')

