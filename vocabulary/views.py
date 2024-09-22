from django.shortcuts import render

def vocabulary_view(request):
    return render(
        request,
        'vocabulary.html',
        {'vocabulary':{'word':'Take'}}
    )
