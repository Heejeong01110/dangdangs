from django.db import models

# Create your models here.

class Board(models.Model):
    title=models.TextField()
    image = models.FileField(upload_to="images/%Y/%m/%d", default='https://image.flaticon.com/icons/svg/149/149852.svg')
    pub_date=models.DateTimeField('date published')
    context=models.TextField()
    hits=models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.context[:100]

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', args=[self.id])

    @property
    def update_counter(self):
        self.hits=self.hits+1
        self.save()

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='comments')   
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_body = models.CharField(max_length=50)