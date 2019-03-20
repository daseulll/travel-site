from django import forms
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post, Comment

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        text= self.fields['text'].widget = SummernoteWidget()
   
    class Meta:
        model = Post
        fields = ('title', 'text', 'image', )
        image_thumbnail = ProcessedImageField(
            spec_id='blog:post:image_thumbnail',
            processors=[ResizeToFill(100, 50)],
            format='JPEG',
            options={'quality' : 80},
            verbose_name="대표이미지",
        )

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
        self.fields['author'].widget.attrs.update({'class':'form-control-sm'})
        self.fields['text'].widget.attrs.update({'class':'form-control'})
   
    class Meta:
        model = Comment
        fields = ('author', 'text',)
