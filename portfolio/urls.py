from django.urls import path
from . import views

urlpatterns= [

	path('' , views.home  , name='home' ),
	path('portfolio' , views.portfolio  , name='portfolio' ),
	path('hire-me' , views.hire_me  , name='hire_me' ),
	path('dict' , views.dictionary  , name='dict' ),
]