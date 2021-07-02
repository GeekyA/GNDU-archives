from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'paperapp'
urlpatterns = [
	path('upload/',views.upload_paper,name='upload'),
	path('',views.show_papers,name='index'),
	path('search',views.search,name='search')
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)