import graphene
from graphene_django.types import DjangoObjectType
from user.attachinfo.models import AttachInfo

class AttachInfoType( DjangoObjectType ):
    class Meta:
        model = AttachInfo
        only_fields = ( 'school' , 'company' , 'location' , 'about' )

    gravatar = graphene.String()

    def resolve_gravatar( self , info , * args , ** kwargs ):
        return get_gravatar_url( self.email , size = 250 )