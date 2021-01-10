from django.conf.urls import url
from . import views



urlpatterns = [
    #url(r'^$', views.index, name='index'),

    url(r'^$', views.login_user, name='login'),

    url(r'^login/$', views.login_user, name='login_user'),

    url(r'^logout/$', views.logout_user, name='logout_user'),



    #url(r'^login/$', views.UserFormView.as_view,name='login'),

    url(r'^image_list', views.image_list,name="image_list"),

    url(r'^flavor_list', views.flavor_list, name='flavor_list'),

    url(r'^instance_list$', views.instance_list, name='instance_list'),

    url(r'^get_create_instance_form', views.get_create_instance_form, name='get_create_instance_form'),
    url(r'^create_instance', views.create_instance, name='create_instance'),

    url(r'^get_delete_instance_form', views.get_delete_instance_form, name='get_delete_instance_form'),
    url(r'^delete_instance', views.delete_instance, name='delete_instance'),

##################################################################################################################

    # url(r'^api/get_instances$', api.get_instances),
    # url(r'^api/create_instance', api.create_instance),


#################################################################################################################


]