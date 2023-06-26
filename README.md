# F55121006_FelisyaBrigitaTaniaWong_UASPAA2

1. Analisis Sorting Algorithm:
    a.	Worst Case:
        •	Bubble Sort: Pada worst case, Bubble Sort memiliki kompleksitas waktu O(n^2). Hal ini terjadi ketika elemen-elemen dalam array terurut secara terbalik, sehingga setiap elemen perlu dipindahkan ke posisi yang tepat dengan melakukan perbandingan dan pertukaran pada setiap pasangan elemen.
        •	Insertion Sort: Pada worst case, Insertion Sort memiliki kompleksitas waktu O(n^2). Hal ini terjadi ketika elemen-elemen dalam array terurut secara terbalik, sehingga setiap elemen perlu dipindahkan ke posisi yang tepat dengan melakukan perbandingan dan penempatan pada posisi yang benar.
    b.	Best Case:
        •	Bubble Sort: Pada best case, Bubble Sort memiliki kompleksitas waktu O(n). Hal ini terjadi ketika elemen-elemen dalam array sudah terurut secara ascending, sehingga tidak ada pertukaran yang perlu dilakukan selama iterasi.
        •	Insertion Sort: Pada best case, Insertion Sort memiliki kompleksitas waktu O(n). Hal ini terjadi ketika elemen-elemen dalam array sudah terurut secara ascending, sehingga tidak ada perbandingan dan pergeseran yang perlu dilakukan selama iterasi.
    c.	Average Case:
        •	Bubble Sort: Pada average case, Bubble Sort memiliki kompleksitas waktu O(n^2). Ini terjadi ketika elemen-elemen dalam array tidak memiliki pola tertentu dan membutuhkan pertukaran untuk memperoleh urutan yang benar.
        •	Insertion Sort: Pada average case, Insertion Sort memiliki kompleksitas waktu O(n^2). Ini terjadi ketika elemen-elemen dalam array tidak memiliki pola tertentu dan perbandingan serta penempatan diperlukan untuk memperoleh urutan yang benar.
    
2. Analisis Shortest Path Calculation
    a.	Worst Case:
        •	TSP (Travelling Salesman Problem): Algoritma ini menggunakan pendekatan brute force dengan menggunakan rekursi dan backtracking untuk mengeksplorasi semua kemungkinan rute. Jadi, pada kasus terburuk, kompleksitas waktu TSP adalah O(n!), di mana n adalah jumlah kota. Ini terjadi ketika semua kemungkinan rute harus diperiksa sebelum menemukan rute terpendek.
        •	Dijkstra: Pada kasus terburuk, algoritma Dijkstra memiliki kompleksitas waktu O((V + E) log V), di mana V adalah jumlah simpul (kota) dan E adalah jumlah tepi (jarak antara kota). Hal ini terjadi ketika ada banyak jalur yang harus diperiksa untuk mencapai tujuan akhir.
    b.	Best Case:
        •	TSP (Travelling Salesman Problem): Tidak ada best case khusus dalam algoritma TSP karena setiap rute harus dieksplorasi.
        •	Dijkstra: Pada kasus terbaik, ketika simpul awal adalah simpul tujuan itu sendiri, maka kompleksitas waktu Dijkstra adalah O(1) karena tidak ada jalur yang perlu diperiksa.
    c.	Average Case:
        •	TSP (Travelling Salesman Problem): Tidak ada rata-rata kasus khusus yang didefinisikan secara umum dalam algoritma TSP karena kompleksitasnya sangat tergantung pada jumlah kota dan setiap rute harus dieksplorasi.
        •	Dijkstra: Pada kasus rata-rata, kompleksitas waktu Dijkstra adalah O((V + E) log V), di mana V adalah jumlah simpul (kota) dan E adalah jumlah tepi (jarak antara kota). Ini terjadi ketika ada beberapa jalur yang harus diperiksa untuk mencapai tujuan akhir.
