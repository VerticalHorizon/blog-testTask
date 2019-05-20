from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Post
from .serializers import PostSerializer, ReactionSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def get_permissions(self):
    #     if self.action in ('list', 'retrieve'):
    #         permission_classes = [IsAuthenticated]
    #     else:
    #         permission_classes = [IsAdmin]
    #     return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        return self.__reaction(request)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        return self.__reaction(request)

    def __reaction(self, request):
        request.data['post'] = self.get_object().pk
        request.data['user'] = request.user.pk
        serializer = ReactionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)