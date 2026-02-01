### 4. `debug` 브랜치 (Screenshots & Monitoring)

```markdown
# Step 4: Debugging with Screenshots

The final step adds a visual debugging layer. Since the browser runs in headless mode (no UI), I implemented a feature to capture and save screenshots.

## 📝 Learning Points
- Using `driver.save_screenshot()` to capture the browser state.
- Mapping **Docker Volumes** (`./screenshots:/app/screenshots`) to access images generated inside the container from the local host.
- Managing files with timestamps using Python's `datetime` module.

## 🚀 Key Result
- Screenshots are saved in the `/screenshots` folder every time the scraper runs. This is crucial for verifying that the scraper is seeing the correct page content.