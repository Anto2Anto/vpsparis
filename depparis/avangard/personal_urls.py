from django.urls import path
from .views import *

urlpatterns = [
        # path('', PersonalViewSet.as_view({'get': 'list'}), name = 'personal'),
        path('', PersonalAPI.as_view(), name = 'personal'),
        path('current/', PersonalCurrentAPI.as_view(), name = 'current'),
        path('history/', PersonalHistoryAPI.as_view(), name = 'history'),
        path('favourite/', PersonalFavouriteAPI.as_view(), name = 'favourite'),
        path('parametres/', PersonalParametresAPI.as_view(), name = 'parametres'),
]
