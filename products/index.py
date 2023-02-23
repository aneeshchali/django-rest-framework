from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    #not crucial information to be used.
    fields = [
        'title',
        'content',
        'price',
        'user',
    ]

