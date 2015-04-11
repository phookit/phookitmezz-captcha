# phookitmezz-captcha
Captcha for Mezzanine sign up and comment forms. Relies on django-simple-captcha for captcha handling. django-simple-captcha will be installed if you have installed mezzcaptcha from PyPi.

Currently the signup form will work however the comments form will only be compatible with the next release of Mezzanine.

## django-simple-captcha installation with Mezzanine

See https://django-simple-captcha.readthedocs.org/en/latest/usage.html#installation for general installation instructions.
Once django-simple-captcha has been installed you must update you urls.py.

    # url("^$", "mezzanine.blog.views.blog_post_list", name="home"),
    
    url(r'^captcha/', include('captcha.urls')),  # <-- add django-simple-captcha urls here
    
    # MEZZANINE'S URLS
    # ----------------
    # ADD YOUR OWN URLPATTERNS *ABOVE* THE LINE BELOW.
    # ``mezzanine.urls`` INCLUDES A *CATCH ALL* PATTERN
    # FOR PAGES, SO URLPATTERNS ADDED BELOW ``mezzanine.urls``
    # WILL NEVER BE MATCHED!

Add django-simple-captcha to your installed apps.

    "mezzanine.twitter",
    "mezzanine.accounts",
    "captcha",    # <-- add django-simple-captcha 
    # "mezzanine.mobile",

Make sure you have sync'd or migrated your database after installing django-simple-capctha and you should be good to go.

## SignUp form usage
Specify which sign-up form to use in your settings file.

    ACCOUNTS_PROFILE_FORM_CLASS = 'mezzcaptcha.forms.SignUpCaptchaForm'

The sign-up form should now include a captcha.

## Comment form usage
Specify which comment form to use in your settings file.

    COMMENT_FORM_CLASS = "mezzcaptcha.forms.GuestCommentForm"

Now guest users will have to fill in the captcha, registered users will not.
