# Doctor Directory Website

A Python Flask web application to display doctor details that can be accessed publicly via a link.

## Features

- Display list of all doctors
- Individual doctor detail pages
- Responsive and modern UI
- Easy to deploy to free hosting services

## Quick Start

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and visit: `http://localhost:5000`

## Deployment Options (Free Hosting)

### Option 1: PythonAnywhere (Recommended - Free Tier Available)

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your files via the Files tab
3. Go to Web tab and create a new web app
4. Set the source code path and WSGI configuration file
5. Your site will be available at `yourusername.pythonanywhere.com`

### Option 2: Render.com (Free Tier Available)

1. Sign up at [render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository or upload files
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`
6. Your site will be available at `your-app.onrender.com`

### Option 3: Railway.app (Free Tier Available)

1. Sign up at [railway.app](https://railway.app)
2. Create a new project
3. Deploy from GitHub or upload files
4. Railway will automatically detect Flask and deploy

### Option 4: Heroku (Free Tier Discontinued, but Paid Options Available)

1. Install Heroku CLI
2. Create `Procfile` with: `web: gunicorn app:app`
3. Deploy using: `git push heroku main`

## Customizing Doctor Data

Edit the `DOCTORS` list in `app.py` to add, modify, or remove doctor information.

## Project Structure

```
.
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── templates/
    ├── base.html         # Base template
    ├── index.html        # Home page
    ├── doctor_detail.html # Individual doctor page
    ├── about.html        # About page
    └── 404.html          # Error page
```

## Requirements

- Python 3.7+
- Flask 3.0.0

## Notes

- The application uses placeholder images. Replace with actual doctor photos by updating the `image` field in the `DOCTORS` data.
- For production deployment, set `debug=False` in `app.py`
- Consider using environment variables for sensitive configuration

