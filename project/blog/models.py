from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Blog(models.Model):
    author = models.ForeignKey(User, editable = False, null=True, blank=True, on_delete=models.SET_NULL,)
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
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="like_user_set", through='Like')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
    
    @property
    def like_count(self):
        return self.like_user_set.count()

class Comment(models.Model):
    blog_key = models.ForeignKey(Blog, on_delete = models.CASCADE, null = True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add = True)
    comment_contents = models.CharField(max_length = 200)

    class Meta:
        ordering = ['-id']

    def __str__(self):
            return self.comment_contents

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = (('user', 'blog'))