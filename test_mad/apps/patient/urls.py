from rest_framework.routers import DefaultRouter
from .views import PatientViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients')

urlpatterns = router.urls
# urlpatterns = [
#     path('patients/', PatientListView.as_view(), name='patients'),
# ]
