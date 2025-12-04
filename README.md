# Home Mess Management System

A web-based management system for home mess operations built with Python Flask and Excel backend.

## Features

- **Add New Students**: Register students with name and payment method
- **View Student Details**: Select any student from dropdown to view:
  - Payment information (method, amount, date)
  - Daily meal records (Lunch/Dinner status)
- **Update Meal Status**: Mark lunch/dinner as Yes/No for any date
- **Update Payment**: Record payment amounts and dates
- **Excel Backend**: All data is stored in Excel file (`data/mess_data.xlsx`)

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

### Adding a New Student
1. Enter the student's name
2. Select payment method (Cash, UPI, Bank Transfer, Card, or Other)
3. Click "Add Student"

### Viewing Student Details
1. Select a student from the dropdown menu
2. View payment information and meal records
3. Update payment or meal status as needed

### Updating Meal Status
1. Select a student from the dropdown
2. Choose a date
3. Check/uncheck Lunch and/or Dinner options
4. Click "Update Meal Status"

### Updating Payment
1. Select a student from the dropdown
2. Enter payment amount
3. Select payment date
4. Click "Update Payment"

## Data Storage

All data is stored in `data/mess_data.xlsx` with the following columns:
- Student_ID: Unique identifier for each student
- Name: Student name
- Payment_Method: Payment method used
- Date: Date of meal record
- Lunch: Yes/No for lunch
- Dinner: Yes/No for dinner
- Payment_Amount: Payment amount
- Payment_Date: Date of payment

## Notes

- The Excel file is automatically created in the `data` directory when you first run the application
- All dates are stored in YYYY-MM-DD format
- Meal status can be updated day by day for each student

