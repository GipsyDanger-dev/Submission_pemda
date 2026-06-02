import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

def scrape_main():
    base_url = "https://fashion-studio.dicoding.dev"
    all_products = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    print("--- Memulai Proses Scraping ---")

    try:
        for page in range(1, 51):
            # Pola URL: index.html untuk hal 1, page2.html atau page-2.html untuk selanjutnya
            if page == 1:
                url = f"{base_url}/index.html"
            else:
                url = f"{base_url}/page{page}.html" # Coba pola tanpa strip dulu
            
            response = requests.get(url, headers=headers, timeout=15)
            
            # Jika pola page2.html gagal (404), coba pola page-2.html
            if response.status_code == 404:
                url = f"{base_url}/page-{page}.html"
                response = requests.get(url, headers=headers, timeout=15)

            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.text, 'html.parser')
            
            # MENCARI PRODUK: Mencari semua elemen yang membungkus info produk
            # Biasanya Dicoding menggunakan class 'card-body' atau 'product-item'
            items = soup.find_all(['div', 'section'], class_=lambda x: x and ('card' in x or 'product' in x))
            
            # Jika tidak ketemu class, cari berdasarkan keberadaan teks '$' (Price)
            if not items:
                items = [p.find_parent('div') for p in soup.find_all(string=lambda t: '$' in t)]

            for item in items:
                if not item: continue
                
                # Ambil judul: cari tag heading (h1-h6) atau class title
                title_tag = item.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'b'])
                title = title_tag.get_text(strip=True) if title_tag else "Unknown Product"
                
                # Ambil semua paragraf atau span untuk detail
                details = [d.get_text(strip=True) for d in item.find_all(['p', 'span', 'li'])]
                
                # Validasi minimal ada judul dan harga
                if title != "Unknown Product" and len(details) >= 1:
                    all_products.append({
                        'Title': title,
                        'Price': next((d for d in details if '$' in d), None),
                        'Rating': next((d for d in details if '/' in d or 'Rating' in d), None),
                        'Colors': next((d for d in details if 'Color' in d), "0"),
                        'Size': next((d for d in details if 'Size' in d), "N/A"),
                        'Gender': next((d for d in details if 'Gender' in d), "Unisex"),
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
            
            if page % 10 == 0:
                print(f"Halaman {page} selesai. Total sementara: {len(all_products)}")
            
            time.sleep(0.05)
            
        return pd.DataFrame(all_products).drop_duplicates()

    except Exception as e:
        print(f"Error Extract: {e}")
        return pd.DataFrame()