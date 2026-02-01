# Step 1: Basic Django Scraper

This is the initial stage of the tutorial. I set up the Django environment and created a custom management command to run a web scraper.

## 📝 Learning Points
- Initializing a Django project and app.
- Creating a `ScrapedData` model to store information in SQLite.
- Using **Selenium** within a Django Service to extract `h1` and `a` tags from the instructor's test page.

## 🚀 Key Command
```bash
python manage.py scraper
```