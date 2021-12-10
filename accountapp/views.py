from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


# UI 설정 부분
from accountapp.models import NewModel
from accountapp.serializers import NewModelSerializer, UserSerializer


def hello_world_template(request):
    return render(request, 'accountapp/hello_world_template.html')

# 로직 처리부분
@api_view(['GET', 'POST'])
def hello_world(request):

    if request.method == 'POST':
        input_data = request.data.get('input_data')

        new_model = NewModel()
        new_model.text = input_data
        new_model.save()

        # Serialize 하는 부분
        serializer = NewModelSerializer(new_model)

        return Response(serializer.data)

    new_model_list = NewModel.objects.all()
    serializer = NewModelSerializer(new_model_list, many=True)

    return Response(serializer.data)


def AccountCreateTemplate(request):
    return render(request, 'accountapp/create.html')


class AccountCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []