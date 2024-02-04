from django import template
from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path if 'request' in context else ''
    menu_items = MenuItem.objects.filter(parent__isnull=True, title=menu_name).first()

    if menu_items:
        current_item = MenuItem.objects.filter(url=current_url).first()

        if current_item:
            ancestors = [current_item]
            get_ancestors(current_item, ancestors)
        else:
            ancestors = []

        return {'menu_items': menu_items, 'current_url': current_url, 'ancestors': ancestors}

    return {}


def get_ancestors(menu_item, ancestors):
    if menu_item.parent:
        ancestors.insert(0, menu_item.parent)
        get_ancestors(menu_item.parent, ancestors)
