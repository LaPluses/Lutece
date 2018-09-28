from django.db import models, transaction
from user.models import User
from discussion.models import Discussion
import django.utils.timezone as timezone
from discussion.models import Discussion
from uuslug import uuslug
# Create your models here.

class Article( models.Model ):
    content = models.TextField( default = '' )
    title = models.CharField( max_length = 128 , default = '' )
    user = models.ForeignKey( User , null = True ,  on_delete = models.SET_NULL )
    create_time = models.DateTimeField ( default = timezone.now )
    slug = models.CharField( blank = True , max_length = 256 )
    view = models.IntegerField( default = 0 )
    disable = models.BooleanField( default = False )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug( self.title, instance = self )
        super( Article , self ).save( * args , ** kwargs )

    class Meta:
        permissions = (
            ('view_all' , 'Can view all articles'),
        )

class ArticleDiscussion( Discussion ):
    article = models.ForeignKey( Article  , null = True , blank = True , on_delete = models.SET_NULL , db_index = True )