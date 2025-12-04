from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Dr. Khansaa Khidir details
DOCTOR = {
    'name': 'Dr. Khansaa Khidir',
    'full_name': 'Dr. Khansaa Khidir',
    'specialization': 'Consultant Obstetricians & Gynaecologist',
    'location': 'Abu Dhabi',
    'experience': 'More than 8 years',
    'experience_details': 'Dr. Khansaa has more than 8 years of experience in many leading medical centers in UAE and Sudan. She was an Obstetrics & Gynecology Specialist at a reputable hospital in Al Ain before joining Danat Al Emarat. She also has teaching experience giving lectures to medical students and interns.',
    'special_interests': 'Fetomaternal Medicine and Reproductive Medicine',
    'education': [
        {
            'degree': 'Medical Degree',
            'institution': 'Omdurman Islamic University, Sudan',
            'year': '2007'
        },
        {
            'degree': 'MRCOG Part 1',
            'institution': 'Royal College of Obstetrics & Gynecology, UK',
            'year': '2008'
        },
        {
            'degree': 'Clinical MD in Obstetrics & Gynecology',
            'institution': 'Sudan Medical Specialization Board',
            'year': '2016'
        },
        {
            'degree': 'Member of Arab Board of Health Specialization',
            'institution': 'Arab Board of Health Specialization in Obstetrics & Gynecology',
            'year': '2017'
        }
    ],
    'hospital': 'Danat Al Emarat Hospital for Women & Children',
    'location_full': 'Abu Dhabi, UAE',
    'booking_link': 'https://okdc.me/bh0W7Q',
    'image': 'https://www.okadoc.com/uploads/doctor/photo/khansaa-khidir.jpg'
}

@app.route('/')
def index():
    """Home page showing Dr. Khansaa Khidir"""
    return render_template('doctor_detail.html', doctor=DOCTOR)

if __name__ == '__main__':
    # For local development
    app.run(debug=True, host='0.0.0.0', port=5000)

