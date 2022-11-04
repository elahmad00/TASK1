# from re import X
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

#from core.models import ArithmeticModel
from .serializers import ArithmeticSerializer

# Create your views here.

db = {
    "slackUsername": "Ahmaad",
    "age": 25,
    "bio": "web developer",
    "backend": True
}


def home(request):
    return JsonResponse(db)


class CreateView(APIView):

    # def get(self,request,*args, **kwargs):
    #     # post = ArithmeticModel.objects.all()
    #     # serializer = ArithmeticSerializer(post,many=True)
    #     # return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArithmeticSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            """Getting datas from submitted form"""
            a= serializer.data['a']
            b = serializer.data['b']
            optype = serializer.data['operation_type']

            """main sequence """
            if optype == "addition":
                result = a + b
            elif optype == "subtraction":
                result = a - b

            elif optype == "multiplication":
                result = a * b
                
            else:
                result = "operator not found"

            response = {"slackUsername": "Ahmaad", "result": result, "operation_type": optype}
            return Response(response)
        return Response(serializer.errors)



