from django.contrib import admin
from django.db import models
from .models import Article, Tag, MyIdea
from django.urls import reverse
from django.utils.html import format_html
from markdownx.widgets import AdminMarkdownxWidget


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    @staticmethod
    def go_tag_page(obj):
        url = reverse('admin:cloudsen_blog_tag_change', args=(obj.tag.pk,))
        return format_html('<a href="{}">{}</a>', url, obj.tag.name)

    @staticmethod
    def go_user_page(obj):
        url = reverse('admin:auth_user_change', args=(obj.author.pk,))
        return format_html('<a href="{}">{}</a>', url, obj.author.username)

    go_tag_page.admin_order_field = 'tag'
    go_tag_page.short_description = 'tag'
    go_user_page.admin_order_field = 'author'
    go_user_page.short_description = 'author'
    list_display = [
        'title',
        'id',
        'go_user_page',
        'go_tag_page',
        'create_time',
        'update_time',
        'is_deleted'
    ]
    list_display_links = [
        'title'
    ]
    ordering = ('id',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'id',
        'create_time',
        'update_time',
        'is_deleted'
    ]
    list_display_links = [
        'id',
        'name'
    ]
    ordering = ('id',)


@admin.register(MyIdea)
class MyIdeaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'author',
        'content',
        'create_time',
        'update_time',
        'is_deleted',
    ]
    list_display_links = [
        'id',
        'content',
    ]
    formfield_overrides = {
        models.TextField: {
            'widget': AdminMarkdownxWidget,
        }
    }
