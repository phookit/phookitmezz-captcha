from mezzanine.generic.forms import ThreadedCommentForm
from mezzanine.accounts.forms import ProfileForm
from captcha.fields import CaptchaField


class GuestCommentForm(ThreadedCommentForm):
    def __init__(self, request, *args, **kwargs):
        super(GuestCommentForm, self).__init__(request, *args, **kwargs)
        if not request.user.is_authenticated():
            self.fields['captcha'] = CaptchaField()


class SignUpCaptchaForm(ProfileForm):
    def __init__(self, request, *args, **kwargs):
        super(SignUpCaptchaForm, self).__init__(request, *args, **kwargs)
        self.fields['captcha'] = CaptchaField()
