"""MTG API resources exposed by the mtgsdk package."""

from mtgsdk import Card, Set, Subtype, Supertype, Type
from mtgsdk.config import __endpoint__
from mtgsdk.restclient import RestClient


class Format:
    """Adapter for the formats endpoint, which is not exposed by mtgsdk."""

    @staticmethod
    def all() -> list[str]:
        return RestClient.get(f"{__endpoint__}/formats")["formats"]
