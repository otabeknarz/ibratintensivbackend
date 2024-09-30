from django.db import models


class People(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class TGPeople(models.Model):
    id = models.CharField(max_length=40, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    invited_friends = models.ManyToManyField(
        "self", null=True, blank=True, symmetrical=False, related_name="parents"
    )

    def __str__(self) -> str:
        return self.name

    def invite(self, friend_id: str, friend_name: str) -> None:
        if TGPeople.objects.filter(id=friend_id).exists():
            raise ValueError(f'{friend_name} has already registered.')

        friend = TGPeople.objects.create(id=friend_id, name=friend_name)

        self.invited_friends.add(friend)
        self.save()
