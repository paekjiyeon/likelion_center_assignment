from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='media/images/', blank = True)
    # file = models.FileField(null=True)
    image = ProcessedImageField(
            upload_to='media/images/', # 저장 위치
            processors=[ResizeToFill(600,600)], # 처리할 작업 목록
            format='JPEG', # 저장 포맷(확장자)
            options= {'quality': 90 }, # 저장 포맷 관련 옵션 (JPEG 압축률 설정)
            blank = True,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    blog_key = models.ForeignKey(Blog, on_delete = models.CASCADE, null = True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add = True)
    comment_contents = models.CharField(max_length = 200)

    class Meta:
        ordering = ['-id']

    def __str__(self):
            return self.comment_contents
