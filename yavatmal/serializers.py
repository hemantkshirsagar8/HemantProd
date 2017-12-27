from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import *

class T_QuestionsSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = T_QuestionsSet
        fields = '__all__'



