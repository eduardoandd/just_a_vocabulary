from django.contrib import admin
from random_word.models import Vocabulary

class VocabularyAdmin(admin.ModelAdmin):
    list_display= ('id','word','translation','total_hits','total_errors',)
    search_fields=('word',)
    
admin.site.register(Vocabulary,VocabularyAdmin)
