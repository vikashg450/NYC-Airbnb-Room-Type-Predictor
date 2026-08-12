# 🏙️ NYC Airbnb Room Type Predictor

> An AI-powered web application that predicts whether a New York City Airbnb listing is an **Entire home/apt**, **Private room**, or **Shared room** — visualised as the city skyline lighting up.

![Python](https://img.shields.io/badge/Python-3.12.7-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-009688?style=flat&logo=fastapi&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6.1-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=flat&logo=render&logoColor=white)

---

## 📸 Preview

| Hero & Form | After Prediction |
|---|---|
| Dark NYC skyline background, glassmorphism panels, animated teal badge | Buildings light up proportionally to confidence scores |

---

## ✨ Features

- 🔮 **Instant ML predictions** — enter listing details and get a room type prediction in real time
- 📊 **Probability breakdown** — animated bar charts showing confidence for all 3 classes
- 🏙️ **NYC skyline visualisation** — buildings light up based on prediction probability
- 🌆 **4 example listings** — pre-filled examples across Manhattan, Brooklyn, Queens & Bronx
- 📡 **Live API health indicator** — shows whether the backend is online or unreachable
- 📱 **Fully responsive** — works on mobile, tablet, and desktop
- ♿ **Accessible** — `aria-live`, `aria-label`, reduced-motion support, keyboard navigable

---

## 🧠 Machine Learning

| Detail | Info |
|---|---|
| **Dataset** | [NYC Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data) |
| **Task** | Multi-class classification |
| **Target classes** | `Entire home/apt`, `Private room`, `Shared room` |
| **Pipeline** | scikit-learn `Pipeline` (preprocessing + classifier) |
| **Model file** | `Model_Pipeline.pkl` (≈37 MB) |
| **Notebook** | `nyc_airbnb_room_type_classification.ipynb` |

### Input Features

| Feature | Type | Description |
|---|---|---|
| `latitude` | float | Listing latitude (-90 to 90) |
| `longitude` | float | Listing longitude (-180 to 180) |
| `price` | float | Price per night in USD |
| `minimum_nights` | int | Minimum nights required for booking |
| `number_of_reviews` | int | Total number of guest reviews |
| `reviews_per_month` | float | Average monthly review rate |
| `calculated_host_listings_count` | int | Total listings by this host |
| `availability_365` | int | Days available per year (0–365) |
| `neighbourhood_group` | str | NYC borough (Manhattan, Brooklyn, etc.) |
| `neighbourhood` | str | Specific neighbourhood name |

---

## 🗂️ Project Structure

```
NYC-Airbnb-Room-Type-Predictor/
│
├── main.py                                       # FastAPI backend — prediction & health endpoints
├── Model_Pipeline.pkl                            # Pre-trained scikit-learn pipeline (~37 MB)
├── requirements.txt                              # Python dependencies (pinned versions)
├── runtime.txt                                   # Python version for Render deployment
│
├── index.html                                    # Frontend — single-page app
├── style.css                                     # Styling — dark glassmorphism theme
├── script.js                                     # Frontend logic — API calls, animations
│
└── nyc_airbnb_room_type_classification.ipynb     # Training notebook (EDA + model)
```

---

## 🚀 Quick Start

### Prerequisites

- Python **3.12+**
- `pip`

### 1. Clone the repository

```bash
git clone https://github.com/vikashg450/NYC-Airbnb-Room-Type-Predictor.git
cd NYC-Airbnb-Room-Type-Predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at **http://localhost:8000**  
Interactive docs (Swagger UI) at **http://localhost:8000/docs**

### 4. Open the frontend

In a separate terminal, serve the frontend:

```bash
python -m http.server 7891
```

Then open **http://localhost:7891** in your browser.

> **Note:** If running locally, update `API_BASE_URL` in `script.js` line 5 to `http://localhost:8000`.

---

## 🌐 API Reference

### `GET /`
Health check — returns API status.

**Response:**
```json
{
  "status": "ok",
  "message": "NYC Airbnb Room Type Predictor API is running."
}
```

---

### `POST /predict`
Predict the room type for a given listing.

**Request body:**
```json
{
  "latitude": 40.7484,
  "longitude": -73.9857,
  "price": 120,
  "minimum_nights": 2,
  "number_of_reviews": 84,
  "reviews_per_month": 2.3,
  "calculated_host_listings_count": 1,
  "availability_365": 210,
  "neighbourhood_group": "Manhattan",
  "neighbourhood": "Midtown"
}
```

**Response:**
```json
{
  "Predicted_room_type": "Entire home/apt",
  "Probability": [0.87, 0.11, 0.02]
}
```

> Probability values are aligned to sklearn's alphabetical `classes_` order:  
> `[Entire home/apt, Private room, Shared room]`

---

## ☁️ Deployment (Render)

The backend is deployed at:  
🔗 **https://nyc-airbnb-room-type-predictor.onrender.com**

### Deploy your own instance

1. Push this repo to GitHub
2. Create a new **Web Service** on [Render](https://render.com)
3. Connect your GitHub repository
4. Set the following:

| Setting | Value |
|---|---|
| **Environment** | Python |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn main:app --host 0.0.0.0 --port $PORT` |
| **Python Version** | `3.12.7` (from `runtime.txt`) |

> ⚠️ **Cold starts:** Render's free tier spins down after inactivity. The first request after idle may take ~30 seconds. The API status badge in the UI will show "unreachable" until the server warms up — this is expected.

---

## 🛠️ Tech Stack

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** — high-performance Python web framework
- **[Uvicorn](https://www.uvicorn.org/)** — ASGI server
- **[scikit-learn](https://scikit-learn.org/)** — ML pipeline & prediction
- **[pandas](https://pandas.pydata.org/)** — data framing for model input
- **[Pydantic](https://docs.pydantic.dev/)** — request validation (v2 compatible)

### Frontend
- **Vanilla HTML / CSS / JavaScript** — zero dependencies, zero build step
- **[Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk)** + **Inter** + **JetBrains Mono** — Google Fonts
- CSS glassmorphism, aurora gradients, SVG NYC skyline, smooth micro-animations

---

## 📦 Dependencies

```
fastapi==0.115.6
uvicorn[standard]==0.34.0
pydantic==2.10.4
pandas==2.2.3
scikit-learn==1.6.1
joblib==1.4.2
```

---

## 📓 Training Notebook

The Jupyter notebook `nyc_airbnb_room_type_classification.ipynb` covers:

- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data cleaning & feature engineering
- 🏗️ Pipeline construction (encoding + scaling + classifier)
- 📈 Model evaluation & metrics
- 💾 Saving the trained pipeline with `joblib`

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👤 Author

Built with ❤️ using NYC Airbnb open data.  
Trained for educational and demonstration purposes — predictions are probabilistic estimates.
