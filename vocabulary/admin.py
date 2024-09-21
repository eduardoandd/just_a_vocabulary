from django.contrib import admin
from vocabulary.models import Vocabulary,Type



class TypeAdmin(admin.ModelAdmin):
    list_display=('id','name',)
    search_fields=('name',)

class VocabularyAdmin(admin.ModelAdmin):
    list_display=('word','translation','type','total_hits','total_errors',)
    search_fields=('word',)


admin.site.register(Vocabulary,VocabularyAdmin)
admin.site.register(Type,TypeAdmin)


