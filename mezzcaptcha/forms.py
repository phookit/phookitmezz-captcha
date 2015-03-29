from mezzanine.generic.forms import ThreadedCommentForm                                                      
from captcha.fields import CaptchaField

class GuestCommentForm(ThreadedCommentForm):                                                           
    def __init__(self, request, *args, **kwargs):                                                            
        super(GuestCommentForm, self).__init__(request, *args, **kwargs)                               
        if not request.user.is_authenticated():                                                              
            self.fields['captcha'] = CaptchaField()
