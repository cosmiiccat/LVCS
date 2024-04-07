from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from utils import custom_exceptions
from django.http import JsonResponse
from . import lvcs_client
from rest_framework.decorators import api_view

import json
import os


# Create your views here.
@api_view(['GET'])
def ensure(request):
    try:
        if request.method != "GET":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        response = {"success": "true", "status": "online"}
        return JsonResponse(response)
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})

@csrf_exempt
@api_view(['POST'])
def config(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["path", "username", "email"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        resp = lvcs_client.config(
            path=req_data["path"],
            username=req_data["username"],
            email=req_data['email']
        )   

        return JsonResponse({"success":"true", "data":resp['data']})

    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})

@csrf_exempt
@api_view(['POST'])
def init(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["path"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        resp = lvcs_client.init(
            path=req_data["path"]
        )   

        return JsonResponse({"success":"true", "data":resp['data']})

    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    
@csrf_exempt
@api_view(['POST'])
def add(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["path"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        resp = lvcs_client.commit(
            path=req_data["path"]
        )   

        return JsonResponse({"success":"true", "data":resp['data']})

    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    
@csrf_exempt
@api_view(['POST'])
def commit(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["path", "commit_message"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        resp = lvcs_client.commit(
            path=req_data["path"],
            commit=True,
            commit_message=req_data['commit_message']
        )   

        return JsonResponse({"success":"true", "data":resp['data']})

    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    
@csrf_exempt
@api_view(['POST'])
def pull(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["path"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        resp = lvcs_client.pull(
            path=req_data["path"],
        )   

        return JsonResponse({"success":"true", "data":resp['data']})

    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})