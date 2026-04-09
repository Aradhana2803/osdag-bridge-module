import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'osdag_backend.settings')
django.setup()

from bridge_design.models import LocationData

# Sample data for 5 major cities
cities_data = [
    {
        'state': 'Maharashtra',
        'district': 'Mumbai',
        'wind_speed': 44,
        'seismic_zone': 'III',
        'zone_factor': 0.16,
        'max_temp': 45,
        'min_temp': 11
    },
    {
        'state': 'Delhi',
        'district': 'New Delhi',
        'wind_speed': 47,
        'seismic_zone': 'IV',
        'zone_factor': 0.24,
        'max_temp': 47,
        'min_temp': 2
    },
    {
        'state': 'Tamil Nadu',
        'district': 'Chennai',
        'wind_speed': 50,
        'seismic_zone': 'III',
        'zone_factor': 0.16,
        'max_temp': 42,
        'min_temp': 19
    },
    {
        'state': 'Karnataka',
        'district': 'Bangalore',
        'wind_speed': 33,
        'seismic_zone': 'II',
        'zone_factor': 0.10,
        'max_temp': 36,
        'min_temp': 15
    },
    {
        'state': 'West Bengal',
        'district': 'Kolkata',
        'wind_speed': 50,
        'seismic_zone': 'III',
        'zone_factor': 0.16,
        'max_temp': 43,
        'min_temp': 12
    }
]

print("Loading sample data...")
for city_data in cities_data:
    location, created = LocationData.objects.get_or_create(**city_data)
    if created:
        print(f"✓ Added: {city_data['district']}, {city_data['state']}")
    else:
        print(f"→ Already exists: {city_data['district']}, {city_data['state']}")

print("\n✅ Sample data loaded successfully!")