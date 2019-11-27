from django.db import models
from user.models import User

# Create your models here.
class Post(models.Model):
    class Meta:
        db_table='post'
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=256,null=False)
    postdate=models.DateField(null=False)
    author=models.ForeignKey(User,on_delete=True)
    def __repr__(self):
        return '<Post {} {} {} {}>'.format(self.id,self.title,self.postdate,self.author)
class Content(models.Model):
    class Meta:
        db_table='content'
    post=models.OneToOneField(Post,on_delete=True)
    content=models.TextField(null=False)
    def __repr__(self):
        return '<Cotent {} {}>'.format(self.post,self.content)