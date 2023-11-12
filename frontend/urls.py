from django.urls import path

from . import views

app_name = 'frontend'
urlpatterns = [
    # Send all / to index()
    path('', views.index, name='index'),
    # Send /character/int to character()
    path('character/<int:character_id>', views.character, name='character'),
    # Send /characters to characters()
    path('characters/', views.characters, name='characters'),
    # Send /quote/int to quote()
    path('quote/<int:quote_id>', views.quote, name='quote'),
    # Send /quotes to quotes()
    path('quotes/', views.quotes, name='quotes'),
]
