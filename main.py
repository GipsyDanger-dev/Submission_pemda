from utils.extract import scrape_main
from utils.transform import transform_data
from utils.load import load_to_csv

def main():
    print("Memulai ETL Pipeline...")
    
    # 1. Extract
    raw_df = scrape_main()
    print(f"Total data mentah: {len(raw_df)}")
    
    if not raw_df.empty:
        # 2. Transform
        print("Sedang membersihkan data...")
        clean_df = transform_data(raw_df)
        print(f"Total data bersih: {len(clean_df)}")
        
        # 3. Load
        if not clean_df.empty:
            load_to_csv(clean_df)
            print("ETL Berhasil! File products.csv siap dikirim.")
        else:
            print("Gagal: Data kosong setelah transformasi. Periksa kembali filter di transform.py")
    else:
        print("Gagal: Tidak ada data yang berhasil diekstrak.")

if __name__ == "__main__":
    main()