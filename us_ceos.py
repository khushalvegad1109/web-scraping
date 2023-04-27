from linkedin_api import Linkedin
import re

def search_ceos():
    api = Linkedin('khushalvegad11@gmail.com', 'Vk@11092000')
    
    search_params = {
        'keywords': 'CEO',
        'location': 'United States',
    }
    
    search_results = api.search_people(search_params)
    
    ceo_profiles = []
    
    for profile in search_results['elements']:
        if 'CEO' in profile['title']:
            ceo_profiles.append(profile)
    
    ceos = []
    for profile in ceo_profiles:
        name = f"{profile['firstName']} {profile['lastName']}"
        location = re.search(r"\bUnited States\b", profile['locationName'])
        if location:
            ceos.append(name)
    
    return ceos

ceos = search_ceos()
print(ceos)