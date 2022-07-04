from django.db import models

# Create your models here.

class IndexPage(models.Model):
    img1 = models.ImageField('HomePage img1', upload_to='media', null=True)
    img2 = models.ImageField('HomePage img2', upload_to='media', null=True)
    img3 = models.ImageField('HomePage img3', upload_to='media', null=True)
    name1 = models.CharField('HomePage name1', max_length=50, null=True)
    name2 = models.CharField('HomePage name2', max_length=60, null=True)
    name3 = models.CharField('HomePage name3', max_length=70, null=True)
    about = models.TextField('HomePage about', null=True)
    number = models.CharField('HomePage number', max_length=30, null=True)

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'


class About(models.Model):
    drName = models.CharField('Dr. name', max_length=50)
    about = models.CharField('About Dr. ', max_length=250)
    years = models.CharField('Years ', max_length=250)


    def __str__(self):
        return self.drName

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'





class Timeline(models.Model):
    name = models.CharField('Name', max_length=50)
    Abuout = models.CharField('Abuout', max_length=50)
    data = models.CharField('Abuout', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Timeline'
        verbose_name_plural = 'Timelines'



class Testimonials(models.Model):
    opinion1 = models.CharField('Customer feedback ֊ 1', max_length=250)
    opinion2 = models.CharField('Customer feedback ֊ 2', max_length=250)
    nameCustomer = models.CharField('Customer name', max_length=50)
    aboutCustomer = models.CharField('About Customer', max_length=250)
    img = models.ImageField('Customer image', upload_to='media')

    def __str__(self):
        return self.nameCustomer

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'








# class IndexPage(models.Model):
#     name = models.CharField('Header', max_length=50)
#     about = models.CharField('About Template', max_length=50)
#     phoneNumber = models.CharField('Phone nomber', max_length=50)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'IndexPage'
#         verbose_name_plural = 'IndexPages'


# class IndexPageSlayder(models.Model):
#     slayderWorlds = models.CharField('Header', max_length=50)

#     def __str__(self):
#         return self.slayderWorlds

#     class Meta:
#         verbose_name = 'IndexPageSlayder'
#         verbose_name_plural = 'IndexPageSlayders'