from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
from .validator import val_email

class Guru(models.Model):
    nipguru = models.IntegerField(
        validators=[MaxValueValidator(999999999999)]
    )
    namaguru = models.CharField(max_length=50)

    jk = (
        ('Pria', 'Pria'),
        ('Wanita', 'Wanita')
    )
    kelaminguru = models.CharField(max_length=10,choices = jk)
    alamatguru  = models.TextField()
    tanggallahir  = models.DateField()
    hpguru = models.CharField(max_length=15)
    email = models.EmailField(
        default='example@mail.id',
        validators = [val_email]
    
    )
    photoguru = models.CharField(max_length=100, default='noimage.png')
    jenjang = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=50)
    namakampus = models.CharField(max_length=50)

    def __str__(self):
        return "{}. {}".format(self.id, self.namaguru)
    
    
class Sekolah(models.Model):
    npsn = models.IntegerField(),
    namasekolah = models.CharField(max_length=50),
    nis = models.CharField(max_length=50),
    nss = models.CharField(max_length=50),
    prov = models.CharField(max_length=50),
    kab = models.CharField(max_length=50),
    kec = models.CharField(max_length=50),
    kel = models.CharField(max_length=50),
    hp = models.CharField(max_length=50),
    email = models.CharField(max_length=50),
    web = models.CharField(max_length=50),

    def __str__(self):
        return "{}".format(self.namasekolah)