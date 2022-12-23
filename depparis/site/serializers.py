import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


class IndexSerializer(serializers.ModelSerializer):
        class Meta:
                model = Service_cat
                fields = "__all__"


class PersonalSerializer(serializers.ModelSerializer):
        class Meta:
                model = Personal
                fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
        #username = serializers.CharField()
        #phone = serializers.CharField()
        #email = serializers.EmailField()
        #password1 = serializers.CharField()
        #password2 = serializers.CharField()
        class Meta:
                model = Personal
                fields = "__all__"


class FeedbackSerializer(serializers.Serializer):
        name = serializers.CharField()
        email = serializers.EmailField()
        theme = serializers.CharField()
        message = serializers.CharField()
        phone = serializers.CharField()
