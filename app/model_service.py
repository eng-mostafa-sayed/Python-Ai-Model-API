from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib


# =========================
# 1) Load Dataset
# =========================

iris = load_iris()

X = iris.data
y = iris.target

# Names of flowers
flower_names = iris.target_names


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

model = LogisticRegression(max_iter=200)


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
print(classification_report(y_test, y_pred, target_names=flower_names))


# =========================
# 6) Save Model
# =========================

joblib.dump(model, "iris_logistic_model.pkl")

print("Iris model saved successfully!")


def predict_iris(features: list[float]):
    """Predict the Iris flower type from the features sent to the API."""

    if len(features) != 4:
        return {
            "error": "Please send exactly 4 numbers: sepal_length, sepal_width, petal_length, petal_width"
        }

    input_data = [features]

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    confidence = float(probabilities.max())

    return {
        "input": features,
        "prediction": str(flower_names[prediction]),
        "class_id": int(prediction),
        "confidence": round(confidence, 2),
    }
