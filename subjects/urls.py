from django.urls import path


from .views import SubjectList, SubjectCreate



urlpatterns = [
	path('', SubjectList.as_view(), name='subject_list'),
	path('create/', SubjectCreate.as_view(), name='subject_create'),
]