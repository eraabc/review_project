from django import  forms


class TaskForm(forms.Form):
    title = forms.CharField(max_length=100,
                            label='Название задачи',
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}),
                                  label='Описание',
                                  required=True,)
    extra_info = forms.CharField(label='Дополнительное описание',
                                 widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}),
                                 required=False)
    finish_date = forms.DateField(label='Дата выполнения',widget=forms.DateInput(attrs={'class':'form-control','type':'date'}),required=False)