from django import forms
from radio.models import Show, StationStatusUpdate
from numbersfm.utils.icecast import archive_stream_is_running, start_archives, stop_archives


class StationStatusUpdateForm(forms.ModelForm):
    is_live = forms.ChoiceField(choices=(
            (True, 'Live'),
            (False, 'Archive')
            ))
    
    class Meta:
        model = StationStatusUpdate
        exclude = ('timestamp',)

    def clean(self):
        # clear out extra data if it's an archive stream
        if not self.cleaned_data.get('is_live') or self.cleaned_data.get('is_live') == 'False':
            self.cleaned_data['current_show'] = None
            self.cleaned_data['current_song'] = ''

        if self.cleaned_data.get('is_live') != 'False' and not self.cleaned_data['current_show']:
            raise forms.ValidationError("Select the current live show.")
        
        return self.cleaned_data

    def save(self, *args, **kwargs):
        status = super(StationStatusUpdateForm, self).save(*args, **kwargs)
        
        if status.is_live and archive_stream_is_running():
            stop_archives()
        elif not status.is_live and not archive_stream_is_running():
            start_archives()
