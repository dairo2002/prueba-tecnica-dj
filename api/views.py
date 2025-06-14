from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def listCountries(request):
    paises = [
        {
            'nombre': 'Colombia',
            'codigo': 'CO',
            'bandera': 'https://flagcdn.com/w320/co.png'
        },
        {
            'nombre': 'Mexico',
            'codigo': 'MX',
            'bandera': 'https://flagcdn.com/w320/mx.png'
        },
        {
            'nombre': 'Francia',
            'codigo': 'Fr',
            'bandera': 'https://flagcdn.com/w320/fr.png'
        },
    ]
    return Response(paises)
