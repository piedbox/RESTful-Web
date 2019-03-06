from rest_framework import status
from toys.models import Toy
from toys.serializers import ToySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# decorator api_view generates the appropriate response for the unsupported HTTP verbs or methods This decorator is a wrapper that converts a function-based view into a subclass of the  rest_framework.views.APIView class
# Теперь сможем заюзать http OPTIONS 0.0.0.0:8000/toys/2/
# для определения параметров или требований, связанных с ресурсом
# http 0.0.0.0:8000/toys/ Accept:text/html - даст ответ в html разметке


@api_view(['GET', 'POST'])
def toy_list(request):
    """Для получения списка элементов. Или добавления одного элемента."""
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True)
        return Response(toys_serializer.data)

    elif request.method == 'POST':
        toy_serializer = ToySerializer(data=request.data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(toy_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def toy_detail(request, pk):
    """Для получения/изменения/удаления одного элемента."""
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        toy_serializer = ToySerializer(toy)
        return Response(toy_serializer.data)

    elif request.method == 'PUT':
        toy_serializer = ToySerializer(toy, data=request.data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data)
        return Response(toy_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
