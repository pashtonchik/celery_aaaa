from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from celery_test.celery import test_task_1


@api_view(["GET"])
def aaa(request):
    test_task_1.delay()
    return Response(status=status.HTTP_200_OK, data={"ok": True})