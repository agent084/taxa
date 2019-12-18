from django.contrib import admin
from apps.listing.models import Photo
from apps.listing.models import Listing
from apps.listing.models import Amenity
# Register your models here.
admin.site.register(Photo)
admin.site.register(Listing)
admin.site.register(Amenity)