from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import LocationData, BridgeDesign
from .serializers import LocationDataSerializer, BridgeDesignSerializer


class LocationDataViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for location data"""
    queryset = LocationData.objects.all()
    serializer_class = LocationDataSerializer
    
    @action(detail=False, methods=['get'])
    def states(self, request):
        """Get list of all states"""
        states = LocationData.objects.values_list('state', flat=True).distinct().order_by('state')
        return Response(list(states))
    
    @action(detail=False, methods=['get'])
    def districts(self, request):
        """Get districts for a specific state"""
        state = request.query_params.get('state')
        if not state:
            return Response({'error': 'State parameter required'}, status=400)
        
        districts = LocationData.objects.filter(state=state).values_list('district', flat=True)
        return Response(list(districts))
    
    @action(detail=False, methods=['get'])
    def by_location(self, request):
        """Get location data by state and district"""
        state = request.query_params.get('state')
        district = request.query_params.get('district')
        
        if not state or not district:
            return Response({'error': 'State and district parameters required'}, status=400)
        
        try:
            location = LocationData.objects.get(state=state, district=district)
            serializer = self.get_serializer(location)
            return Response(serializer.data)
        except LocationData.DoesNotExist:
            return Response({'error': 'Location not found'}, status=404)


class BridgeDesignViewSet(viewsets.ModelViewSet):
    """API endpoint for bridge designs"""
    queryset = BridgeDesign.objects.all()
    serializer_class = BridgeDesignSerializer
    
    def get_queryset(self):
        """Filter designs based on query parameters"""
        queryset = BridgeDesign.objects.all()
        
        # Filter by favorites
        favorites_only = self.request.query_params.get('favorites', None)
        if favorites_only and favorites_only.lower() == 'true':
            queryset = queryset.filter(is_favorite=True)
        
        # Search by name
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )
        
        return queryset
    
    @action(detail=False, methods=['post'])
    def validate_geometry(self, request):
        """Validate geometry parameters"""
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            return Response({'valid': True, 'message': 'Geometry is valid'})
        except Exception as e:
            return Response({'valid': False, 'errors': serializer.errors}, status=400)
    
    @action(detail=True, methods=['post'])
    def toggle_favorite(self, request, pk=None):
        """Toggle favorite status of a design"""
        design = self.get_object()
        design.is_favorite = not design.is_favorite
        design.save()
        serializer = self.get_serializer(design)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def duplicate(self, request, pk=None):
        """Duplicate an existing design"""
        original = self.get_object()
        
        # Create a copy
        original.pk = None
        original.id = None
        original.name = f"{original.name} (Copy)"
        original.is_favorite = False
        original.save()
        
        serializer = self.get_serializer(original)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Get design statistics"""
        total_designs = BridgeDesign.objects.count()
        favorites = BridgeDesign.objects.filter(is_favorite=True).count()
        
        # Most common locations
        from django.db.models import Count
        common_locations = BridgeDesign.objects.values(
            'location__state', 'location__district'
        ).annotate(
            count=Count('id')
        ).order_by('-count')[:5]
        
        return Response({
            'total_designs': total_designs,
            'favorites': favorites,
            'common_locations': list(common_locations)
        })
