### 2. `docker` 브랜치 (Containerization)

```markdown
# Step 2: Dockerizing the Scraper

In this step, I moved the local development environment into a **Docker container**. This ensures the scraper runs consistently regardless of the host OS.

## 📝 Learning Points
- Writing a `Dockerfile` to install system dependencies (Firefox, GeckoDriver).
- Configuring **Selenium Options** for a headless environment (`--headless`, `--no-sandbox`).
- Using `docker-compose` to build and manage the containerized service.

## 🚀 Key Command
```bash
docker compose up --build -d
docker exec -it webscraper-server-1 python manage.py scraper
```