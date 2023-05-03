from blog.django_settings import * # noqa

try:
    from blog.local_settings import *
except:
    import traceback;traceback.print_exc()
