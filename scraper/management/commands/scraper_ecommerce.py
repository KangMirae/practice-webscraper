# management/commands/scraper_ecommerce.py
from django.core.management.base import BaseCommand
from scraper.services.scraper_ecommerce import scraper_ecommerce_website
from scraper.models import EcommerceProduct 

class Command(BaseCommand):
    help = "webscraper.io 쇼핑몰 데이터를 긁어옵니다."

    def handle(self, *args, **kwargs):
        self.stdout.write("스크래핑 시작...")
        
        data = scraper_ecommerce_website()
        
        for item in data:
            EcommerceProduct.objects.create(
                title=item["title"],
                price=item["price"],
                description=item["description"],
                url=item["url"]
            )
            
        self.stdout.write(self.style.SUCCESS(f"{len(data)}개의 상품 정보를 저장했습니다!"))