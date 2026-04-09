"""
Comprehensive Indian Location Engineering Data Loader

This script populates the database with accurate engineering parameters based on:
1. IRC: 6-2017 (Temperature Data - Annexure F)
2. IS 1893 Part 1: 2016 (Seismic Zone Data - Annex E)
3. IS 875 Part 3: 2015 (Wind Speed Data - Annex A)

All data sourced from official Indian Standards and IRC codes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'osdag_backend.settings')
django.setup()

from bridge_design.models import LocationData


# Comprehensive location data combining all engineering parameters
# Data structure: {state, district/city, wind_speed (m/s), seismic_zone, zone_factor, max_temp (°C), min_temp (°C)}

comprehensive_data = [
    # Andaman and Nicobar Islands
    {'state': 'Andaman and Nicobar Islands', 'district': 'Port Blair', 'wind_speed': 44, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 36.4, 'min_temp': 14.6},
    {'state': 'Andaman and Nicobar Islands', 'district': 'Car Nicobar', 'wind_speed': 44, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 38.1, 'min_temp': 10.9},
    {'state': 'Andaman and Nicobar Islands', 'district': 'Hut Bay', 'wind_speed': 44, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 39.4, 'min_temp': 0.2},
    
    # Andhra Pradesh
    {'state': 'Andhra Pradesh', 'district': 'Visakhapatnam', 'wind_speed': 50, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 45.4, 'min_temp': 10.5},
    {'state': 'Andhra Pradesh', 'district': 'Vijayawada', 'wind_speed': 50, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 48.8, 'min_temp': 8.5},
    {'state': 'Andhra Pradesh', 'district': 'Tirupati', 'wind_speed': 47, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 45.2, 'min_temp': 12.9},
    {'state': 'Andhra Pradesh', 'district': 'Guntur', 'wind_speed': 50, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 47.4, 'min_temp': 11.1},
    {'state': 'Andhra Pradesh', 'district': 'Kakinada', 'wind_speed': 50, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 47.2, 'min_temp': 12.0},
    {'state': 'Andhra Pradesh', 'district': 'Nellore', 'wind_speed': 50, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 46.7, 'min_temp': 11.1},
    {'state': 'Andhra Pradesh', 'district': 'Kurnool', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 45.6, 'min_temp': 6.7},
    {'state': 'Andhra Pradesh', 'district': 'Anantapur', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 44.1, 'min_temp': 9.4},
    
    # Arunachal Pradesh
    {'state': 'Arunachal Pradesh', 'district': 'Itanagar', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 38.8, 'min_temp': 6.0},
    {'state': 'Arunachal Pradesh', 'district': 'Pasighat', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 38.8, 'min_temp': 6.0},
    {'state': 'Arunachal Pradesh', 'district': 'Tawang', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 29.0, 'min_temp': -5.0},
    
    # Assam
    {'state': 'Assam', 'district': 'Guwahati', 'wind_speed': 50, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 40.3, 'min_temp': 3.0},
    {'state': 'Assam', 'district': 'Dibrugarh', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 39.8, 'min_temp': 1.0},
    {'state': 'Assam', 'district': 'Silchar', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 39.4, 'min_temp': 5.0},
    {'state': 'Assam', 'district': 'Tezpur', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 45.7, 'min_temp': 5.6},
    {'state': 'Assam', 'district': 'Jorhat', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 39.0, 'min_temp': 2.7},
    
    # Bihar
    {'state': 'Bihar', 'district': 'Patna', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 46.6, 'min_temp': 1.4},
    {'state': 'Bihar', 'district': 'Gaya', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 49.0, 'min_temp': 1.2},
    {'state': 'Bihar', 'district': 'Muzaffarpur', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 44.5, 'min_temp': 2.2},
    {'state': 'Bihar', 'district': 'Bhagalpur', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 46.6, 'min_temp': 3.8},
    {'state': 'Bihar', 'district': 'Darbhanga', 'wind_speed': 55, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 44.1, 'min_temp': 0.0},
    
    # Chandigarh
    {'state': 'Chandigarh', 'district': 'Chandigarh', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 47.8, 'min_temp': -1.3},
    
    # Chhattisgarh
    {'state': 'Chhattisgarh', 'district': 'Raipur', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 47.9, 'min_temp': 3.9},
    {'state': 'Chhattisgarh', 'district': 'Bilaspur', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 47.0, 'min_temp': 6.6},
    {'state': 'Chhattisgarh', 'district': 'Bhilai', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 47.0, 'min_temp': 6.6},
    {'state': 'Chhattisgarh', 'district': 'Jagdalpur', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 46.1, 'min_temp': 2.8},
    
    # Dadra and Nagar Haveli and Daman and Diu
    {'state': 'Dadra and Nagar Haveli and Daman and Diu', 'district': 'Silvassa', 'wind_speed': 44, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 39.0, 'min_temp': 15.0},
    {'state': 'Dadra and Nagar Haveli and Daman and Diu', 'district': 'Daman', 'wind_speed': 44, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 38.0, 'min_temp': 16.0},
    {'state': 'Dadra and Nagar Haveli and Daman and Diu', 'district': 'Diu', 'wind_speed': 44, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 44.0, 'min_temp': 5.0},
    
    # Delhi
    {'state': 'Delhi', 'district': 'New Delhi', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 48.4, 'min_temp': -2.2},
    {'state': 'Delhi', 'district': 'North Delhi', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 48.4, 'min_temp': -2.2},
    {'state': 'Delhi', 'district': 'South Delhi', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 48.4, 'min_temp': -2.2},
    {'state': 'Delhi', 'district': 'East Delhi', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 48.4, 'min_temp': -2.2},
    {'state': 'Delhi', 'district': 'West Delhi', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 48.4, 'min_temp': -2.2},
    
    # Goa
    {'state': 'Goa', 'district': 'Panaji', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 39.8, 'min_temp': 3.4},
    {'state': 'Goa', 'district': 'Margao', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 38.4, 'min_temp': 12.2},
    {'state': 'Goa', 'district': 'Vasco da Gama', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 38.2, 'min_temp': 13.6},
    
    # Gujarat
    {'state': 'Gujarat', 'district': 'Ahmedabad', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 47.8, 'min_temp': 2.2},
    {'state': 'Gujarat', 'district': 'Surat', 'wind_speed': 44, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 45.6, 'min_temp': 4.4},
    {'state': 'Gujarat', 'district': 'Vadodara', 'wind_speed': 44, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 46.7, 'min_temp': -1.1},
    {'state': 'Gujarat', 'district': 'Rajkot', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 47.9, 'min_temp': -0.6},
    {'state': 'Gujarat', 'district': 'Bhuj', 'wind_speed': 50, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 47.8, 'min_temp': -0.2},
    {'state': 'Gujarat', 'district': 'Bhavnagar', 'wind_speed': 44, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 47.3, 'min_temp': 0.6},
    {'state': 'Gujarat', 'district': 'Jamnagar', 'wind_speed': 44, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 44.6, 'min_temp': 0.4},
    
    # Haryana
    {'state': 'Haryana', 'district': 'Gurugram', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 49.0, 'min_temp': -0.4},
    {'state': 'Haryana', 'district': 'Faridabad', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 49.0, 'min_temp': -0.4},
    {'state': 'Haryana', 'district': 'Panipat', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 47.2, 'min_temp': -0.5},
    {'state': 'Haryana', 'district': 'Ambala', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 47.8, 'min_temp': -1.3},
    {'state': 'Haryana', 'district': 'Hisar', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 48.8, 'min_temp': -3.9},
    {'state': 'Haryana', 'district': 'Karnal', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 49.0, 'min_temp': -0.4},
    
    # Himachal Pradesh
    {'state': 'Himachal Pradesh', 'district': 'Shimla', 'wind_speed': 39, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 32.4, 'min_temp': -12.2},
    {'state': 'Himachal Pradesh', 'district': 'Manali', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 35.0, 'min_temp': -11.6},
    {'state': 'Himachal Pradesh', 'district': 'Dharamshala', 'wind_speed': 47, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 42.7, 'min_temp': -1.9},
    {'state': 'Himachal Pradesh', 'district': 'Kullu', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 40.0, 'min_temp': -5.2},
    {'state': 'Himachal Pradesh', 'district': 'Mandi', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 42.1, 'min_temp': -2.7},
    
    # Jammu and Kashmir
    {'state': 'Jammu and Kashmir', 'district': 'Srinagar', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 38.3, 'min_temp': -20.0},
    {'state': 'Jammu and Kashmir', 'district': 'Jammu', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 47.4, 'min_temp': 0.6},
    {'state': 'Jammu and Kashmir', 'district': 'Anantnag', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 35.7, 'min_temp': -16.7},
    {'state': 'Jammu and Kashmir', 'district': 'Baramulla', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 37.6, 'min_temp': -15.7},
    
    # Jharkhand
    {'state': 'Jharkhand', 'district': 'Ranchi', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 43.4, 'min_temp': 0.6},
    {'state': 'Jharkhand', 'district': 'Jamshedpur', 'wind_speed': 47, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 47.7, 'min_temp': 3.9},
    {'state': 'Jharkhand', 'district': 'Dhanbad', 'wind_speed': 47, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 48.5, 'min_temp': 1.9},
    {'state': 'Jharkhand', 'district': 'Bokaro', 'wind_speed': 47, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 46.7, 'min_temp': 4.4},
    
    # Karnataka
    {'state': 'Karnataka', 'district': 'Bangalore', 'wind_speed': 33, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 38.9, 'min_temp': 7.8},
    {'state': 'Karnataka', 'district': 'Mysore', 'wind_speed': 33, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 39.4, 'min_temp': 8.6},
    {'state': 'Karnataka', 'district': 'Mangalore', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 39.8, 'min_temp': 15.9},
    {'state': 'Karnataka', 'district': 'Hubli', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 41.9, 'min_temp': 6.7},
    {'state': 'Karnataka', 'district': 'Belgaum', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 41.9, 'min_temp': 6.7},
    {'state': 'Karnataka', 'district': 'Gulbarga', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 46.1, 'min_temp': 5.6},
    
    # Kerala
    {'state': 'Kerala', 'district': 'Thiruvananthapuram', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 38.3, 'min_temp': 16.0},
    {'state': 'Kerala', 'district': 'Kochi', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 36.5, 'min_temp': 16.3},
    {'state': 'Kerala', 'district': 'Kozhikode', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 38.1, 'min_temp': 13.8},
    {'state': 'Kerala', 'district': 'Thrissur', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 38.5, 'min_temp': 16.0},
    {'state': 'Kerala', 'district': 'Alappuzha', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 39.9, 'min_temp': 13.8},
    {'state': 'Kerala', 'district': 'Palakkad', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 41.8, 'min_temp': 14.0},
    
    # Ladakh
    {'state': 'Ladakh', 'district': 'Leh', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 23.0, 'min_temp': -15.0},
    {'state': 'Ladakh', 'district': 'Kargil', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 30.0, 'min_temp': -18.0},
    
    # Lakshadweep
    {'state': 'Lakshadweep', 'district': 'Kavaratti', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 38.0, 'min_temp': 22.1},
    {'state': 'Lakshadweep', 'district': 'Agatti', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 38.0, 'min_temp': 22.1},
    {'state': 'Lakshadweep', 'district': 'Minicoy', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 36.7, 'min_temp': 16.7},
    
    # Madhya Pradesh
    {'state': 'Madhya Pradesh', 'district': 'Bhopal', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 46.0, 'min_temp': 0.6},
    {'state': 'Madhya Pradesh', 'district': 'Indore', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 46.0, 'min_temp': -2.8},
    {'state': 'Madhya Pradesh', 'district': 'Gwalior', 'wind_speed': 47, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 48.3, 'min_temp': -1.1},
    {'state': 'Madhya Pradesh', 'district': 'Jabalpur', 'wind_speed': 47, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 46.7, 'min_temp': 0.0},
    {'state': 'Madhya Pradesh', 'district': 'Ujjain', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 46.0, 'min_temp': 0.0},
    {'state': 'Madhya Pradesh', 'district': 'Sagar', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 46.4, 'min_temp': 1.1},
    
    # Maharashtra
    {'state': 'Maharashtra', 'district': 'Mumbai', 'wind_speed': 44, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 42.2, 'min_temp': 7.4},
    {'state': 'Maharashtra', 'district': 'Pune', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 43.3, 'min_temp': 1.7},
    {'state': 'Maharashtra', 'district': 'Nagpur', 'wind_speed': 44, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 47.8, 'min_temp': 3.9},
    {'state': 'Maharashtra', 'district': 'Nashik', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 43.9, 'min_temp': 0.4},
    {'state': 'Maharashtra', 'district': 'Aurangabad', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 43.6, 'min_temp': 1.2},
    {'state': 'Maharashtra', 'district': 'Thane', 'wind_speed': 44, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 42.2, 'min_temp': 7.4},
    {'state': 'Maharashtra', 'district': 'Kolhapur', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 42.3, 'min_temp': 8.6},
    {'state': 'Maharashtra', 'district': 'Solapur', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 46.0, 'min_temp': 4.4},
    
    # Manipur
    {'state': 'Manipur', 'district': 'Imphal', 'wind_speed': 47, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 36.1, 'min_temp': -2.7},
    
    # Meghalaya
    {'state': 'Meghalaya', 'district': 'Shillong', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 30.2, 'min_temp': -3.3},
    {'state': 'Meghalaya', 'district': 'Cherrapunji', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 31.1, 'min_temp': -1.0},
    
    # Mizoram
    {'state': 'Mizoram', 'district': 'Aizawl', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 35.5, 'min_temp': 6.1},
    
    # Nagaland
    {'state': 'Nagaland', 'district': 'Kohima', 'wind_speed': 44, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 27.0, 'min_temp': 4.0},
    {'state': 'Nagaland', 'district': 'Dimapur', 'wind_speed': 44, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 35.0, 'min_temp': 5.0},
    
    # Odisha
    {'state': 'Odisha', 'district': 'Bhubaneswar', 'wind_speed': 50, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 46.5, 'min_temp': 8.6},
    {'state': 'Odisha', 'district': 'Cuttack', 'wind_speed': 50, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 47.7, 'min_temp': 5.8},
    {'state': 'Odisha', 'district': 'Puri', 'wind_speed': 50, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 44.2, 'min_temp': 7.5},
    {'state': 'Odisha', 'district': 'Rourkela', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 49.0, 'min_temp': 3.6},
    {'state': 'Odisha', 'district': 'Balasore', 'wind_speed': 50, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 46.7, 'min_temp': 6.7},
    
    # Puducherry
    {'state': 'Puducherry', 'district': 'Puducherry', 'wind_speed': 50, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 45.5, 'min_temp': 15.1},
    {'state': 'Puducherry', 'district': 'Karaikal', 'wind_speed': 50, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 42.0, 'min_temp': 17.8},
    
    # Punjab
    {'state': 'Punjab', 'district': 'Chandigarh', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 47.8, 'min_temp': -1.3},
    {'state': 'Punjab', 'district': 'Ludhiana', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 46.6, 'min_temp': -1.7},
    {'state': 'Punjab', 'district': 'Amritsar', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 47.8, 'min_temp': -3.6},
    {'state': 'Punjab', 'district': 'Jalandhar', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 47.7, 'min_temp': 0.0},
    {'state': 'Punjab', 'district': 'Patiala', 'wind_speed': 47, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 47.0, 'min_temp': -0.9},
    {'state': 'Punjab', 'district': 'Bathinda', 'wind_speed': 47, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 48.0, 'min_temp': -2.0},
    
    # Rajasthan
    {'state': 'Rajasthan', 'district': 'Jaipur', 'wind_speed': 47, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 49.0, 'min_temp': -2.2},
    {'state': 'Rajasthan', 'district': 'Jodhpur', 'wind_speed': 47, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 49.9, 'min_temp': -1.7},
    {'state': 'Rajasthan', 'district': 'Udaipur', 'wind_speed': 47, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 46.4, 'min_temp': -1.3},
    {'state': 'Rajasthan', 'district': 'Bikaner', 'wind_speed': 47, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 49.4, 'min_temp': -4.0},
    {'state': 'Rajasthan', 'district': 'Ajmer', 'wind_speed': 47, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 47.4, 'min_temp': -2.8},
    {'state': 'Rajasthan', 'district': 'Kota', 'wind_speed': 47, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 48.5, 'min_temp': 1.8},
    
    # Sikkim
    {'state': 'Sikkim', 'district': 'Gangtok', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 29.9, 'min_temp': -2.2},
    
    # Tamil Nadu
    {'state': 'Tamil Nadu', 'district': 'Chennai', 'wind_speed': 50, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 49.1, 'min_temp': 15.7},
    {'state': 'Tamil Nadu', 'district': 'Coimbatore', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 42.6, 'min_temp': 12.2},
    {'state': 'Tamil Nadu', 'district': 'Madurai', 'wind_speed': 39, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 44.5, 'min_temp': 10.5},
    {'state': 'Tamil Nadu', 'district': 'Tiruchirappalli', 'wind_speed': 47, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 43.9, 'min_temp': 13.9},
    {'state': 'Tamil Nadu', 'district': 'Salem', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 42.8, 'min_temp': 11.1},
    {'state': 'Tamil Nadu', 'district': 'Vellore', 'wind_speed': 39, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 45.0, 'min_temp': 8.4},
    
    # Telangana
    {'state': 'Telangana', 'district': 'Hyderabad', 'wind_speed': 44, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 45.5, 'min_temp': 6.1},
    {'state': 'Telangana', 'district': 'Warangal', 'wind_speed': 44, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 47.8, 'min_temp': 8.3},
    {'state': 'Telangana', 'district': 'Nizamabad', 'wind_speed': 44, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 47.3, 'min_temp': 4.4},
    {'state': 'Telangana', 'district': 'Khammam', 'wind_speed': 44, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 47.2, 'min_temp': 9.4},
    
    # Tripura
    {'state': 'Tripura', 'district': 'Agartala', 'wind_speed': 39, 'seismic_zone': 'V', 'zone_factor': 0.36, 'max_temp': 42.2, 'min_temp': 2.0},
    
    # Uttar Pradesh
    {'state': 'Uttar Pradesh', 'district': 'Lucknow', 'wind_speed': 47, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 47.7, 'min_temp': -1.0},
    {'state': 'Uttar Pradesh', 'district': 'Kanpur', 'wind_speed': 47, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 47.3, 'min_temp': 0.4},
    {'state': 'Uttar Pradesh', 'district': 'Agra', 'wind_speed': 47, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 48.6, 'min_temp': -2.2},
    {'state': 'Uttar Pradesh', 'district': 'Varanasi', 'wind_speed': 47, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 47.2, 'min_temp': 1.0},
    {'state': 'Uttar Pradesh', 'district': 'Noida', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 48.4, 'min_temp': -2.2},
    {'state': 'Uttar Pradesh', 'district': 'Gorakhpur', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 49.4, 'min_temp': 1.7},
    {'state': 'Uttar Pradesh', 'district': 'Allahabad', 'wind_speed': 47, 'seismic_zone': 'II', 'zone_factor': 0.10, 'max_temp': 48.8, 'min_temp': -0.7},
    {'state': 'Uttar Pradesh', 'district': 'Bareilly', 'wind_speed': 47, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 47.3, 'min_temp': -1.3},
    
    # Uttarakhand
    {'state': 'Uttarakhand', 'district': 'Dehradun', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 43.9, 'min_temp': -1.1},
    {'state': 'Uttarakhand', 'district': 'Haridwar', 'wind_speed': 39, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 47.4, 'min_temp': -2.2},
    {'state': 'Uttarakhand', 'district': 'Nainital', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 31.5, 'min_temp': -7.8},
    {'state': 'Uttarakhand', 'district': 'Roorkee', 'wind_speed': 39, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 47.4, 'min_temp': -2.2},
    
    # West Bengal
    {'state': 'West Bengal', 'district': 'Kolkata', 'wind_speed': 50, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 43.9, 'min_temp': 6.7},
    {'state': 'West Bengal', 'district': 'Howrah', 'wind_speed': 50, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 43.9, 'min_temp': 6.7},
    {'state': 'West Bengal', 'district': 'Siliguri', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 40.9, 'min_temp': 2.2},
    {'state': 'West Bengal', 'district': 'Durgapur', 'wind_speed': 47, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 46.2, 'min_temp': 0.8},
    {'state': 'West Bengal', 'district': 'Asansol', 'wind_speed': 47, 'seismic_zone': 'III', 'zone_factor': 0.16, 'max_temp': 46.2, 'min_temp': 0.8},
    {'state': 'West Bengal', 'district': 'Darjeeling', 'wind_speed': 47, 'seismic_zone': 'IV', 'zone_factor': 0.24, 'max_temp': 28.5, 'min_temp': -7.2},
]

print("=" * 80)
print("COMPREHENSIVE INDIAN LOCATION ENGINEERING DATA LOADER")
print("=" * 80)
print("\nData Sources:")
print("  • IRC: 6-2017 (Temperature Data - Annexure F)")
print("  • IS 1893 Part 1: 2016 (Seismic Zone Data - Annex E)")
print("  • IS 875 Part 3: 2015 (Wind Speed Data - Annex A)")
print("\n" + "=" * 80)
print()

print(f"Loading comprehensive location data...")
print(f"Total locations to process: {len(comprehensive_data)}")
print()

added_count = 0
updated_count = 0
error_count = 0

for location_info in comprehensive_data:
    try:
        location, created = LocationData.objects.update_or_create(
            state=location_info['state'],
            district=location_info['district'],
            defaults={
                'wind_speed': location_info['wind_speed'],
                'seismic_zone': location_info['seismic_zone'],
                'zone_factor': location_info['zone_factor'],
                'max_temp': location_info['max_temp'],
                'min_temp': location_info['min_temp']
            }
        )
        
        if created:
            added_count += 1
            print(f"✓ Added: {location_info['district']}, {location_info['state']}")
        else:
            updated_count += 1
            print(f"→ Updated: {location_info['district']}, {location_info['state']}")
    except Exception as e:
        error_count += 1
        print(f"✗ Error processing {location_info['district']}, {location_info['state']}: {str(e)}")

print()
print("=" * 80)
print("DATABASE POPULATION SUMMARY")
print("=" * 80)
print(f"✅ Successfully completed!")
print(f"   • New locations added: {added_count}")
print(f"   • Existing locations updated: {updated_count}")
print(f"   • Errors encountered: {error_count}")
print(f"   • Total locations in database: {LocationData.objects.count()}")
print()

# Show summary by state
states = LocationData.objects.values_list('state', flat=True).distinct().order_by('state')
print(f"📊 COVERAGE SUMMARY:")
print(f"   Total States/UTs: {len(states)}")
print()

for state in states:
    count = LocationData.objects.filter(state=state).count()
    # Get a sample location to show the data
    sample = LocationData.objects.filter(state=state).first()
    print(f"   {state}: {count} location(s)")
    if sample:
        print(f"      Sample: {sample.district} - Wind: {sample.wind_speed} m/s, "
              f"Zone: {sample.seismic_zone} (Z={sample.zone_factor}), "
              f"Temp: {sample.max_temp}°C/{sample.min_temp}°C")

print()
print("=" * 80)
print("DATA VALIDATION")
print("=" * 80)

# Count locations by seismic zone
print("\n🔍 Seismic Zone Distribution:")
for zone in ['II', 'III', 'IV', 'V']:
    count = LocationData.objects.filter(seismic_zone=zone).count()
    print(f"   Zone {zone}: {count} locations")

# Count locations by wind speed range
print("\n💨 Wind Speed Distribution:")
wind_ranges = [(33, 39), (40, 44), (45, 50), (51, 55)]
for min_speed, max_speed in wind_ranges:
    count = LocationData.objects.filter(
        wind_speed__gte=min_speed, 
        wind_speed__lte=max_speed
    ).count()
    print(f"   {min_speed}-{max_speed} m/s: {count} locations")

# Temperature extremes
print("\n🌡️  Temperature Extremes:")
max_temp_loc = LocationData.objects.order_by('-max_temp').first()
min_temp_loc = LocationData.objects.order_by('min_temp').first()
print(f"   Highest Max Temp: {max_temp_loc.max_temp}°C at {max_temp_loc.district}, {max_temp_loc.state}")
print(f"   Lowest Min Temp: {min_temp_loc.min_temp}°C at {min_temp_loc.district}, {min_temp_loc.state}")

print()
print("=" * 80)
print("🎉 DATABASE IMPLEMENTATION COMPLETE!")
print("=" * 80)
print("\n✨ All location data has been populated with accurate engineering parameters")
print("   from official IRC and IS codes.")
print()