# 🖼️ Image Compression using K-Means Clustering

Compress images by reducing the number of colors using **K-Means clustering** in Python.

This project demonstrates color quantization: each pixel is reassigned to the nearest cluster centroid, producing a smaller color palette while preserving visual structure.

---

## ✨ What this project does

- Loads an input image
- Applies K-Means clustering on RGB pixel values
- Reconstructs the image with only **K** representative colors
- Saves/displays a compressed output image
- Helps visualize the trade-off between image quality and compression

---

## 🧠 Concept

An RGB image can be viewed as a set of 3D points (`R, G, B`).

K-Means:
1. Chooses `K` centroids in color space
2. Assigns each pixel to the nearest centroid
3. Updates centroids until convergence
4. Replaces original pixel colors with centroid colors

This reduces unique colors from potentially millions to just **K**.

---

## 📁 Repository

- **Repo:** `willow788/Image-Compression-using-K-means-clustering`
- **Language:** Python (100%)

---

## ⚙️ Setup

### 1) Clone

```bash
git clone https://github.com/willow788/Image-Compression-using-K-means-clustering.git
cd Image-Compression-using-K-means-clustering
```

### 2) Create virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it:

- **Windows (PowerShell)**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- **Windows (CMD)**
  ```cmd
  .venv\Scripts\activate.bat
  ```
- **macOS/Linux**
  ```bash
  source .venv/bin/activate
  ```

### 3) Install dependencies

```bash
pip install numpy matplotlib scikit-learn pillow opencv-python
```

> If your script uses only some of these libraries, you can trim this list accordingly.

---

## ▶️ Run

From the project root:

```bash
python <your_script_name>.py
```

If arguments are supported in your script, use a pattern like:

```bash
python <your_script_name>.py --input input.jpg --k 16 --output output.jpg
```

---

## 📊 Choosing K (number of colors)

- **Small K** (e.g., 4, 8): stronger compression, more visible color banding
- **Medium K** (e.g., 16, 32): balanced quality/compression
- **Large K** (e.g., 64+): better quality, less compression

Try multiple values and compare outputs side by side.

---

## 🧪 Suggested experiments

- Compare outputs for `K = 4, 8, 16, 32, 64`
- Test on natural photos vs flat illustrations/logos
- Measure:
  - output file size
  - number of unique colors
  - visual quality (optional: PSNR/SSIM)

---

## 🛠️ Possible improvements

- Add CLI support with `argparse`
- Add automatic plotting of original vs compressed images
- Export a metrics table (size reduction, runtime)
- Batch compress all images in a folder
- Add notebook version for step-by-step learning

---

## 🤝 Contributing

Contributions are welcome.  
Feel free to fork the repo, open an issue, and submit a pull request.

---

## 📄 License

MIT © willow788

---

## 👤 Author

**[willow788](https://github.com/willow788)**