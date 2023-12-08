from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)      # e.g. "Narset, Enlightened Master"
    mana_cost = serializers.CharField(max_length=200) # e.g. "{3}{U}{R}{W}"
    cmc = serializers.IntegerField()
    # colors
    type = serializers.CharField(max_length=200)      # e.g. "Legendary Creature — Human Monk"


class SetSerializer:
    pass


class TypeSerializer:
    pass


class SubtypeSerializer:
    pass


class SupertypeSerializer:
    pass


class FormatSerializer:
    pass
