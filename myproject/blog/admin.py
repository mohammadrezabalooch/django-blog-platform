from django.contrib import admin
from .models import Article,Category, IPAddress
# admin page header

admin.site.site_header = 'My Django Weblog'

# Register your models here.

def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status="p")
    if rows_updated == 1:
        message_bit = "1 article was published"
    else:
        message_bit = "{} articles were published".format(rows_updated)
    modeladmin.message_user(request, message_bit)


make_published.short_description = "publish selected articles"


def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status="d")
    if rows_updated == 1:
        message_bit = "1 article was drafted"
    else:
        message_bit = "{} articles were drafted".format(rows_updated)
    modeladmin.message_user(request, message_bit)
make_draft.short_description = "draft selected articles"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("position", "title", 'parent', "slug", "status")
    list_filter = (["status"])
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug" : ("title",)}
admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "thumbnail_tag", "author", "slug", "publish", "is_special", "status", 'category_to_str')
    list_filter = ("publish", "status", "author")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug" : ("title",)}
    ordering = ("-status", "-publish")
    actions = [make_published, make_draft]

admin.site.register(Article, ArticleAdmin)
admin.site.register(IPAddress)