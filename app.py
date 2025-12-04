from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Doctor details data
DOCTORS = [
    {
        'id': 1,
        'name': 'Dr. Sarah Johnson',
        'specialization': 'Cardiologist',
        'qualifications': 'MBBS, MD, DM (Cardiology)',
        'experience': '15 years',
        'phone': '+1 (555) 123-4567',
        'email': 'sarah.johnson@hospital.com',
        'address': '123 Medical Center, Health Street, City, State 12345',
        'consultation_hours': 'Mon-Fri: 9:00 AM - 5:00 PM',
        'bio': 'Dr. Sarah Johnson is a renowned cardiologist with over 15 years of experience in treating heart-related conditions. She specializes in preventive cardiology and interventional procedures.',
        'image': 'https://via.placeholder.com/300x300?text=Dr.+Sarah+Johnson'
    },
    {
        'id': 2,
        'name': 'Dr. Michael Chen',
        'specialization': 'Neurologist',
        'qualifications': 'MBBS, MD, DM (Neurology)',
        'experience': '12 years',
        'phone': '+1 (555) 234-5678',
        'email': 'michael.chen@hospital.com',
        'address': '456 Brain Health Clinic, Neuro Avenue, City, State 12345',
        'consultation_hours': 'Mon-Wed-Fri: 10:00 AM - 6:00 PM',
        'bio': 'Dr. Michael Chen is an expert neurologist specializing in stroke treatment, epilepsy, and neurodegenerative diseases. He has published numerous research papers in international journals.',
        'image': 'https://via.placeholder.com/300x300?text=Dr.+Michael+Chen'
    },
    {
        'id': 3,
        'name': 'Dr. Emily Rodriguez',
        'specialization': 'Pediatrician',
        'qualifications': 'MBBS, MD, DCH',
        'experience': '10 years',
        'phone': '+1 (555) 345-6789',
        'email': 'emily.rodriguez@hospital.com',
        'address': '789 Children\'s Care Center, Kids Lane, City, State 12345',
        'consultation_hours': 'Tue-Thu-Sat: 8:00 AM - 4:00 PM',
        'bio': 'Dr. Emily Rodriguez is a compassionate pediatrician dedicated to children\'s health and wellness. She has extensive experience in treating childhood illnesses and developmental disorders.',
        'image': 'https://via.placeholder.com/300x300?text=Dr.+Emily+Rodriguez'
    }
]

@app.route('/')
def index():
    """Home page showing all doctors"""
    return render_template('index.html', doctors=DOCTORS)

@app.route('/doctor/<int:doctor_id>')
def doctor_detail(doctor_id):
    """Individual doctor detail page"""
    doctor = next((d for d in DOCTORS if d['id'] == doctor_id), None)
    if not doctor:
        return render_template('404.html'), 404
    return render_template('doctor_detail.html', doctor=doctor)

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

if __name__ == '__main__':
    # For local development
    app.run(debug=True, host='0.0.0.0', port=5000)

