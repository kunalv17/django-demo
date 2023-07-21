from .models import User, Product
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import UserSerializer, ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False, methods=['GET'], url_path='check_user')
    def check_user(self, request):
        username = request.query_params.get('username')
        if not username:
            return Response({'message': 'Please provide a username in the query parameters.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(name=username)
            serializer = UserSerializer(user,context={'request': request})
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'message': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    