from django.db import models


class MsgPost(models.Model):
    user = models.CharField(max_length=12)
    title = models.CharField(max_length=30)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
