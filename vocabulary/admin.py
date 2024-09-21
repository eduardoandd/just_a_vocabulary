from django.contrib import admin
from vocabulary.models import Vocabulary

class VocabularyAdmin(admin.ModelAdmin):
    list_display=('word','translation','total_hits','total_errors')
    search_fields=('word',)

admin.site.register(Vocabulary,VocabularyAdmin)
