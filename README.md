# Mello: Mental Health Conversation Chatbot

## Overview

Mello is a mental health conversation chatbot designed to provide supportive responses based on user input. It uses a Support Vector Machine (SVM) model to classify user messages into predefined categories and respond with appropriate, empathetic messages.

## Functionality

- **Text Classification**: Mello classifies user input into different categories or tags (e.g., `happy`, `sad`, `casual`, `about`).
- **Response Generation**: Based on the predicted tag, Mello selects and returns a relevant response from a predefined set of responses for each tag.
- **Interactive**: The chatbot interacts with users, providing responses and asking follow-up questions to better understand their feelings.

## Models Used

### **Support Vector Classification (SVC)**

- **Description**: An SVM-based classifier that uses a linear kernel to separate text data into different categories.
- **Purpose**: Classify user messages into predefined tags based on their content.
- **Implementation**: 
  - **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency) is used to convert text data into numerical feature vectors.
  - **Training**: The model is trained on these vectors with their corresponding tags.

## Steps Incorporated

1. **Data Preparation**:
   - **Load Data**: Read intent data from a JSON file containing patterns, tags, and responses.
   - **Preprocess Text**: Convert text to lowercase and strip whitespace for consistency.
   - **Extract Patterns and Tags**: Create lists of text patterns and their associated tags. Store responses in a dictionary for each tag.

2. **Text Vectorization**:
   - **TF-IDF Vectorizer**: Convert text patterns into numerical feature vectors suitable for machine learning algorithms.

3. **Model Training**:
   - **Train SVM**: Fit the SVM classifier on the feature vectors and tags.

4. **Prediction and Response**:
   - **Predict Tag**: Classify new user inputs to predict the appropriate tag.
   - **Generate Response**: Select a response from the predefined responses based on the predicted tag.

5. **User Interaction**:
   - **Interactive Loop**: Continuously prompt the user for input, predict the tag, and provide a response until the user decides to quit.

## Drawbacks

- **Limited Handling of Unmapped Data**: The model may not perform well on inputs that do not fit the predefined tags or are significantly different from the training data.
- **Data Dependency**: The quality of responses depends heavily on the diversity and representativeness of the training data.
- **Lack of Contextual Understanding**: The model may struggle with understanding complex user inputs or maintaining context over long conversations.



## Usage

To use Mello:

1. **Run the Script**: Execute the main script to start the chatbot.
2. **Interact with Mello**: Type your messages and observe Mello’s responses.
3. **Quit**: Type `quit` to end the conversation.

## Example

```python
Enter String : i am feeling happy
User Input: i am feeling happy
Predicted Tag: happy
Response: That's great to hear. I'm glad you're feeling this way.

Enter String : i am feeling sad
User Input: i am feeling sad
Predicted Tag: sad
Response: I'm here for you. Could you tell me why you're feeling this way?
