from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    bio = models.TextField()
    image = models.ImageField(upload_to='user_image/')
    website = models.URLField()

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follower_user')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following_user')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower} - {self.following}'

class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_image')
    video = models.ImageField(upload_to='post_video')
    description = models.TextField()
    hashtag = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.description} - {self.hashtag}'

class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.post}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post} - {self.user} - {self.text}'

class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.comment}'

class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='story_image/')
    video = models.ImageField(upload_to='story_video/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class Save(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class SaveItem(models.Model):
    post = models.ForeignKey(Save, on_delete=models.CASCADE, related_name='item')
    save = models.ForeignKey(Save, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post} - {self.save}'