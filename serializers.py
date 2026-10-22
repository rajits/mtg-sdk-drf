from rest_framework import serializers


class CardSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField(max_length=200)
    mana_cost = serializers.CharField(max_length=200, allow_blank=True, allow_null=True, required=False)
    cmc = serializers.FloatField(required=False, allow_null=True)
    colors = serializers.ListField(child=serializers.CharField(), required=False, allow_null=True)
    color_identity = serializers.ListField(child=serializers.CharField(), required=False, allow_null=True)
    type = serializers.CharField(max_length=200, required=False, allow_null=True)
    supertypes = serializers.ListField(child=serializers.CharField(), required=False, allow_null=True)
    types = serializers.ListField(child=serializers.CharField(), required=False, allow_null=True)
    subtypes = serializers.ListField(child=serializers.CharField(), required=False, allow_null=True)
    rarity = serializers.CharField(required=False, allow_null=True)
    set = serializers.CharField(required=False, allow_null=True)
    set_name = serializers.CharField(required=False, allow_null=True)
    text = serializers.CharField(required=False, allow_null=True)
    flavor = serializers.CharField(required=False, allow_null=True)
    artist = serializers.CharField(required=False, allow_null=True)
    number = serializers.CharField(required=False, allow_null=True)
    power = serializers.CharField(required=False, allow_null=True)
    toughness = serializers.CharField(required=False, allow_null=True)
    image_url = serializers.URLField(required=False, allow_null=True)


class SetSerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()
    gatherer_code = serializers.CharField(required=False, allow_null=True)
    old_code = serializers.CharField(required=False, allow_null=True)
    magic_cards_info_code = serializers.CharField(required=False, allow_null=True)
    release_date = serializers.CharField(required=False, allow_null=True)
    border = serializers.CharField(required=False, allow_null=True)
    type = serializers.CharField(required=False, allow_null=True)
    block = serializers.CharField(required=False, allow_null=True)
    online_only = serializers.BooleanField(required=False)


class StringSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return str(instance)


class TypeSerializer(StringSerializer):
    pass


class SubtypeSerializer(StringSerializer):
    pass


class SupertypeSerializer(StringSerializer):
    pass


class FormatSerializer(StringSerializer):
    pass
