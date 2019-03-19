from django import forms
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from .models import Post, Comment

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['text'].widget.attrs.update({'class':'form-control'})
   
    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'image_thumbnail', )
        image_thumbnail = ProcessedImageField(
            spec_id='myapp:blog:image_thumbnail',
            processors=[Thumbnail(120, 120)],
            format='jPEG',
            options={'qulity' : 100},
            blank=True,
        )

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
        self.fields['author'].widget.attrs.update({'class':'form-control-sm'})
        self.fields['text'].widget.attrs.update({'class':'form-control-sm'})
   
    class Meta:
        model = Comment
        fields = ('author', 'text',)
