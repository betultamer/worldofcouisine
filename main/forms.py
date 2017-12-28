from django import forms

from .models import Comment


RATING_CHOICES = (
    ('1', 'Very Poor - 1'),
    ('2', 'Poor 2'),
    ('3', 'Average 3'),
    ('4','Good 4'),
    ('5', 'Very good 5'),
)



class CommentForm(forms.ModelForm):
     def clean_body(self):
            comment = self.cleaned_data['body']
            return comment

     class Meta:
         model = Comment
         fields = '__all__'
         widgets = {
             'rating': forms.RadioSelect(choices=RATING_CHOICES),
         }
