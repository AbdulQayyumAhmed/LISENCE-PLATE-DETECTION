# 🚗 VisionX: AI License Plate Detector

VisionX is a premium, high-performance license plate detection dashboard powered by **YOLOv8**. It features a modern, glassmorphic UI designed for a seamless, single-screen experience.

![Dashboard Preview](https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png)

## ✨ Key Features

- **🚀 Real-time Detection**: Lightning-fast license plate localization using YOLOv8.
- **💎 Glassmorphism UI**: A premium, modern dashboard with interactive hover effects and smooth transitions.
- **📱 Single-Screen Layout**: Optimized for 1080p+ screens to ensure no scrolling is required.
- **🖼️ Fixed Visualization**: Consistent 300px image containers for both input and detection results.
- **🌩️ Cloud Ready**: Optimized for deployment on Streamlit Cloud with automatic dependency handling.

## 🛠️ Technology Stack

- **Core Architecture**: [YOLOv8](https://github.com/ultralytics/ultralytics) (Ultralytics)
- **Frontend Framework**: [Streamlit](https://streamlit.io/)
- **Image Processing**: [OpenCV](https://opencv.org/) & [Pillow](https://python-pillow.org/)
- **Model Format**: PyTorch (`.pt`)

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/lisence-plate-detection.git
   cd lisence-plate-detection
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## 📦 Deployment

This app is optimized for **Streamlit Cloud**. 

- The `packages.txt` file handles system-level graphics libraries (`libgl1`).
- The `requirements.txt` is configured for headless server environments.

To deploy:
1. Push your code to a GitHub repository.
2. Connect your GitHub account to [Streamlit Cloud](https://share.streamlit.io/).
3. Select `app.py` as the main file and click **Deploy**.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---
Built with ❤️ by VisionX AI Team
