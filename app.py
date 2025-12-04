from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
import os
from datetime import datetime
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Excel file path
EXCEL_FILE = 'data/mess_data.xlsx'
DATA_DIR = 'data'

# Ensure data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def init_excel_file():
    """Initialize Excel file with proper structure if it doesn't exist"""
    if not os.path.exists(EXCEL_FILE):
        # Create initial DataFrame structure
        df = pd.DataFrame(columns=[
            'Student_ID', 'Name', 'Payment_Method', 'Date', 
            'Lunch', 'Dinner', 'Payment_Amount', 'Payment_Date'
        ])
        df.to_excel(EXCEL_FILE, index=False)

def get_all_students():
    """Get list of all unique students"""
    if not os.path.exists(EXCEL_FILE):
        return []
    
    df = pd.read_excel(EXCEL_FILE)
    if df.empty:
        return []
    
    # Get unique students with their basic info
    students = []
    for student_id in df['Student_ID'].unique():
        student_row = df[df['Student_ID'] == student_id].iloc[0]
        students.append({
            'id': student_id,
            'name': student_row['Name'],
            'payment_method': student_row['Payment_Method']
        })
    return students

def get_student_details(student_id):
    """Get all details for a specific student"""
    if not os.path.exists(EXCEL_FILE):
        return None
    
    df = pd.read_excel(EXCEL_FILE)
    student_data = df[df['Student_ID'] == student_id].copy()
    
    if student_data.empty:
        return None
    
    # Convert dates to strings for JSON serialization
    student_data['Date'] = pd.to_datetime(student_data['Date']).dt.strftime('%Y-%m-%d')
    student_data['Payment_Date'] = pd.to_datetime(student_data['Payment_Date']).dt.strftime('%Y-%m-%d')
    
    return {
        'id': student_id,
        'name': student_data.iloc[0]['Name'],
        'payment_method': student_data.iloc[0]['Payment_Method'],
        'records': student_data.to_dict('records')
    }

def add_student(name, payment_method):
    """Add a new student"""
    if not os.path.exists(EXCEL_FILE):
        init_excel_file()
    
    df = pd.read_excel(EXCEL_FILE)
    
    # Generate new student ID
    if df.empty:
        new_id = 1
    else:
        new_id = int(df['Student_ID'].max()) + 1
    
    # Add initial record for today
    today = datetime.now().strftime('%Y-%m-%d')
    new_row = {
        'Student_ID': new_id,
        'Name': name,
        'Payment_Method': payment_method,
        'Date': today,
        'Lunch': 'No',
        'Dinner': 'No',
        'Payment_Amount': 0,
        'Payment_Date': today
    }
    
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_excel(EXCEL_FILE, index=False)
    
    return new_id

def update_meal_status(student_id, date, lunch, dinner):
    """Update meal status for a specific student and date"""
    if not os.path.exists(EXCEL_FILE):
        return False
    
    df = pd.read_excel(EXCEL_FILE)
    
    # Check if record exists for this student and date
    mask = (df['Student_ID'] == student_id) & (df['Date'] == date)
    
    if mask.any():
        # Update existing record
        df.loc[mask, 'Lunch'] = lunch
        df.loc[mask, 'Dinner'] = dinner
    else:
        # Create new record for this date
        student_info = df[df['Student_ID'] == student_id].iloc[0]
        new_row = {
            'Student_ID': student_id,
            'Name': student_info['Name'],
            'Payment_Method': student_info['Payment_Method'],
            'Date': date,
            'Lunch': lunch,
            'Dinner': dinner,
            'Payment_Amount': 0,
            'Payment_Date': student_info.get('Payment_Date', date)
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    
    df.to_excel(EXCEL_FILE, index=False)
    return True

def update_payment(student_id, amount, payment_date):
    """Update payment information for a student"""
    if not os.path.exists(EXCEL_FILE):
        return False
    
    df = pd.read_excel(EXCEL_FILE)
    
    # Update payment for all records of this student
    df.loc[df['Student_ID'] == student_id, 'Payment_Amount'] = amount
    df.loc[df['Student_ID'] == student_id, 'Payment_Date'] = payment_date
    
    df.to_excel(EXCEL_FILE, index=False)
    return True

@app.route('/')
def index():
    """Main page"""
    students = get_all_students()
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['POST'])
def add_student_route():
    """Add a new student"""
    name = request.form.get('name')
    payment_method = request.form.get('payment_method')
    
    if name and payment_method:
        student_id = add_student(name, payment_method)
        return redirect(url_for('index'))
    
    return redirect(url_for('index'))

@app.route('/get_student/<int:student_id>')
def get_student_route(student_id):
    """Get student details as JSON"""
    details = get_student_details(student_id)
    if details:
        return jsonify(details)
    return jsonify({'error': 'Student not found'}), 404

@app.route('/update_meal', methods=['POST'])
def update_meal_route():
    """Update meal status"""
    student_id = int(request.form.get('student_id'))
    date = request.form.get('date')
    # Checkboxes send 'Yes' if checked, otherwise not present (default to 'No')
    lunch = 'Yes' if request.form.get('lunch') == 'Yes' else 'No'
    dinner = 'Yes' if request.form.get('dinner') == 'Yes' else 'No'
    
    if update_meal_status(student_id, date, lunch, dinner):
        return redirect(url_for('index'))
    
    return redirect(url_for('index'))

@app.route('/update_payment', methods=['POST'])
def update_payment_route():
    """Update payment information"""
    student_id = int(request.form.get('student_id'))
    amount = float(request.form.get('amount', 0))
    payment_date = request.form.get('payment_date')
    
    if update_payment(student_id, amount, payment_date):
        return redirect(url_for('index'))
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_excel_file()
    app.run(debug=True, host='0.0.0.0', port=5000)

