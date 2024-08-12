import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import random

# Load the JSON data
data = pd.read_json('./intents.json')

# Function to preprocess text (lowercase and strip whitespace)
def preprocess_text(text):
    return text.lower().strip()

# Prepare the data
patterns = []
responses_dict = {}
tags = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        tags.append(intent['tag'])
        # Store the responses in a dictionary with the tag as the key
        if intent['tag'] not in responses_dict:
            responses_dict[intent['tag']] = intent['responses']

# Vectorize the text data
vectorizer = TfidfVectorizer(preprocessor=preprocess_text)
X = vectorizer.fit_transform(patterns)

# Train the Naive Bayes model on all the data
model = MultinomialNB()
model.fit(X, tags)

# Example usage: Predict the tag for a new input
while True:
    new_input = input("Enter String : ")
    if new_input.lower()=='quit':
        print("Bye")
        break
    new_input_vectorized = vectorizer.transform([new_input])
    predicted_tag = model.predict(new_input_vectorized)[0]

    # Find a response based on the predicted tag
    response = random.choice(responses_dict[predicted_tag])

    print(f"User Input: {new_input}")
    print(f"Predicted Tag: {predicted_tag}")
    print(f"Response: {response}")
