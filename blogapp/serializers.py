from .models import BlogModel
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # the model it will serialize
        model = BlogModel
        # fields to be included in the serialized ouput
        fields = ['id', 'title', 'body']