#urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateContactView, DetailsContactView, CreateSnippetsView, DetailsSnippetsView

#Define urls to access the apis and its actions (POST, PUT, DELETE)
urlpatterns = {
    url(r'^contact/$', CreateContactView.as_view(), name="create"),
	url(r'^contact/(?P<pk>[0-9]+)/$', DetailsContactView.as_view(), name="details"),
    url(r'^snippets/$', CreateSnippetsView.as_view(), name="snippets-create"),
    url(r'^snippets/(?P<pk>[0-9]+)/$', DetailsSnippetsView.as_view(), name="snippets-details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)