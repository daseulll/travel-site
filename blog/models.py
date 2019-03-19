from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(
        upload_to='blog/image',
        blank=True,
        verbose_name='Image',
        )
    image_thumbnail = ProcessedImageField(
        upload_to='blog/thumbnail',
        processors=[Thumbnail(120, 120)],
        format='jPEG',
        options={'qulity' : 100},
        verbose_name="대표이미지",
        blank=True,
    )
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True,
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
        
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
    author = models.CharField(max_length=200)
    text = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return "{}에 작성됨 - {} : {} ".format(self.post.title, self.author, self.text)
