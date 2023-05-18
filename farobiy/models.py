from django.db import models

class Teachers(models.Model):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    image = models.ImageField(upload_to='media/farobiy/teachers')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.full_name

class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Skils(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    content = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Skil"
        verbose_name_plural = "Skils"

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    image = models.ImageField(upload_to='media/farobiy/courses')
    image_1 = models.ImageField(upload_to='media/farobiy/courses', null=True, blank=True)
    image_2 = models.ImageField(upload_to='media/farobiy/courses', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    skils = models.ManyToManyField('Skils', related_name='skills')
    teacher = models.ManyToManyField('Teachers')

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name

class MessageFromUser(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "MessageFromUser"
        verbose_name_plural = "MessageFromUsers"

    def __str__(self):
        return self.name