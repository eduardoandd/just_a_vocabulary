from django.shortcuts import render,redirect
from random_word.models import Vocabulary
from random_word.forms import NewWordModelForm



def random_view(request):
    
    message=''
    random_word= Vocabulary.objects.order_by('?').values_list('word','translation').first()
    
    if request.method == "POST":
        translation= request.POST['translation']
        
        if translation == random_word[1]:
            message='success'
        else:
            message='fail'
    
    return render(
        request,
        'random.html',
        {'random_word': random_word[0], 'message': message} 
    )
    
def new_word_view(request):
    
    if request.method == 'POST':
        
        new_word_form= NewWordModelForm(request.POST)
        
        if new_word_form.is_valid():
            new_word_form.save()
            return redirect('random_form')
    else:
        new_word_form=NewWordModelForm()
        
    return render(request, 'new_word.html', {'new_word_form': new_word_form})
            
