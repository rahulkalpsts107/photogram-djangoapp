from django import forms

#Form the captures the Image Upload data
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='Only png, jpeg and gif allowed'
    )
    caption = forms.CharField(max_length=30,label='Enter a Caption',required=False)