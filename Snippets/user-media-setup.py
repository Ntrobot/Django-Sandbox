## Snippet for serving static media files uploaded by users during development
## Directory: In the individual app folder
## Date: 01/11/2021
## Variables to be changed:


### settings.py ###
# Where to save user uploaded content
# media root is the directory where the uploaded content are uploaded
MEDIA_ROOT = BASE_DIR / 'media'
# how these uploaded content would be accessed via URL
MEDIA_URL = '/media/'


### urls.py ###

# Importing the required modules
from django.conf import settings
from django.conf.urls.static import static

# This method should only be used during development when the debug mode is enabled
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)