# 🚀 Quick Start - Get Your Public Link in 5 Minutes

## Easiest Method: PythonAnywhere (FREE)

### Step 1: Create Account (2 minutes)
1. Go to: **https://www.pythonanywhere.com**
2. Click **"Beginner: sign up for a free account"**
3. Enter your email and create password
4. Verify your email

### Step 2: Upload Your Files (2 minutes)
1. After login, click **"Files"** tab at the top
2. Click **"Upload a file"** button
3. Upload these files:
   - ✅ `app.py`
   - ✅ `wsgi.py`
   - ✅ `requirements.txt`

4. For templates folder:
   - Create a folder called `templates` in PythonAnywhere
   - Upload all HTML files from your `templates` folder into it:
     - `base.html`
     - `index.html`
     - `doctor_detail.html`
     - `about.html`
     - `404.html`

### Step 3: Create Web App (1 minute)
1. Click **"Web"** tab at the top
2. Click **"Add a new web app"** button
3. Click **"Next"** (keep default domain)
4. Select **"Flask"** framework
5. Select **"Python 3.10"** (or latest)
6. Click **"Next"** → **"Next"** → **"All done!"**

### Step 4: Configure (1 minute)
1. Still in **"Web"** tab, scroll down to **"Code"** section
2. Find **"Source code"** - change it to: `/home/YOURUSERNAME/mysite`
   (Replace YOURUSERNAME with your actual username shown at top)
3. Find **"Working directory"** - change to: `/home/YOURUSERNAME/mysite`
4. Scroll to **"WSGI configuration file"** section
5. Click on the file link (blue text)
6. **Delete everything** in that file
7. **Paste this code** (replace YOURUSERNAME):
```python
import sys
path = '/home/YOURUSERNAME/mysite'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application
```
8. Click **Save**

### Step 5: Install Flask (1 minute)
1. Click **"Tasks"** tab
2. Click **"Bash"** (opens a console)
3. Type: `pip3.10 install --user flask`
4. Press Enter and wait for installation

### Step 6: Go Live! (30 seconds)
1. Go back to **"Web"** tab
2. Click the big green **"Reload"** button
3. Click on your website link (shown at top): `http://YOURUSERNAME.pythonanywhere.com`

## 🎉 Done! 

Your website is now live and accessible to everyone at:
**http://YOURUSERNAME.pythonanywhere.com**

Share this link with anyone - it works 24/7 without you running anything!

---

## Alternative: Render.com (Also FREE)

1. Go to: **https://render.com**
2. Sign up with GitHub (or email)
3. Click **"New +"** → **"Web Service"**
4. Connect your GitHub repo OR use **"Public Git repository"**
5. Fill in:
   - **Name**: doctor-directory
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Click **"Create Web Service"**
7. Wait 2-3 minutes
8. Get your link: `https://your-app.onrender.com`

---

## Need Help?

- PythonAnywhere: https://help.pythonanywhere.com
- Render: https://render.com/docs

