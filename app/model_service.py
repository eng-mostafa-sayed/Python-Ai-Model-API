from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


# Sample training data.
# Later, you can replace these examples with your real dataset.
messages = [
    "Win cash prize now",
    "Free money offer",
    "Hello, how are you?",
    "Can we meet tomorrow?",
    "Congratulations you won",
    "Please send me the file",
]

labels = ["spam", "spam", "ham", "ham", "spam", "ham"]


# Build the model pipeline.
# CountVectorizer converts text into numbers.
# MultinomialNB classifies the text as spam or ham.
model = Pipeline(
    [
        ("vectorizer", CountVectorizer()),
        ("classifier", MultinomialNB()),
    ]
)


# Train the model once when the API starts.
# Your original code used "texts", but the correct variable here is "messages".
model.fit(messages, labels)


def predict_text(text: str):
    """Return a spam or ham prediction for the provided text."""

    # Later, you can load a saved trained model here instead of training above.
    # Example:
    # import joblib
    # model = joblib.load("models/spam_classifier.joblib")
    #
    # You can also add text preprocessing here.
    # Example:
    # text = text.lower().strip()

    prediction = model.predict([text])[0]

    # Get the highest prediction probability as the confidence score.
    probabilities = model.predict_proba([text])[0]
    confidence = float(probabilities.max())

    return {
        "input": text,
        "prediction": prediction,
        "confidence": round(confidence, 2),
    }
