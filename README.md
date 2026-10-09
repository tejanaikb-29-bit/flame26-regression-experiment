# ScoreSense — FLAME'26 Regression Experiment

A small, interactive **Multiple Linear Regression** demo that estimates an exam score from study hours, attendance, previous exam score, and sleep duration. It is designed as a learning experiment and uses **synthetic practice data**, not real student records.

## Project files

- `app.py` — Flask app; loads the CSV and trains a scikit-learn Linear Regression model.
- `data/student_performance.csv` — 180 generated practice rows.
- `templates/index.html` — responsive prediction interface.
- `static/style.css` — visual design and responsive styling.
- `requirements.txt` — Python dependencies.
- `Procfile` and `render.yaml` — deployment configuration for Render.
- `experiment.ipynb` — experiment notebook for data exploration, model training, metrics and plot.

## Run locally (Windows)

1. Install Python 3.10+.
2. Extract the ZIP and open a terminal in the `FLAME26_Regression_Experiment` folder.
3. Create a virtual environment:
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the website:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000` in your browser.

## Run the notebook

```bash
pip install jupyter matplotlib
jupyter notebook experiment.ipynb
```

Run the notebook cells from top to bottom. It explores the CSV, splits the data, trains Linear Regression, reports MAE/RMSE/R², and plots actual versus predicted values.

## Publish to GitHub

1. Create a new **public** GitHub repository named `flame26-regression-experiment`.
2. Upload the contents of this folder (not the ZIP itself), keeping the folder structure.
3. Commit the files to the `main` branch.
4. Copy the repository URL. That is your **GitHub link**.

## Deploy on Render

1. Sign in to Render and choose **New + → Web Service**.
2. Connect your GitHub account and select `flame26-regression-experiment`.
3. Render should detect `render.yaml`. If asked, set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
4. Choose a free instance if available and click **Create Web Service**.
5. Wait for deployment to finish. Open the `https://...onrender.com` URL and test a prediction. That URL is your **Render link**.

## What to submit

- **Render link:** the live deployed website URL from your Render dashboard.
- **GitHub link:** the public repository URL.

You must create/publish these links yourself; this ZIP does not claim to have deployed the project or created a repository.

## Experiment summary

**Aim:** Build and demonstrate a regression model that predicts a continuous numerical outcome.

**Algorithm:** Multiple Linear Regression.

**Input features:** study hours/day, attendance %, previous exam score, sleep hours/day.

**Target:** final exam score (0–100).

**Libraries:** pandas, scikit-learn, Flask, matplotlib (notebook only).

**Important limitation:** The data is synthetic and the model is for demonstrating the workflow only. Predictions should not be used for real academic decisions.
