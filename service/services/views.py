from django.db.models import Prefetch
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from services.models import Subscriptions
from services.serializers import SubscriptionsSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscriptions.objects.all().prefetch_related(
        'plan',
        Prefetch('client', queryset=Client.objects.all().select_related('user').only('company_name', 'user__email')))
    serializer_class = SubscriptionsSerializer
