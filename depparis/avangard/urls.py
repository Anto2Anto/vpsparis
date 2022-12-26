from django.urls import path
from .views import *

urlpatterns = [
        #path('', FeedbackAPI.as_view(), name = 'home'),
        path('', ContactFormView.as_view(), name='contact'),
        #path('cle_en_main/', show_cle_en_main, name = 'cle_en_main'),
        # path('service/<slug:service_slug>/', ServiceHome.as_view(), name = 'service')
        #path('service', ServiceCatHome.as_view(), name = 'service'),
        #path('register/', RegisterViewSet.as_view(), name = 'register'),
        path('login/', LoginUser.as_view(), name = 'login'),
        path('logout/', logout_user, name = 'logout'),
]
