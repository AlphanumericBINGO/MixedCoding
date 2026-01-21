from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Your dataset
messages = [
    {"text": "Congratulations! You've won a free vacation to the Bahamas!", "label": "spam"},
    {"text": "URGENT: Your account has been selected for a £500 reward. Claim now.", "label": "spam"},
    {"text": "You've been chosen for a free iPhone 15. Click to confirm.", "label": "spam"},
    {"text": "Win £1000 cash instantly! Reply YES to enter.", "label": "spam"},
    {"text": "Your number was drawn in our weekly prize pool. Claim today.", "label": "spam"},
    {"text": "Limited offer: Get a free smartwatch with this link.", "label": "spam"},
    {"text": "Act now! Your loan pre - approval expires in 2 hours.", "label": "spam"},
    {"text": "You've been selected for a VIP casino bonus. Tap to activate.", "label": "spam"},
    {"text": "FREE entry into our £5000 prize draw. Reply WIN.", "label": "spam"},
    {"text": "Your delivery is waiting. Pay £1 to release your package.", "label": "spam"},
    {"text": "Exclusive deal: 90% off designer sunglasses today only.", "label": "spam"},
    {"text": "You are the lucky winner of a £250 Tesco voucher!", "label": "spam"},
    {"text": "Get rich fast! Start earning £500/day from home.", "label": "spam"},
    {"text": "Your PayPal has been limited. Verify immediately.", "label": "spam"},
    {"text": "Claim your free Netflix subscription for 1 year.", "label": "spam"},
    {"text": "You've been selected for a government grant. Apply now.", "label": "spam"},
    {"text": "Final notice: Your reward is about to expire.", "label": "spam"},
    {"text": "Congratulations! Your phone number won £750.", "label": "spam"},
    {"text": "Get a free credit score check instantly. No card needed.", "label": "spam"},
    {"text": "Your bank account is compromised. Log in to secure it.", "label": "spam"},
    {"text": "FREE gift card waiting for you. Click to redeem.", "label": "spam"},
    {"text": "You've been selected for a premium dating trial.", "label": "spam"},
    {"text": "Your tax refund is ready. Confirm your details.", "label": "spam"},
    {"text": "Special offer: Buy 1 get 3 free! Limited time.", "label": "spam"},
    {"text": "You have won a luxury cruise! Confirm your spot now.", "label": "spam"},

    {"text": "Hey, are we still meeting later today?", "label": "ham"},
    {"text": "Don't forget to bring your notebook tomorrow.", "label": "ham"},
    {"text": "I'll be home in 10 minutes.", "label": "ham"},
    {"text": "Can you call me when you're free?", "label": "ham"},
    {"text": "Happy birthday! Hope you have a great day.", "label": "ham"},
    {"text": "Just finished work, heading home now.", "label": "ham"},
    {"text": "What time is the movie tonight?", "label": "ham"},
    {"text": "Let me know when you arrive safely.", "label": "ham"},
    {"text": "Lunch was great, we should go again.", "label": "ham"},
    {"text": "I'll send you the notes later today.", "label": "ham"},
    {"text": "Can you pick up some milk on your way?", "label": "ham"},
    {"text": "Meeting has been moved to 3pm.", "label": "ham"},
    {"text": "Thanks for helping me earlier!", "label": "ham"},
    {"text": "I'll text you the address in a minute.", "label": "ham"},
    {"text": "Do you want to play later tonight?", "label": "ham"},
    {"text": "Weather looks nice today.", "label": "ham"},
    {"text": "I'm stuck in traffic, running late.", "label": "ham"},
    {"text": "Let's grab coffee tomorrow morning.", "label": "ham"},
    {"text": "I'll check and get back to you.", "label": "ham"},
    {"text": "Can you send me that file again?", "label": "ham"},
    {"text": "Dinner is ready when you are.", "label": "ham"},
    {"text": "Just landed, talk soon.", "label": "ham"},
    {"text": "I'll be offline for a bit.", "label": "ham"},
    {"text": "Thanks, that really helped.", "label": "ham"},
    {"text": "See you at the gym later.", "label": "ham"}
]

# Extract texts and labels
texts = [m["text"] for m in messages]
labels = [m["label"] for m in messages]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.2, stratify=labels
)

# Vectorize text
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Evaluate
predictions = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, predictions))

# Test your own message
sample = ["You have won a free vacation!"]
sample_vec = vectorizer.transform(sample)
print("Prediction:", model.predict(sample_vec))
