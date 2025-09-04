from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all().order_by('-date')
    serializer_class = ReservationSerializer

    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        reservation = self.get_object()
        new_status = request.data.get('status')
        valid_status = [s[0] for s in Reservation.STATUS_CHOICES]
        if new_status not in valid_status:
            return Response({'error': 'Estado inválido.'}, status=status.HTTP_400_BAD_REQUEST)
        reservation.status = new_status
        reservation.save()
        return Response(self.get_serializer(reservation).data)
