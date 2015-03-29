from setuptools import setup, find_packages

setup(name="mezzcaptcha",
      version="0.1.0",
      description="Custom mezzanine forms with captchas",
      long_description="""\
Includes a comment form that will display a captcha to guest users
but will not display a captcha to logged in uers.
""",
      author="Paul Hunt",
      author_email="paul@phookit.com",
      url="https://github.com/phookit/phookitmezz-captcha",
      license="BSD",
      packages=find_packages(),
      include_package_data=True,
      install_requires=['django-simple-captcha>=0.4.4',],
)

