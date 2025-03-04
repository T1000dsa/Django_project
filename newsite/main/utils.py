menu = [{'title':'about site', 'url_name':'about_name'}, 
        {'title':'addpage', 'url_name':'add_name'}, 
        {'title':'contacts', 'url_name':'contacts_name'}, 
        {'title':'home', 'url_name':'home_name'},
        ]

class DataMixin:
    index_list = None
    title_page = None
    cat_selected = None
    paginate_by = 10
    post = None
    extra_context  = {}
    
    def __init__(self):
        if self.title_page:
            self.extra_context['title'] =self.title_page
        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected
        if self.post is not None:
            self.extra_context['post'] = self.post
        if self.index_list is not None:
            self.extra_context['index_list'] = self.index_list
        if self.paginate_by != 5:
            self.extra_context['paginate_by'] = self.paginate_by


    def get_mixin_context(self, context:dict, **kwargs):
        context['menu'] = menu
        context['cat_selected'] = None
        context.update(kwargs)
        return context