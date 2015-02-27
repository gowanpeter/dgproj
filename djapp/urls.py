
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from djapp import views

urlpatterns = patterns('',

    url(r'^home$', 'djapp.views.home', name='home'),
    url(r'^glaze$', 'djapp.views.GlazeView', name='glaze'),
    url(r'^documentation$', 'djapp.views.DocumentationView', name='documentation',),
    url(r'^condition$', 'djapp.views.ConditionView', name='condition',),
    url(r'^exhibition$', 'djapp.views.ExhibitionView', name='exhibition',),
    url(r'^hline$', 'djapp.views.HeathLineLookupView', name='hline',),
    url(r'^logo$', 'djapp.views.LogoView', name='logo',),
    url(r'^maker$', 'djapp.views.MakerLookupView', name='maker',),
    url(r'^material$', 'djapp.views.MaterialLookupView', name='material',),
    url(r'^method$', 'djapp.views.MethodLookupView', name='method',),
    url(r'^pub$', 'djapp.views.PublicationView', name='pub',),
    url(r'^setc$', 'djapp.views.SetCollectionView', name='set',),
)




    #src/kk
 #   url(r'^djapp/', include('djapp.urls', namespace='djapp', app_name='kk')),
 #   url(r'^$',djapp.views.kk_directory, name='kk')


#if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL,
                          #document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL,
                          #document_root=settings.MEDIA_ROOT)
