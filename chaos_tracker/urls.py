from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, InteractionViewSet, top_chaos_employee

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'interactions', InteractionViewSet)


urlpatterns = [
    path('top-chaos-employee/', top_chaos_employee, name='top-chaos-employee'),
    path('', include(router.urls)),
]