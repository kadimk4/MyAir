# from django.shortcuts import render
# from rest_framework.response import Response
# from users.models import UserPaginator
# from rest_framework.generics import GenericAPIView, ListAPIView
# from rest_framework import status
# from users.repositories.repository import UserRepository
# from users.api.serializers import UserCrudSerializer, UserSerializer

# class SelfListView(ListAPIView):
#     queryset = UserRepository.get_all()

#     serializer_class = UserSerializer
#     pagination_class = UserPaginator


# class SelfCreateView(GenericAPIView):
#     serializer_class = UserCrudSerializer

#     def post(request):
#         serializer = UserRepository.post(request)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class SelfUpdareDeleteView(GenericAPIView):
#     serializer_class = UserCrudSerializer

#     def patch(request):
#         serializer = UserRepository.update(request)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def delete(request):
#         serializer = UserRepository.delete(request)
#         return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
