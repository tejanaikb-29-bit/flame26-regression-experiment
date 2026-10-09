from pathlib import Path
import pandas as pd
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "student_performance.csv"

# Train a simple regression model from the included practice dataset.
data = pd.read_csv(DATA_PATH)
FEATURES = [
    "study_hours_per_day",
    "attendance_percent",
    "previous_exam_score",
    "sleep_hours_per_day",
]
model = LinearRegression().fit(data[FEATURES], data["final_exam_score"])

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None
    values = {
        "study_hours_per_day": "3.0",
        "attendance_percent": "85",
        "previous_exam_score": "70",
        "sleep_hours_per_day": "7.5",
    }
    if request.method == "POST":
        try:
            values = {key: request.form.get(key, "").strip() for key in FEATURES}
            row = {key: float(value) for key, value in values.items()}
            limits = {
                "study_hours_per_day": (0, 16),
                "attendance_percent": (0, 100),
                "previous_exam_score": (0, 100),
                "sleep_hours_per_day": (0, 24),
            }
            for key, (low, high) in limits.items():
                if not low <= row[key] <= high:
                    raise ValueError(f"{key.replace('_', ' ').title()} must be between {low} and {high}.")
            estimate = float(model.predict(pd.DataFrame([row], columns=FEATURES))[0])
            prediction = round(max(0, min(100, estimate)), 1)
        except (ValueError, TypeError) as exc:
            error = str(exc) or "Please enter valid numbers in all fields."
    return render_template("index.html", prediction=prediction, error=error, values=values)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= int(__import__("os").environ.get("PORT", 5000)), debug=False)
