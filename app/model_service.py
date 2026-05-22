from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib


# =========================
# 1) Training Data
# =========================

messages = [
    "Congratulations! You won a free prize",
    "Win money now",
    "Click here to claim your reward",
    "Free offer just for you",
    "You have won a lottery",
    "Claim your free gift now",
    "Urgent! Your account has a problem",
    "Get cash now",
    "Limited time offer",
    "You won a free iPhone",
    "Hello, how are you?",
    "Can we meet tomorrow?",
    "Please call me when you arrive",
    "Don't forget the meeting",
    "I will send you the file",
    "Are you coming today?",
    "Let's study together",
    "Good morning",
    "Please check your email",
    "See you later",
]

labels = [
    "spam",
    "spam",
    "spam",
    "spam",
    "spam",
    "spam",
    "spam",
    "spam",
    "spam",
    "spam",
    "ham",
    "ham",
    "ham",
    "ham",
    "ham",
    "ham",
    "ham",
    "ham",
    "ham",
    "ham",
]


# =========================
# 2) Create Model Pipeline
# =========================

model = Pipeline(
    [
        ("vectorizer", CountVectorizer()),
        ("classifier", MultinomialNB()),
    ]
)


# =========================
# 3) Train Model
# =========================

model.fit(messages, labels)


# =========================
# 4) Save Model
# =========================

joblib.dump(model, "spam_ham_model.pkl")


def predict_text(text: str):
    """Predict if the text is spam or ham."""

    prediction = model.predict([text])[0]
    probabilities = model.predict_proba([text])[0]
    confidence = float(probabilities.max())

    return {
        "input": text,
        "prediction": str(prediction),
        "confidence": round(confidence, 2),
    }
