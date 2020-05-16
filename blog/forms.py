from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():

        model  = Post
        fields = ('author','title','text')
        
        title = forms.CharField(widget=forms.TextInput(attrs={'class':'textinputclass'}))
        text = forms.CharField(widget=forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}))
        
        # widgets = {
        #     'title' : forms.TextInput(attrs={'class':'textinputclass'}),
        #     'text'  : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        # }
        
         
        
class CommentForm(forms.ModelForm):

    class Meta():
        model  = Comment
        fields = ('author','text')
        
        author = forms.CharField(widget=forms.TextInput(attrs={'class':'textinputclass'}))
        text = forms.CharField(widget=forms.Textarea(attrs={'class':'editable medium-editor-textarea'}))
        
        # widgets = {
        #     'author' : forms.TextInput(attrs={'class':'textinputclass'}),
        #     'text'   : forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        # }
        
        
        
    
        
        

