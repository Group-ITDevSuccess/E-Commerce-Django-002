# production_settings.py

from .settings import *

# Security settings
DEBUG = False
ALLOWED_HOSTS = ['itdevsuccess.pythonanywhere.com']  # Remplacez par votre domaine de production

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'itdevsuccess$ti_varotra_v1_0',
        'USER': 'itdevsuccess',
        'PASSWORD': 'AllahSeul',
        'HOST': 'itdevsuccess.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}

# Static files settings
STATIC_ROOT = os.path.join(BASE_DIR, "static")  # Remplacez par le chemin absolu vers le répertoire des fichiers statiques de production

# Autres configurations spécifiques à l'environnement de production
# ...

