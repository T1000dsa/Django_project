from django.contrib import admin, messages
from .models import Worker, Category, TagModel, Helmet
from django.utils.safestring import mark_safe
class TagFilter(admin.SimpleListFilter):
    title = 'Tags'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('tag_0', 'tag0'),
            ('tag_1', 'tag1'),
        ]

    def queryset(self, request, queryset):
        return queryset



@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'photo','photo_tumb', 'content', 'description', 'tags','cat']
    readonly_fields = ['photo_tumb']
    filter_horizontal = ['tags']
    prepopulated_fields = {'slug':('title', )}
    list_display = ('title', 'time_create', 'photo_tumb','is_published','description', 'cat', 'brief',)
    list_display_links =  ('title',)
    ordering = ['id']
    list_editable = ('is_published','description')
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = [TagFilter, 'cat__name', 'is_published']

    save_on_top = True

    @admin.display(description='brief info', ordering='description')
    def brief(self, info:Worker):
        if info.description:
            return f'Length of the description {len(info.description)}'
        else:
            return f'There is no description'
    
    @admin.display(description='tumb')
    def photo_tumb(self, info:Worker):
        if info.photo:
            return mark_safe(f'<img src="{info.photo.url}" width="50" height="50">')
        else:
            adress = r"\media\photos\None_image\None.png"
            return mark_safe(f'<img src="{adress}" width="50" height="50">')

    
    @admin.action(description='Publish the worker')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Worker.Status.Published)
        self.message_user(request, f'was changed {count} of data')

    @admin.action(description='Hide the worker')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Worker.Status.Draft)
        self.message_user(request, f'was changed {count} of data', messages.WARNING)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links =  ('id', 'name')
    ordering = ['id']

@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')
    list_display_links =  ('id', 'tag')
    ordering = ['id']
#admin.site.register(Worker, WorkerAdmin)
# Register your models here.
