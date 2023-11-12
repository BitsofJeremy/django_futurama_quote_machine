from random import randrange
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import CharacterSerializer, QuoteSerializer
from .models import Character, Quote

# Create your views here.


# /index shows a random quote
def index(request):
    num_quotes = Quote.objects.count()
    quote_to_get = randrange(1, num_quotes)
    rand_quote = Quote.objects.filter(id=quote_to_get)
    context = {'quote': rand_quote}
    return render(request, 'frontend/index.html', context)


# /character quote show all quotes by character
def character(request, character_id):
    # TODO for no character found, better 404
    char = get_object_or_404(Character, pk=character_id)
    char_quotes = Quote.objects.filter(character__name=char)
    context = {
        'character': char,
        'quotes': char_quotes
    }
    return render(request, 'frontend/character.html', context)


# /characters show all characters
def characters(request):
    chars = Character.objects.all()
    context = {
        'characters': chars
    }
    return render(request, 'frontend/characters.html', context)


# /quotes shows all quotes in DB
def quotes(request):
    all_quotes = Quote.objects.all()
    context = {
        'quotes': all_quotes
    }
    return render(request, 'frontend/quotes.html', context)


# /quote shows specific quote
def quote(request, quote_id):
    # TODO for no quote found, better 404
    _quote = get_object_or_404(Quote, pk=quote_id)
    context = {
        'quote': _quote
    }
    return render(request, 'frontend/quote.html', context)


class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Characters to be viewed or edited.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Quotes to be viewed or edited.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.IsAuthenticated]
