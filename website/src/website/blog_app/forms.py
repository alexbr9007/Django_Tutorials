from django import forms
from .models import BlogPost

# Forms are for rendering

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'slug', 'content', 'published_date']

    # custom method to verify if the title already exists
    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title has already been used.")
        return title