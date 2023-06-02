import graphene
from graphene_django import DjangoObjectType,DjangoListField
from .models import SettingUser


class SettingUserType(DjangoObjectType):#describe the model
    class Meta :
        model = SettingUser
        fields = ('id','first_name','last_name','city','email')


class Query(graphene.ObjectType):

    all_users = graphene.List(SettingUserType,id = graphene.Int())

    # all_users = DjangoListField(SettingUserType)

    def resolve_all_users(root,info,id):
        return SettingUser.objects.get(pk=id)


    


schema = graphene.Schema(query=Query)