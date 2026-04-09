from rest_framework import serializers
from .models import LocationData, BridgeDesign


class LocationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationData
        fields = '__all__'


class BridgeDesignSerializer(serializers.ModelSerializer):
    location_data = LocationDataSerializer(source='location', read_only=True)
    location_name = serializers.SerializerMethodField()
    
    class Meta:
        model = BridgeDesign
        fields = '__all__'
    
    def get_location_name(self, obj):
        if obj.location:
            return f"{obj.location.district}, {obj.location.state}"
        return None
    
    def validate_span(self, value):
        """Validate span is between 20m and 45m"""
        if value < 20 or value > 45:
            raise serializers.ValidationError(
                "Outside the software range. Span must be between 20m and 45m."
            )
        return value
    
    def validate_carriageway_width(self, value):
        """Validate carriageway width"""
        if value < 4.25 or value >= 24:
            raise serializers.ValidationError(
                "Carriageway requirements from IRC must be greater than 4.25m and less than 24m."
            )
        return value
    
    def validate_skew_angle(self, value):
        """Validate skew angle"""
        if abs(value) > 15:
            raise serializers.ValidationError(
                "IRC 24 (2010) requires detailed analysis when skew angle exceeds ±15°."
            )
        return value
    
    def validate(self, data):
        """Validate geometry equation if all fields present"""
        if all(k in data for k in ['carriageway_width', 'girder_spacing', 'deck_overhang', 'num_girders']):
            carriageway = data['carriageway_width']
            spacing = data.get('girder_spacing')
            overhang = data.get('deck_overhang')
            num_girders = data.get('num_girders')
            
            if spacing and overhang and num_girders:
                overall_width = carriageway + 5
                
                # Check spacing and overhang < overall width
                if spacing >= overall_width:
                    raise serializers.ValidationError({
                        'girder_spacing': 'Girder spacing must be less than overall bridge width.'
                    })
                
                if overhang >= overall_width:
                    raise serializers.ValidationError({
                        'deck_overhang': 'Deck overhang must be less than overall bridge width.'
                    })
                
                # Check equation: (Overall Width - Overhang) / Spacing = No. of Girders
                calculated_girders = (overall_width - overhang) / spacing
                if abs(calculated_girders - num_girders) > 0.01:
                    raise serializers.ValidationError({
                        'geometry': 'Equation not satisfied: (Overall Width - Overhang) / Spacing ≠ No. of Girders'
                    })
        
        return data


class BridgeDesignListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing designs"""
    location_name = serializers.SerializerMethodField()
    
    class Meta:
        model = BridgeDesign
        fields = ['id', 'name', 'description', 'location_name', 'span', 
                  'carriageway_width', 'created_at', 'updated_at', 'is_favorite',
                  'estimated_cost', 'total_weight']
    
    def get_location_name(self, obj):
        if obj.location:
            return f"{obj.location.district}, {obj.location.state}"
        return None
