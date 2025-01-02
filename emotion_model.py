from transformers import pipeline

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

def analyze_emotion(text):
    result = classifier(text)[0]
    label = result['label'].lower()
    confidence = result['score']

    if "negative" in label:
        return "sad", confidence
    elif "positive" in label:
        return "happy", confidence
    else:
        return "neutral", confidence
