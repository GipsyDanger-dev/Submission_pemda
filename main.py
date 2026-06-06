from utils.extract import scrape_main
from utils.transform import transform_data
from utils.load import load_to_csv

def main():
    print("Memulai ETL Pipeline...")
    
    # 1. Extract
    raw_df = scrape_main()
    
    if not raw_df.empty:
        # 2. Transform
        print("Sedang membersihkan data...")
        clean_df = transform_data(raw_df)
        
        # --- CEK DISINI ---
        print("\n--- VERIFIKASI TIPE DATA SEBELUM SIMPAN ---")
        print(clean_df.info()) 
        print("-------------------------------------------\n")
        
        # 3. Load
        if not clean_df.empty:
            load_to_csv(clean_df)
            print("ETL Berhasil!")
    else:
        print("Gagal: Data kosong.")

if __name__ == "__main__":
    main()