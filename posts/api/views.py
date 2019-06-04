from rest_framework import generics
from posts.models import Post, Categories
from posts.api.serializers import PostSerializer, \
    PostDetailSerializer, CategoriesSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class CategoriesListView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesView(generics.ListAPIView):
    serializer_class = PostDetailSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Post.objects.filter(category__title=category)
