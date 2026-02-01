# 🚀 Django Web Scraper: Tutorial Project

This repository contains a web scraping system developed as part of a technical tutorial provided by **Factoria F5 Madrid**. The project demonstrates a step-by-step transition from a local script to a fully automated, containerized scraping service.

---

## 📝 Project Overview
This project follows a 4-step learning path to build a containerized scraping tool:
- **Target Site:** [jorgebenitezlopez.com](https://jorgebenitezlopez.com) (Instructor's test page)
- **Core Logic:** Captures headers (`h1`) and links (`a`) while performing automated debugging via screenshots.
- **Source Material:** [Factoria-F5-madrid/webscraper](https://github.com/Factoria-F5-madrid/webscraper)

---

## ✨ Features Covered
- **Django Integration:** Storing scraped data into a structured SQLite database using Django ORM.
- **Containerization:** Running a headless Firefox browser (GeckoDriver) inside a Docker container.
- **Automation:** Scheduling the scraper to run automatically every 5 minutes using Linux Cron.
- **Visual Debugging:** Capturing browser screenshots with timestamps to monitor the scraping status within the container.

---

## 🛠 Tech Stack
- **Language:** Python 3.11+
- **Framework:** Django 5.x / 6.x
- **Automation:** Selenium (Firefox/GeckoDriver)
- **DevOps:** Docker & Docker Compose
- **Scheduling:** Linux Cron

---

## 🚀 How to Run (Docker)

### 1. Build and Start the Containers
```bash
docker compose up --build -d
```

### 2. Database Setup
```bash
docker exec -it webscraper-server-1 python manage.py migrate
```

### 3. Run the Scraper Manually
```bash
docker exec -it webscraper-server-1 python manage.py scraper
```

### 4. Monitor Results
- Screenshots: Automatically saved in the `./screenshots` folder on your local machine via volume mapping.
- Automation Logs: Check `/var/log/cron.log` inside the container for execution history.

---

## 📂 Project Evolution (Branch History)

- **master (Step 1):** Initial Django setup and basic scraping functionality.
- **docker (Step 2):** Moving the environment into Docker with Selenium and Firefox.
- **cronjob (Step 3):** Implementation of automated scheduling using Linux Cron.
- **debug (Step 4):** Final implementation including the screenshot capture and monitoring system.

---

## 🤝 Credits

Original educational material and tutorial structure provided by [Factoria F5 Madrid](https://github.com/Factoria-F5-madrid/webscraper).
Completed and debugged as a learning project by Mirae Kang.

