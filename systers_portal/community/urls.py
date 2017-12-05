from django.conf.urls import url

from community.views import (CommunityLandingView, EditCommunityProfileView,
                             ViewCommunityProfileView, CommunityPageView,
                             AddCommunityPageView, EditCommunityPageView,
                             DeleteCommunityPageView, CommunityUsersView,
                             UserPermissionGroupsView, AddCommunityView)

urlpatterns = [

    url(r'add_community/$', AddCommunityView.as_view(),
        name='add_community'),
    url(r'^(?P<slug>[\w-]+)/$', CommunityLandingView.as_view(),
        name='view_community_landing'),
    url(r'^(?P<slug>[\w-]+)/profile/$', ViewCommunityProfileView.as_view(),
        name='view_community_profile'),
    url(r'^(?P<slug>[\w-]+)/profile/edit/$',
        EditCommunityProfileView.as_view(), name='edit_community_profile'),
    url(r'^(?P<slug>[\w-]+)/p/add/$', AddCommunityPageView.as_view(),
        name="add_community_page"),
    url(r'^(?P<slug>[\w-]+)/p/(?P<page_slug>\w+)/edit/$',
        EditCommunityPageView.as_view(), name="edit_community_page"),
    url(r'^(?P<slug>[\w-]+)/p/(?P<page_slug>\w+)/delete/$',
        DeleteCommunityPageView.as_view(), name="delete_community_page"),
    url(r'^(?P<slug>[\w-]+)/p/(?P<page_slug>\w+)/$',
        CommunityPageView.as_view(), name="view_community_page"),
    url(r'^(?P<slug>[\w-]+)/users/$', CommunityUsersView.as_view(),
        name="community_users"),
    url(r'^(?P<slug>[\w-]+)/user/(?P<username>[\w.@+-]+)/permissions/$',
        UserPermissionGroupsView.as_view(), name="user_permission_groups"),
]
