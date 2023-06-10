from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import robots_txt
from blog.feeds import LatestPostsFeed
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSiteMap,CategorySiteMap

sitemaps={'post':PostSiteMap,'category':CategorySiteMap}

urlpatterns = [
    #/////////////BLOG///////////////////////////////////#
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('sitemap.xml/',sitemap,{'sitemaps':sitemaps}),
    path('feed/atom/',LatestPostsFeed(),name="post_feed"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('robots.txt/', robots_txt, name='robots_txt'),
    #////////////////////////////////////////////////////#
]


#--------SETTINGS AND CONFIGURATION-------------------
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
