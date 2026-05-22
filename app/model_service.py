from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib


# =========================
# 1) Training Data
# =========================
# Features:
# [study_hours, attendance_percentage, previous_grade]

X = [
    [1, 50, 40],
    [2, 55, 45],
    [2, 60, 50],
    [3, 65, 55],
    [4, 70, 60],
    [5, 75, 65],
    [6, 80, 70],
    [7, 85, 75],
    [8, 90, 80],
    [9, 95, 85],
    [10, 98, 90],
    [1, 40, 35],
    [2, 45, 38],
    [3, 50, 42],
    [4, 55, 48],
    [5, 60, 52],
    [6, 70, 58],
    [7, 78, 68],
    [8, 88, 78],
    [9, 92, 88],
]

# Labels:
# 0 = Fail
# 1 = Pass

y = [
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
]


# =========================
# 2) Split Data
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)


# =========================
# 3) Create Model
# =========================

model = LogisticRegression()


# =========================
# 4) Train Model
# =========================

model.fit(X_train, y_train)


# =========================
# 5) Test Model
# =========================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))


# =========================
# 6) Save Model
# =========================

joblib.dump(model, "student_pass_fail_model.pkl")

print("Student Pass/Fail model saved successfully!")


def predict_student(
    study_hours: float,
    attendance_percentage: float,
    previous_grade: float,
):
    """Predict if the student will pass or fail from API input values."""

    input_data = [[study_hours, attendance_percentage, previous_grade]]

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    confidence = float(probabilities.max())

    result = "Pass" if prediction == 1 else "Fail"

    return {
        "input": {
            "study_hours": study_hours,
            "attendance_percentage": attendance_percentage,
            "previous_grade": previous_grade,
        },
        "prediction": result,
        "class_id": int(prediction),
        "confidence": round(confidence, 2),
    }
