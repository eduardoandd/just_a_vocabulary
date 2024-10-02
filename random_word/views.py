from django.shortcuts import render,redirect
from random_word.models import Vocabulary
from random_word.forms import WordModelForm
from django.views.generic import CreateView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



def random_view(request):
    
    message=''
    lista=[]
    
    if 'random_word' in request.session: 
        if request.method == "POST":
            
            translation= request.POST['translation']
            correct_translation= request.session['correct_translation']
            random_word= request.session['random_word']
            
            if translation.lower() == correct_translation.lower():
                message='success'
                random_word= random_word_generate()

                while random_word[1].lower() == translation.lower():
                    random_word= random_word_generate()
                    
                get_session(random_word,request)
                lista.append(request.session['random_word'])
                lista.append(request.session['id'])
                lista.append(request.session['correct_translation'])
                
                
            else:
                message='fail'
                lista.append(request.session['random_word'])
                lista.append(request.session['id'])
                lista.append(request.session['correct_translation'])
                
                    
        else:
            random_word= random_word_generate()
            get_session(random_word,request)
            lista.append(request.session['random_word'])
            lista.append(request.session['id'])
            lista.append(request.session['correct_translation'])
            
                     
    else:    
        random_word= random_word_generate()
        get_session(random_word,request)
        lista.append(request.session['random_word'])
        lista.append(request.session['id'])
        lista.append(request.session['correct_translation'])
        
        
    random_word=lista[0]
    id=lista[1]
    translation=lista[2]    
    lista=[]
            
    return render(
        request,
        'random.html',
        {'random_word': random_word, 'message': message, 'id':id,'translation':translation} 
    )
    
def get_session(random_word,request):
     
    request.session['random_word'] = random_word[0]
    request.session['correct_translation'] = random_word[1]
    request.session['id']=random_word[2]
    
def random_word_generate():
    random_word_data= Vocabulary.objects.order_by('?').values_list('word','translation','id').first()
    
    return random_word_data

@method_decorator(login_required(login_url='login'), name='dispatch')                 
class WordCreateView(CreateView):
    model=Vocabulary
    form_class= WordModelForm
    template_name='new_word.html'
    success_url='/random/'

@method_decorator(login_required(login_url='login'), name='dispatch')         
class WordUpdateView(UpdateView):
    model=Vocabulary
    form_class= WordModelForm
    template_name='vocabulary_update.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('word_detail', kwargs= {'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')         
class WordDetailView(DetailView):
    model=Vocabulary
    template_name='word_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')         
class WordDeleteView(DeleteView):
    model=Vocabulary
    template_name='word_delete.html'
    success_url='/random'
        