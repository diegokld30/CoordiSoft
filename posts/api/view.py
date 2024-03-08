from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.api.permissions import IsAdminOrReadOnly

class PostModelViewSet(ModelViewSet):
    #solo los usuarios que esten autenticados con token pueden hacer peticiones
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    #http_method_names = ['get', 'delete']

"""class PostViewSet(ViewSet):
    def list(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk: int):
        post = PostSerializer(Post.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=post.data)


    def create(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)"""


"""class PostApiView(APIView):
    def get(self, request):
        #posts = Post.objects.all()
        #posts = [posts.title for posts in Post.objects.all()]

        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        #Post.objects.create(title=request.data['title'], description=request.data['description'], order=request.data['order'])
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
        #return self.get(request)"""
