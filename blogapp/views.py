from django.shortcuts import render
from blogapp.models import BlogModel
from django.http import JsonResponse
from django.views import View
from .helpers import GetBody

import json
from django.core.serializers import serialize

# for working with djangorestframework serializer
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    # main query for index route
    queryset = BlogModel.objects.all()
    # class to serialize the output
    serializer_class = PostSerializer
    # optional permission class. Sets permission level to allow all vs. [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

# Create your views here.
# class BlogView(View):
#     # Index to show all blog posts
#     def get(self, request):
#         all = BlogModel.objects.all()
#         serialized = serialize("json", all)
#         finalData = json.loads(serialized)
#         return JsonResponse(finalData, safe=False)
#     # Create a blog post
#     def post(self, request):
#         body = GetBody(request)
#         print(body)
#         blogPost = BlogModel.objects.create(title=body["title"], body=body["body"])
#         finalData = json.loads(serialize("json", [blogPost]))
#         return JsonResponse(finalData, safe=False)

# # just to show we can accept query params
# class BlogViewId(View):
#     # Show just 1 post/:id
#     def get(self, request, id):
#         blogPost = BlogModel.objects.get(id=id)
#         finalData = json.loads(serialize("json", [blogPost]))
#         return JsonResponse(finalData, safe=False)
    
#     # PUT, update 1 post/:id
#     def put(self, request, id):
#         body = GetBody(request)
#         BlogModel.objects.filter(id=id).update(**body)
#         # get the updated post
#         blogPost = BlogModel.objects.get(id=id)
#         finalData = json.loads(serialize("json", [blogPost]))
#         return JsonResponse(finalData, safe=False)
    
#     # DEL 1 post/:id
#     def delete(self, request, id):
#         blogPost = BlogModel.objects.get(id=id)
#         blogPost.delete()
#         finalData = json.loads(serialize("json", [blogPost]))
#         return JsonResponse(finalData, safe=False)
    

# # for form data
# class ThirdView(View):
#     def post(self, request):
#         return JsonResponse(GetBody(request))
