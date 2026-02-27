import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config.database import save_resume_data, init_database

init_database()

data = {
    'personal_info': {
        'full_name': 'Test User',
        'email': 'test@test.com',
        'phone': '1234567890',
        'linkedin': 'None',
        'github': 'None',
        'portfolio': 'None'
    },
    'summary': 'Test',
    'target_role': 'Test',
    'target_category': 'Test',
    'education': [],
    'experience': [],
    'projects': [],
    'skills': [],
    'template': 'Modern'
}

try:
    res = save_resume_data(data)
    print("Result:", res)
except Exception as e:
    print("Error:", e)
