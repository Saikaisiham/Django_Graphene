from django.urls import path
from . import views
from graphene_django.views import GraphQLView
from base.schema import schema

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),  # Add a view function or class here
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
