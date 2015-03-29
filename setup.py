from setuptools import setup, find_packages

setup(name="MyPackage",
      version="0.1",
      description="Custom mezzanine forms with captchas",
      long_description="""\
Includes a comment form that will display a captcha to guest users
but will not display a captcha to logged in uers.
""",
      author="Paul Hunt",
      author_email="paul@phookit.com",
      url="https://github.com/phookit/phookitmezz-captcha",
      license="BSD",
      install_requires=['django-simple-captcha>=0.4.4',],
)

