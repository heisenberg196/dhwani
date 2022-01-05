from rest_framework import routers

from dhw.views import ChildSet, DistrictSet, StateSet

router = routers.SimpleRouter()
router.register(r'state', StateSet)
router.register(r'district', DistrictSet)
router.register(r'child', ChildSet)
urlpatterns = router.urls
