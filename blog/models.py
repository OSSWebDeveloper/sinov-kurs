from django.db import models

# Create your models here.

class Post(models.Model):
    JAXON = 'jaxon'
    OZBEKISTON = 'ozbekiston'
    IQTISOD = 'iqtisod'
    CHOISE_GROUP = {
        (JAXON , 'jaxon'),
        (OZBEKISTON , 'ozbekiston'),
        (IQTISOD , 'iqtisod'),
    }

    title = models.CharField('Sarlavha', max_length=150)
    img = models.ImageField('Surat' )
    des = models.TextField("Kengaytma")
    date = models.DateTimeField("Yuklangan sana", auto_now_add=True)
    price = models.IntegerField("Narx $da" , default=1)
    group = models.CharField(max_length=100 , choices=CHOISE_GROUP , default=OZBEKISTON)
    chiqish = models.BooleanField('Ekranga chiqsinmi?' , default=True)

    class Meta :
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'

    def __str__(self) -> str:
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    author_name = models.CharField('Foydalanuvchi', max_length = 50)
    comment_text = models.TextField('Kommentariya', max_length=1000)


    class Meta:
        verbose_name = 'Kommentariya'
        verbose_name_plural = 'Kommentariyalar'
