from .models import Post, Comment
from modeltranslation.translator import TranslationOptions,register

@register(Post)
class ProductTranslationOptions(TranslationOptions):
    fields = ('hashtag', 'description')


@register(Comment)
class ProductTranslationOptions(TranslationOptions):
    fields = ('parent', 'text')