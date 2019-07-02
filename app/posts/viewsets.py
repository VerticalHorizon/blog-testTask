from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from .models import Post, Reaction
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request: Request, pk=None):
        if not Reaction.objects.filter(post=self.get_object(), user=request.user).exists():
            Reaction(post=self.get_object(), user=request.user).save()
            return Response({'message': 'OK'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def unlike(self, request: Request, pk=None):
        if Reaction.objects.filter(post=self.get_object(), user=request.user).exists():
            Reaction.objects.filter(post=self.get_object(), user=request.user).delete()
            return Response({'message': 'OK'}, status=status.HTTP_200_OK)
        return Response({'message': 'There is nothing to remove.'}, status=status.HTTP_400_BAD_REQUEST)
