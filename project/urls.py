from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

# Admin settings
admin.site.site_header = "blog"
admin.site.site_title = "blog site admin"
admin.site.index_title = "blog site administration"


urlpatterns = [
    path("admin/", admin.site.urls),    
    path("api/", include("user.urls")),
    path("api/", include("post.urls")),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)