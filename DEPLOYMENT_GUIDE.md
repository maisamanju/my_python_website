# Quick Deployment Guide - Get Your Public Link

## 🚀 Option 1: PythonAnywhere (Easiest - Recommended)

### Step 1: Sign Up
1. Go to https://www.pythonanywhere.com
2. Click "Beginner: sign up for a free account"
3. Create your account (free tier available)

### Step 2: Upload Files
1. After logging in, click on **Files** tab
2. Click **Upload a file** button
3. Upload these files one by one:
   - `app.py`
   - `requirements.txt`
   - `wsgi.py`
   - Upload the entire `templates` folder (zip it first, then extract on PythonAnywhere)

### Step 3: Create Web App
1. Click on **Web** tab
2. Click **Add a new web app**
3. Choose **Flask** framework
4. Select **Python 3.10** (or latest available)
5. Click **Next** until finished

### Step 4: Configure WSGI
1. In the **Web** tab, find **WSGI configuration file** section
2. Click on the file link (usually `/var/www/yourusername_pythonanywhere_com_wsgi.py`)
3. Replace all content with:
```python
import sys
path = '/home/yourusername/mysite'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application
```
(Replace `yourusername` with your actual PythonAnywhere username)

### Step 5: Install Dependencies
1. Go to **Tasks** tab
2. Click **Bash** to open a console
3. Run: `pip3.10 install --user flask`
4. Wait for installation

### Step 6: Reload Web App
1. Go back to **Web** tab
2. Click the green **Reload** button
3. Your site will be live at: `http://yourusername.pythonanywhere.com`

---

## 🌐 Option 2: Render.com (Also Easy)

### Step 1: Sign Up
1. Go to https://render.com
2. Sign up with GitHub (recommended) or email

### Step 2: Create New Web Service
1. Click **New +** → **Web Service**
2. Connect your GitHub account (or use public repo)
3. Or use **Manual Deploy** option

### Step 3: Configure
- **Name**: doctor-directory (or any name)
- **Environment**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Plan**: Free

### Step 4: Deploy
1. Click **Create Web Service**
2. Wait 2-3 minutes for deployment
3. Your site will be at: `https://your-app-name.onrender.com`

**Note**: For Render, you need to add `gunicorn` to requirements.txt

---

## 🚂 Option 3: Railway.app

### Step 1: Sign Up
1. Go to https://railway.app
2. Sign up with GitHub

### Step 2: Deploy
1. Click **New Project**
2. Select **Deploy from GitHub repo** (or upload files)
3. Railway auto-detects Flask
4. Your site will be at: `https://your-app.up.railway.app`

---

## 📝 Quick Setup for Render (Add Gunicorn)

If using Render, update requirements.txt to include gunicorn:
```
Flask==3.0.0
Werkzeug==3.0.1
gunicorn==21.2.0
```

---

## ✅ After Deployment

Once deployed, you'll get a public URL like:
- `http://yourusername.pythonanywhere.com` (PythonAnywhere)
- `https://your-app.onrender.com` (Render)
- `https://your-app.up.railway.app` (Railway)

**Share this link with anyone** - they can access it 24/7 without you running anything!

---

## 🎯 Recommended: PythonAnywhere

**Why PythonAnywhere?**
- ✅ Free tier available
- ✅ No credit card required
- ✅ Easy Flask setup
- ✅ Reliable uptime
- ✅ Perfect for this use case

