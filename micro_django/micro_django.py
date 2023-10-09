from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line
from django.http import JsonResponse
from django.urls import path

settings.configure(
    ROOT_URLCONF=__name__,
    DEBUG=True,
    SECRET_KEY='secret-key-here',
)


def dados_placas(request):
    list_to_json=[{'id':100,'placa':'BHX1293', 'portaria':'1', 'tipo':'E','data':'30-09-2023','hora':'15:25:20' },
                  {'id':101,'placa':'BHX1233', 'portaria':'1', 'tipo':'E','data':'30-09-2023','hora':'15:25:21' },
                  {'id':102,'placa':'BXA1293', 'portaria':'1', 'tipo':'E','data':'30-09-2023','hora':'15:25:22' }
                  ]
    list_to_json2=[{'id':200,'placa':'GIN5839', 'portaria':'1', 'tipo':'S','data':'20-09-2023','hora':'00:50:20' },
                  {'id':201,'placa':'ABC1234', 'portaria':'1', 'tipo':'E','data':'20-09-2023','hora':'00:45:00' },
                  {'id':202,'placa':'ABC1234', 'portaria':'1', 'tipo':'S','data':'20-09-2023','hora':'00:45:45' }
                  ]
    return JsonResponse(list_to_json2, safe=False)


urlpatterns = [path("", dados_placas)]

application = WSGIHandler()

if __name__ == "__main__":
    execute_from_command_line()
