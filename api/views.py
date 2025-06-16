from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import pytz
# pip install pytz


@api_view(['GET'])
def listCountries(request):
    paises = [
        {
            'id': '1',
            'nombre': 'Colombia',
            'codigo': 'CO',
            'bandera': 'https://flagcdn.com/w320/co.png'
        },
        {
            'id': '2',
            'nombre': 'Mexico',
            'codigo': 'MX',
            'bandera': 'https://flagcdn.com/w320/mx.png'
        },
        {
            'id': '3',
            'nombre': 'Francia',
            'codigo': 'FR',
            'bandera': 'https://flagcdn.com/w320/fr.png'
        },
    ]
    return Response(paises)

@api_view(['GET'])
def listTasks(request):
    tasks = [
        {
            'id': '1',
            'title': 'Realizar documentación en swagger',
            'completed': True,            
        },      
        {
            'id': '2',
            'title': 'Tomar curso React',
            'completed': True,            
        },      
        {
            'id': '3',
            'title': 'Estudiar SpringBoot',
            'completed': True,            
        },      
    ]
    return Response(tasks)


ZONES = {
    "CO": ["America/Bogota", "America/Medellin"],
    "MX": ["America/Mexico_City", "America/Cancun"],
    "FR": ["Europe/Paris", "Europe/Monaco"]
}

@api_view(['GET'])
def zonesCountry(request):
    codeCountry = request.query_params.get('code')
    zones = ZONES.get(codeCountry.upper(), [])
    return Response(zones)

@api_view(['GET'])
def hourZoneCountry(request):
    zone = request.query_params.get('zone', 'UTC')
    # zone = request.query_params.get('zone')
    try:
        # Crea un objecto de zona horaria basado en la zona
        tz = pytz.timezone(zone)
        # Obtiene la fecha actual ajustada a esa zona
        now = datetime.now(tz)
        return Response({
            'date': now.strftime('%Y/%m/%d'),
            'time': now.strftime('%H:%M:%S'),
            'zone': zone
        })
    except pytz.UnknownTimeZoneError:
        return Response({
            'error': True,
            'message': f'Error no se encontro la zona horaria: {zone}'
        }, status=status.HTTP_400_BAD_REQUEST )
