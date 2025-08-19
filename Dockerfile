# שלב 1: תמונת בסיס לפייתון
FROM python:3.11-slim

# שלב 2: קביעת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# שלב 3: העתקת קובץ הדרישות
COPY requirements.txt .

# שלב 4: התקנת התלויות
RUN pip install --no-cache-dir -r requirements.txt

# שלב 5: העתקת שאר קבצי האפליקציה
COPY . .

# שלב 6: חשיפת פורט 8000 (הפורט שבו FastAPI עובד)
EXPOSE 8000

# שלב 7: הפעלת שרת uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]