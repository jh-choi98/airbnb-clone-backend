from django.db import models
from common.models import CommonModel


class Room(CommonModel):
    """Room Model Definition"""

    class RoomTypeChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    country = models.CharField(
        max_length=50,
        default="Canada",
    )
    city = models.CharField(
        max_length=80,
        default="Waterloo",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=100,
    )
    pet_allowed = models.BooleanField(
        default=True,
    )
    room_type = models.CharField(
        max_length=20,
        choices=RoomTypeChoices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
    )


class Amenity(CommonModel):
    """Amenity Model Definition"""

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null=True)
