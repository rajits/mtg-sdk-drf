from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from models import Card, Format, Set, Subtype, Supertype, Type
from serializers import (
    CardSerializer,
    FormatSerializer,
    SetSerializer,
    SubtypeSerializer,
    SupertypeSerializer,
    TypeSerializer,
)


class CardList(APIView):
    """
    View to list all Card instances.
    """

    def get(self, request, format=None):
        query = request.query_params.dict()
        cards = Card.where(**query).all() if query else Card.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)


class CardDetail(APIView):
    def get(self, request, pk, format=None):
        card = Card.find(pk)
        if card is None:
            raise NotFound("Card not found.")
        return Response(CardSerializer(card).data)


class SetList(APIView):
    def get(self, request, format=None):
        query = request.query_params.dict()
        sets = Set.where(**query).all() if query else Set.all()
        return Response(SetSerializer(sets, many=True).data)


class SetDetail(APIView):
    def get(self, request, code, format=None):
        card_set = Set.find(code)
        if card_set is None:
            raise NotFound("Set not found.")
        return Response(SetSerializer(card_set).data)


class TypeList(APIView):
    def get(self, request, format=None):
        return Response(TypeSerializer(Type.all(), many=True).data)


class SubtypeList(APIView):
    def get(self, request, format=None):
        return Response(SubtypeSerializer(Subtype.all(), many=True).data)


class SupertypeList(APIView):
    def get(self, request, format=None):
        return Response(SupertypeSerializer(Supertype.all(), many=True).data)


class FormatList(APIView):
    def get(self, request, format=None):
        return Response(FormatSerializer(Format.all(), many=True).data)
