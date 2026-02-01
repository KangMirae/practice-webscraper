### 3. `cronjob` 브랜치 (Automation)

```markdown
# Step 3: Scheduling with Cronjob

This stage focuses on automation. I configured a **Cronjob** inside the Linux container to run the scraper every 5 minutes automatically.

## 📝 Learning Points
- Setting up a `cronfile` with the schedule `*/5 * * * *`.
- Installing and starting the `cron` service within the Docker container.
- Note: This implementation follows the tutorial's original `cronfile` structure without additional environment path configurations.

## 🚀 Key Command
```bash
# Check if the cron service is running inside the container
docker exec -it webscraper-server-1 service cron status

# Verify the registered crontab
docker exec -it webscraper-server-1 crontab -l