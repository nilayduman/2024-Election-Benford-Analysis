import pandas as pd
import numpy as np
import math
from scipy.stats import chisquare
import matplotlib.pyplot as plt
import multiprocessing

# CSV dosyasından veri okuma
def load_data(file_path, column_name):
    try:
        data = pd.read_csv(file_path)
        return data[column_name].tolist()
    except Exception as e:
        print(f"Veri yüklenirken bir hata oluştu: {e}")
        return []

# Benford'un teorik dağılımı
def benford_distribution():
    return [math.log10(1 + 1/d) for d in range(1, 10)]

# Verinin ilk rakamını almak
def first_digit(n):
    return int(str(n)[0])

# Veriyi analiz etme
def analyze_data(data):
    first_digits = [first_digit(num) for num in data if num > 0]
    digit_counts = [first_digits.count(i) for i in range(1, 10)]  # Bu kısmı kontrol edelim
    digit_frequencies = [count / len(first_digits) for count in digit_counts]
    return digit_frequencies


# Chi-square testi
def chi_square_test(observed, expected):
    stat, p_value = chisquare(observed, expected)
    return stat, p_value

# Grafik oluşturmak için
def plot_results(theoretical, actual, title="Benford Dağılımı Karşılaştırması"):
    x = np.arange(1, 10)
    
    # Eğer actual verisi beklenenden fazla ise, sadece ilk 9 veriyi al
    if len(actual) > 9:
        actual = actual[:9]
    
    plt.bar(x - 0.2, theoretical, width=0.4, label="Teorik Dağılım")
    plt.bar(x + 0.2, actual, width=0.4, label="Gerçek Dağılım")
    plt.xlabel('İlk Rakam')
    plt.ylabel('Frekans')
    plt.title(title)
    plt.legend()
    plt.show()


# Veriyi temizleme ve filtreleme
def clean_data(data):
    # Veriyi pozitif sayılarla sınırlama
    return [x for x in data if isinstance(x, (int, float)) and x > 0]

# Paralel analiz fonksiyonu
def parallel_analysis(data):
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)

    # Her bir parça için analiz işlemi başlat
    results = pool.map(analyze_data, np.array_split(data, num_processes))
    
    pool.close()
    pool.join()

    # Sonuçları birleştirme ve işleme
    all_results = [item for sublist in results for item in sublist]
    return all_results

# CSV dosyasındaki veriyi analiz etme
def analyze_benford_from_file(file_path, column_name):
    data = load_data(file_path, column_name)

    if not data:
        return

    # Veriyi temizleme
    cleaned_data = clean_data(data)

    if len(cleaned_data) == 0:
        print("Geçerli veri bulunamadı.")
        return

    # Paralel analiz
    actual = parallel_analysis(cleaned_data)

    # Teorik Benford dağılımı
    theoretical = benford_distribution()

    # Sonuçları görselleştir
    plot_results(theoretical, actual)

    # Chi-square testi
    stat, p_value = chi_square_test(actual, theoretical)
    print(f"Chi-square testi: Stat={stat}, p-değeri={p_value}")

# Çoklu dosya analizi yapma
def analyze_multiple_sources(file_paths, column_name):
    for file_path in file_paths:
        print(f"Veri analizi başlatılıyor: {file_path}")
        analyze_benford_from_file(file_path, column_name)

# Ana fonksiyon
if __name__ == "__main__":
    trump_file_path = 'trump_data.csv'  # Trump verisi
    kamala_file_path = 'kamala_data.csv'  # Kamala verisi
    column_name = 'Total_Votes'  # Analiz edilecek sütun

    print("Trump verisi analizi:")
    analyze_benford_from_file(trump_file_path, column_name)

    print("\nKamala Harris verisi analizi:")
    analyze_benford_from_file(kamala_file_path, column_name)

