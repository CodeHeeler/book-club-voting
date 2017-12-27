"""book_club_voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from votes import views as vote_views
from books import views as book_views

urlpatterns = [
    url(r'^$', vote_views.open_elections_list, name='open_election_list'),
    url(r'^election$', vote_views.new_election, name='new_election'),
    url(r'^election/(?P<election_id>[0-9]+)$', vote_views.election_detail_view, name='election_detail'),
    url(r'^election/(?P<election_id>[0-9]+)/edit', vote_views.election_edit_view, name='election_edit'),
    url(r'^election/(?P<election_id>[0-9]+)/delete', vote_views.delete_election, name='delete_election'),
    url(r'^open_voting$', vote_views.open_election, name='open_election'),
    url(r'^close_voting$', vote_views.close_election, name='close_election'),
    url(r'^vote$', vote_views.create_ballot, name='create_ballot'),
    url(r'^books', book_views.book_list, name='book_list'),
    url(r'^book$', book_views.new_book, name='new_book'),
    url(r'^book/(?P<book_id>[0-9]+)/edit', book_views.book_edit_view, name='book_edit'),
    url(r'^book/(?P<book_id>[0-9]+)/delete', book_views.book_delete_view, name='book_delete'),
    url(r'^admin/', admin.site.urls),
]
