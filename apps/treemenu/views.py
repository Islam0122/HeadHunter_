from django.shortcuts import render
from django.views import View
from .models import MenuItem

class Menu_View(View):
    template_name = 'menu/menu.html'

    def get_context_data(self, menu_name):
        current_url = self.request.path
        menu_items = MenuItem.objects.filter(parent__isnull=True, title=menu_name).first()

        if menu_items:
            current_item = MenuItem.objects.filter(url=current_url).first()

            if current_item:
                ancestors = [current_item]
                self.get_ancestors(current_item, ancestors)
            else:
                ancestors = []

            return {'menu_items': menu_items, 'current_url': current_url, 'ancestors': ancestors}

        return {}

    def get_ancestors(self, menu_item, ancestors):
        if menu_item.parent:
            ancestors.insert(0, menu_item.parent)
            self.get_ancestors(menu_item.parent, ancestors)

    def get(self, request, *args, **kwargs):
        main_menu_context = self.get_context_data('Main Menu')
        secondary_menu_context = self.get_context_data('Secondary Menu')

        context = {
            'main_menu': main_menu_context,
            'secondary_menu': secondary_menu_context,
        }

        return render(request, self.template_name, context)
