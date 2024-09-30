from django.db.models import Count
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import People, TGPeople
from .serializers import TGPeopleSerializerM2M, TGPeopleIDSerializer


def stats(request):
    users_with_invites = TGPeople.objects.annotate(invite_count=Count('invited_friends')).filter(
        invite_count__gt=0).order_by('-invite_count')
    total_users = TGPeople.objects.count()
    return render(request, 'stats.html', {'users': users_with_invites, 'total_users': total_users})


@api_view(["POST"])
def add_people(request):
    name = request.data["name"]
    phone_number = request.data["phone_number"]
    People.objects.create(name=name, phone_number="+998" + phone_number)
    return Response(
        {"status": "ok", "link": "https://t.me/+-_RM8SFzgm9kZjBi"},
        status=status.HTTP_201_CREATED,
    )


@api_view(["POST"])
def add_tg_people(request):
    id = request.data["id"]
    name = request.data["name"]
    TGPeople.objects.create(id=id, name=name)
    return Response(
        {"status": "ok"},
        status=status.HTTP_201_CREATED,
    )


@api_view(["POST"])
def invite_tg_people(request):
    id = request.data["id"]
    friend_id = request.data["friend_id"]
    friend_name = request.data["friend_name"]
    if id == friend_id:
        return Response(
            {"status": "false", "detail": "you can't invite yourself!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        TGPeople.objects.get(id=id).invite(friend_id, friend_name)
    except Exception as e:
        return Response(
            {"status": "false", "detail": str(e)}, status=status.HTTP_400_BAD_REQUEST
        )
    return Response(
        {"status": "ok", "detail": f"you have invited {friend_id}"},
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
def get_tg_people(request, id: str):
    try:
        people = TGPeople.objects.get(id=id)
        data = TGPeopleSerializerM2M(people).data
    except Exception as e:
        return Response(
            {"status": "false", "detail": str(e)}, status=status.HTTP_400_BAD_REQUEST
        )
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_people_ids(request):
    people_ids = TGPeopleIDSerializer(TGPeople.objects.all(), many=True)
    return Response({"status": "true", "people": people_ids.data})
