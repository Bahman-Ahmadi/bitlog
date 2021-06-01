from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	STATUS_CHOICES = {("d","پیش‌نویس"),("p","منتشر شده")}
	title = models.CharField(max_length=200, verbose_name = "عنوان")
	slug = models.SlugField(max_length=100, unique=True,verbose_name= "لینک")
	note = models.TextField(verbose_name="محتوا")
	img = models.ImageField(upload_to="images", verbose_name="تصویر")
	pubTime = models.TimeField(default=timezone.now, verbose_name="زمان انتشار")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت انتشار")
	
	class Meta:
		verbose_name = "پست"
		verbose_name_plural = "پست"

	def __str__(self):
		return self.title