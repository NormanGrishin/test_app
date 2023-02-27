from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from services.models import Subscriptions
from services.serializers import SubscriptionsSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer
