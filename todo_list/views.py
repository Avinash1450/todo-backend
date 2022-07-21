from django.shortcuts import render,redirect

# Create your views here.
from rest_framework.views import APIView
from .serializers import ToDoSerializer
from .models import ToDo
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import Http404

class todolistview(APIView):


	def get(self,request):
		q = ToDo.objects.all()
		serializer = ToDoSerializer(q, many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer = ToDoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({ 'message' : 'saved succesfully'})
		return Response(serializer.errors)


class tododetailview(APIView):

	def get_queryset(self,request,pk):
		try:
			return ToDo.objects.get(pk=pk)
		except DoesnotExist:
			raise Http404


	def get(self,request,pk):
		query = self.get_queryset(request,pk)
		serializer = ToDoSerializer(query, many=False)
		return Response(serializer.data)
		
	def put(self,request,pk):
		query= self.get_queryset(request,pk)
		serializer = ToDoSerializer(query, request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)

	def delete(self,request,pk):
		query = self.get_queryset(request,pk)
		query.delete()
		return Response({ "message" : f'{query.title} has been deleted'})
