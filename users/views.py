from rest_framework.views import APIView
from rest_framework.response import Response

users = [
    {'id': 1, 'name': 'ivan'},
    {'id': 2, 'name': 'max'},
    {'id': 3, 'name': 'olha'},
    {'id': 4, 'name': 'serhiy'},
    {'id': 5, 'name': 'oleg'},
]


class TestAPI(APIView):
    def get(self, *args, **kwargs):

        return Response(users)

    def put(self, *args, **kwargs):
        new_user = self.request.data
        return Response('method put')

    def patch(self, request):
        return Response('method patch')

    def post(self, request):
        return Response('method post')

    def delete(self, request):
        return Response('method delete')
