from django.db import models



class Post(models.Model):
    
    fromWho = models.CharField(max_length=30,verbose_name='Kim tarafından ')
    description = models.CharField(max_length=135,verbose_name='Açıklama')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='Paylaşılma zamanı')
    likeCount = models.IntegerField(verbose_name='Beğeni sayısı')
    commentCount = models.IntegerField(verbose_name='Yorum sayısı')
