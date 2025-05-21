# Machine Learning for California Housing Price Prediction

Project ini merupakan project pengembangan Model Machine Learning untuk Memprediksi Harga Properti di Wilayah California, Amerika dengan menggunakan dataset data_california_house.csv

## Business Proble Understanding

![gambar](https://github.com/user-attachments/assets/3463589c-d2c6-464b-a412-bc8fda5c0fa3)

Say White merupakan sebuah perusahaan properti berbasis di California yang bergerak dalam layanan jual, beli, dan sewa properti residensial maupun komersial.  Say White berkomitmen untuk membantu klien mendapatkan properti terbaik dengan harga transparan, sesuai nilai pasar, dan menguntungkan kedua belah pihak.

### Problem Statement
California merupakan wilayah dengan pasar properti yang dinamis dan kompleks, dimana harga rumah di wilayah ini dipengaruhi oleh berbagai faktor.  

Sebagai perusahaan properti yang terus berkembang, Say White perlu memiliki strategi penetapan harga yang akurat dan berbasis data. Namun proses estimasi harga masih sering dilakukan secara manual yang sudah tidak relevan karena memakan waktu dan hasilnya terkadang tidak akurat. Say White membutuhkan sistem prediksi harga berbasis machine learning yang dapat menentukan harga properti secara optimal, kompetitif, dan sesuai kondisi pasar.

### Goals
Tujuan dari project ini adalah:
- Mengembangkan model machine learning yang dapat memprediksi harga properti secara akurat berdasarkan faktor-faktor yang mempengaruhi.
- Mendukung strategi bisnis Say White dalam menetapkan harga properti yang optimal, kompetitif, dan sesuai nilai pasar, guna mempercepat transaksi serta menjaga transparansi dan keuntungan bagi semua pihak.

### Stakeholder
Pihak-pihak yang berperan dan akan terdampak dalam implementasi project ini:
- Manajemen Say White: Menentukan strategi pricing dan keputusan bisnis.
- Tim Data & Analytics: Mengembangkan dan mengoptimasi model prediksi harga.
- Tim Marketing & Sales: Menggunakan model untuk menetapkan harga properti di pasar.
- Pemilik Properti (Klien): Mendapatkan harga jual yang optimal sesuai pasar.
- Calon Pembeli: Mendapatkan harga properti yang adil dan sebanding nilainya.

## Exploratory Data Analysis

### Dataset Understanding
- Dataset yang digunakan merupakan data tentang harga properti di California berdasarkan berbagai fitur yang memengaruhinya.
- Dataset terdiri dari 14448 baris data dan 10 kolom (9 kolom numerikal & 1 kolom kategorikal). Berikut informasi detail dari tiap kolom dataset:

![gambar](https://github.com/user-attachments/assets/8c8d5c35-3f2e-4f3f-badf-fc9e5dbe2e41)

### Distribusi Kolom Target
Kolom median_house_value memiliki distribusi right-skewed.

![gambar](https://github.com/user-attachments/assets/09a7970a-37bc-47d7-93d5-4ac5ce7dd126)

### Distribusi Kolom Numerik
Sebagian besar data numerik memiliki:
Diistribusi data yang tidak normal dan cenderung right-skewed.
Perlu dilakukan scaling agar model lebih stabil dan akurat.

![gambar](https://github.com/user-attachments/assets/47f5966f-ffb2-4de6-801f-48e639cf5c48)

### Analisis Lokasi terhadap Harga Properti
Berdasarkan scatterplot antara lokasi dan harga properti, dapat disimpulkan bahwa harga properti dipengaruhi oleh lokasinya. Semakin dekat dengan pesisir maka harga properti cenderung akan semakin tinggi.

![gambar](https://github.com/user-attachments/assets/cd8ce35b-1a14-44ac-bf79-275e72795f3c)

![gambar](https://github.com/user-attachments/assets/f4ab843d-1498-4b36-a457-b1fd4755feb5)

## Machine Learning Modeling
Tahapan dalam proses Machine Learning Modeling:
- Define X & y
- Data Splitting
- Data Preprocessing: ColumnTransformer
- Cross Validation
- Hyperparameter Tuning
- Predict to Test Set

### ColumnTransformer
- Encoding: OneHotEncoder pada ocean_proximity.
- Scaling: RobustScaler pada seluruh kolom numerik.

### Evaluation Metrics
Untuk mengevaluasi kinerja model regresi, beberapa metrik akan digunakan untuk memberikan gambaran tentang seberapa baik model dalam memprediksi harga rumah. Berikut adalah metrik yang akan digunakan:

1. RMSE (Root Mean Squared Error): Mengukur rata-rata kesalahan kuadrat antara prediksi dan nilai aktual. Semakin kecil nilai RMSE, semakin baik model dalam memprediksi harga rumah.
2. MAE (Mean Absolute Error): Mengukur rata-rata kesalahan absolut antara prediksi dan nilai aktual. Metrik ini memberikan gambaran langsung tentang kesalahan rata-rata yang dibuat oleh model.
3. MAPE (Mean Absolute Percentage Error): Mengukur rata-rata persentase kesalahan prediksi. Nilai MAPE yang lebih kecil menunjukkan prediksi harga rumah yang lebih akurat dalam konteks persentase.

Semakin kecil nilai RMSE, MAE, dan MAPE yang dihasilkan, berarti model semakin akurat dalam memprediksi harga sewa sesuai dengan limitasi fitur yang digunakan. 

## Conclusion
- Model terbaik: XGBoost merupakan model terbaik berdasarkan hasil cross-validation dan benchmarking, dengan nilai error (RMSE, MAE, dan MAPE) yang lebih rendah.
- Hasil metrics evaluasi:
  - RMSE	: 43.560
  - MAE	: 29.474
  - MAPE	: 0.17
  - Berdasarkan nilai MAPE dan MAE, dapat disimpulkan bahwa rata-rata prediksi model akan menyimpang sekitar 17% ($29.474) dari harga aktual, jika digunakan pada data baru.
- Visualisasi (Actual vs Predicted): Model mampu memprediksi harga rumah dengan baik pada rentang harga menengah ke bawah, namun masih kesulitan dalam memprediksi rumah harga tinggi .
- Feature Immportance: Fitur ocean_proximity_INLAND  memberikan kontribusi terbesar dalam prediksi harga rumah (56%) .


## Recommendation
- Untuk Model Machine Learning:
  - Lakukan hyperparameter tuning dengan GridSearch  untuk meningkatkan performa model secara optimal.
  - Terapkan feature selection secara iteratif  untuk memilih fitur terbaik dan menyederhanakan model.
  - Lakukan evaluasi dan retraining model secara berkala, minimal 6 bulan sekali agar tetap relevan dengan dinamika pasar properti.

- Untuk Dataset:
  - Update dataset dengan data terbaru untuk mengakomodasi inflasi dan perubahan tren pasar.
  - Penambahan Feature baru yang berpotensi mempengaruhi harga properti secara signifikan (luas tanah, luas bangunan, dll) untuk meningkatkan akurasi prediksi.

## Model Deployment
Model Machine Learning di-deploy dengan membuat sebuah aplikasi berbasis web menggunakan Streamlit yang bisa diakses melalui link berikut: https://mnaghifari-ml-californiahouse.streamlit.app/
