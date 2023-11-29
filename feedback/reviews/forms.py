from django import forms

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your Name', max_length=10, error_messages={
#         'required' : 'Your Name must not be empty',
#         'max_length' : 'Please enter a shorter name'
#     })
#     review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5)

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__' #['user_name', 'review_text', 'rating']
        #exclude = ['owner_comment']

        labels = {
            'user_name' : 'Your Name',
            'review_text' : 'Your Feedback'
        }

        error_messages = {
            'user_name' : {
                'required' : 'Your Name must not be empty',
                'max_length' : 'Please enter a shorter name'
            }
        }
