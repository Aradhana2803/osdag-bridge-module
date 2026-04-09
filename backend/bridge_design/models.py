from django.db import models

class LocationData(models.Model):
    """Store environmental data for different locations"""
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    wind_speed = models.FloatField(help_text="Basic wind speed in m/s")
    seismic_zone = models.CharField(max_length=10)
    zone_factor = models.FloatField()
    max_temp = models.FloatField(help_text="Maximum shade air temperature in °C")
    min_temp = models.FloatField(help_text="Minimum shade air temperature in °C")
    
    class Meta:
        unique_together = ['state', 'district']
        ordering = ['state', 'district']
    
    def __str__(self):
        return f"{self.district}, {self.state}"


class BridgeDesign(models.Model):
    """Store bridge design configurations"""
    STRUCTURE_TYPES = [
        ('Highway', 'Highway'),
        ('Other', 'Other'),
    ]
    
    FOOTPATH_OPTIONS = [
        ('none', 'None'),
        ('single', 'Single-sided'),
        ('both', 'Both'),
    ]
    
    # Design identification
    name = models.CharField(max_length=200, help_text="Design name/identifier")
    description = models.TextField(blank=True, null=True, help_text="Design description or notes")
    
    # Basic inputs
    structure_type = models.CharField(max_length=20, choices=STRUCTURE_TYPES, default='Highway')
    location = models.ForeignKey(LocationData, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Geometric details
    span = models.FloatField(help_text="Span in meters")
    carriageway_width = models.FloatField(help_text="Carriageway width in meters")
    footpath = models.CharField(max_length=10, choices=FOOTPATH_OPTIONS, default='none')
    skew_angle = models.FloatField(default=0, help_text="Skew angle in degrees")
    
    # Material grades
    girder_grade = models.CharField(max_length=10, default='E250')
    cross_bracing_grade = models.CharField(max_length=10, default='E250')
    deck_grade = models.CharField(max_length=10, default='M25')
    
    # Additional geometry
    girder_spacing = models.FloatField(null=True, blank=True)
    num_girders = models.IntegerField(null=True, blank=True)
    deck_overhang = models.FloatField(null=True, blank=True)
    
    # Calculated values
    overall_width = models.FloatField(null=True, blank=True, help_text="Calculated overall bridge width")
    total_weight = models.FloatField(null=True, blank=True, help_text="Estimated total weight in tons")
    estimated_cost = models.FloatField(null=True, blank=True, help_text="Estimated cost in lakhs")
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_favorite = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"
    
    def save(self, *args, **kwargs):
        # Calculate overall width
        if self.carriageway_width:
            self.overall_width = self.carriageway_width + 5
        
        # Estimate weight (simplified calculation)
        if self.span and self.carriageway_width:
            steel_density = 7.85  # tons/m³
            concrete_density = 2.5  # tons/m³
            
            # Rough estimates
            deck_volume = self.span * self.carriageway_width * 0.25  # 0.25m thick deck
            girder_volume = self.span * 0.5 * (self.num_girders or 4)  # approximate girder volume
            
            concrete_weight = deck_volume * concrete_density
            steel_weight = girder_volume * steel_density
            
            self.total_weight = concrete_weight + steel_weight
            
            # Rough cost estimate (₹ per ton)
            steel_cost_per_ton = 60000  # ₹60,000 per ton
            concrete_cost_per_ton = 5000  # ₹5,000 per ton
            
            self.estimated_cost = (
                (steel_weight * steel_cost_per_ton + concrete_weight * concrete_cost_per_ton) / 100000
            )  # Convert to lakhs
        
        super().save(*args, **kwargs)
