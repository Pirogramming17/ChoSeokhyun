from django.db import models

# Create your models here.
class DevTool(models.Model):
    name = models.CharField(max_length=50, verbose_name="명칭")
    kind = models.CharField(max_length=50, verbose_name="분류")
    content = models.TextField(verbose_name="설명")

class Idea(models.Model):
    title = models.CharField(max_length=50, verbose_name="제목")
    image = models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name="사진")
    content = models.TextField(verbose_name="내용")
    interest = models.IntegerField(verbose_name="관심도")
    dev_tool = models.ForeignKey(DevTool, on_delete=models.CASCADE, related_name='dev_tool')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)