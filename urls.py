from django.urls import path
from . import views

urlpatterns=[ 
    # path('api/',Itemsview.as_view(),name='post'),
    path('get/',views.displayAll,name='display'),
    path('get/<int:pk>',views.displayOne,name='displayOne'),
    path('post/',views.add,name='add'),
    path('patch/<int:id>',views.update,name='updata'),
    path("delete/<int:id>",views.remove,name='remove'),
    path('login_user/',views.login_page,name='login_user'),
]