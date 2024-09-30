from django.shortcuts import render,redirect
from random_word.models import Vocabulary
from random_word.forms import NewWordModelForm



def random_view(request):
    
    message=''
    lista=[]
    
    if 'random_word' in request.session: 
        if request.method == "POST":
            print(request.session.items())
            
            translation= request.POST['translation']
            correct_translation= request.session['correct_translation']
            random_word= request.session['random_word']
            
            if translation == correct_translation:
                message='success'
                random_word_data= Vocabulary.objects.order_by('?').values_list('word','translation').first()
                request.session['random_word'] = random_word_data[0]
                request.session['correct_translation'] = random_word_data[1]
                lista.append(request.session['random_word'])
                
            else:
                message='fail'
                lista.append(request.session['random_word'])
                
                  
        else:
            random_word_data= Vocabulary.objects.order_by('?').values_list('word','translation').first()
            request.session['random_word'] = random_word_data[0]
            request.session['correct_translation'] = random_word_data[1]
            lista.append(request.session['random_word'])
            
    else:    
        random_word_data= Vocabulary.objects.order_by('?').values_list('word','translation').first()
        request.session['random_word'] = random_word_data[0]
        request.session['correct_translation'] = random_word_data[1]
        lista.append(request.session['random_word'])
        
    
    random_word=lista[0]
    lista=[]
            
    return render(
        request,
        'random.html',
        {'random_word': random_word, 'message': message} 
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
            
