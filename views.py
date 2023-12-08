from mtgsdk.card import Card, Format, Set, Subtype, Supertype, Type

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


class CardList(APIView):
    """
    View to list all Card instances.
    """
    def get(self, request, format=None):
        return Card.all()


class CardDetail(generics.GenericAPIView):
    pass


class SetList(APIView):
    pass


class SetDetail(generics.GenericAPIView):
    pass


class TypeList(APIView):
    pass


class SubtypeList(APIView):
    pass


class SupertypeList(APIView):
    pass


class FormatList(APIView):
    pass
