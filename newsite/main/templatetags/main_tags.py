from django import template
import main.views as views
from main.models import Worker, Category, TagModel

register = template.Library()

@register.inclusion_tag('main/includes/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats':cats, 'cat_selected':cat_selected}

@register.inclusion_tag('main/includes/list_tags.html')
def show_all_tags(cat_selected=0):
    tags = TagModel.objects.all()
    return {'tags':tags, 'cat_selected':cat_selected}