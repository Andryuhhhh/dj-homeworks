from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()

        main_count = 0

        for form in self.forms:
            if not hasattr(form, 'cleaned_data'):
                continue

            if form.cleaned_data.get('DELETE'):
                continue

            if form.cleaned_data.get('is_main'):
                main_count += 1

        if main_count != 1:
            raise ValidationError('У статьи должен быть ровно один основной раздел.')


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
