from mtgsdk.card import Card

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
