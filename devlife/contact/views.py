from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from devlife.contact.models import Contact
from devlife.contact.serializers import ContactSerializer
from rest_framework import status
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView

def contact_page(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
          return render(request,'contact/contact.html')
    else:
        return redirect('/login')


class ContactData(APIView):
    """
    Managing contact through serializers via GET, POST, DELETE & UPDATE methods
    """
    def get(self, request):
        if request.user.is_authenticated():   # When user is authenticated
            contacts = Contact.objects.all().filter(user=request.user.id)
            contacts_serialized = ContactSerializer(contacts, many=True)
            return Response(contacts_serialized.data)
        else:
            return Response("You are not authorized to access!")
    
    def post(self, request):
        if request.user.is_authenticated():   # When user is authenticated
            dict_data = request.data
            dict_data['user'] = request.user.id
            serializer = ContactSerializer(data=dict_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else: 
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else: # When user is not authenticated 
            return Response("You are not authorized to access!")



class ContactDetail(APIView):
    def get(self, request, pk):
        if request.user.is_authenticated():   # When user is authenticated
            try:
                contact_serialized = ContactSerializer(Contact.objects.get(pk=pk, user=request.user.id))
                return Response(contact_serialized.data)
            except Exception:
                return Response("You are not authorized to access!")
        else:
            return HttpResponse("You are not authorized to access!")

