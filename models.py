from mtgsdk import card

from django.db import models

class Card(card.Card, models.Model):
  pass
