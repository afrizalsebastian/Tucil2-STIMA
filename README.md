# Tucil2-STIMA

## Deskripsi Singkat Program
Folder terdiri dari
```
├── docs
├── src
|   ├── libraryScipy.ipynb
|   ├── main.ipynb
|   └── myConvexHull.py
└── README.md
```
### myConvexHull
```
calculateDeterminant(point1, point2,point3) => Untuk Mengetahui titik berada di kiri atau kanan garis
find2InitialPoint(listPoint) =>encari 2 titik awal sebagai pembagi awal 2 titik tersebut diambil berdasarkan nilai x terkecil dan nilai x terbesar
calculateDistance(point1, point2, point3) => Menghitung jarak titik ke garis
findMaxDistance(point1, point2, listPoint) => Mencari titik dengan jarak terjauh dari garis
divideSide(point1, point2, listPoint) => Membagi Menjadi 2 sisi
solveLeftSide(point1, point2, leftListPoint, countPointInLeft) => Menyelesaikan sisi kiri dari 2 titik awal
solveRightSide(point1, point2, rightListPoint, countPointInRight) => menyelesaikan sisi kanan dari 2 titik awal
myConvexHull(listAllPoint) => Mengembalikan points yang menjadi point untuk convexHull
connectThePoint(hullPoint) => menyambungkan dari satu titik ke titik lain
```

## Requirement
1. [Python 3](https://www.python.org/downloads/)
2. [Jupyter NoteBook](https://jupyter.org/install)
3. matplotlib
4. pandas
5. numpy

## Menjalankan Program
1. Buka Folder pada Jupyter Notebook dan buka file main.ipynb
2. Klik Run pada Menu Bar ![image](https://user-images.githubusercontent.com/82313717/155914610-bb380000-9671-465c-bc6f-9f6dc9d3a8eb.png) untuk setiap cell mulai dari cell teratas.


## Author

[Afrizal Sebastian--13520120](https://github.com/afrizalsebastian)
