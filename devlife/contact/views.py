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

def contact_page(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
          return render(request,'contact/contact.html')
    else:
        return redirect('/login')

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def contact_data(request):
    if request.user.is_authenticated():   # When user is authenticated
        if request.method == 'GET':         # For viewing records
            contacts = Contact.objects.all().filter(user=request.user.id)
            contacts_serialized = ContactSerializer(contacts, many=True)
            return JsonResponse(contacts_serialized.data, safe=False,)
        elif request.method == 'POST':      # For creating a record
            dict_data = request.data
            dict_data['user'] = request.user.id
            serializer = ContactSerializer(data=dict_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':    # For deleting a record
            pass
    else: # When user is not authenticated 
        return HttpResponse("You are not authorized to access!")

# Create your views here.
