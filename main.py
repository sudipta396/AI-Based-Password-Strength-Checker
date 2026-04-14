import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("password_dataset_.csv")

passwords = data["password"]
labels = data["label"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(passwords)

model = LogisticRegression()
model.fit(X, labels)

def rule_score(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1
        
    return score

def check_strength(password):
    X_test = vectorizer.transform([password])
    ml_score = model.predict(X_test)[0]
    
    r_score = rule_score(password)
    
    
    final_score = ml_score + (r_score / 5)
    if final_score <= 1.5:
        strength = "Weak"

    elif final_score < 2:
        strength = "Medium"
    else:
        strength = "Strong"
    
    return strength, round(final_score, 2)


password = input("Enter Password: ")

strength, score = check_strength(password)

print("Strength:", strength)
print("Score:", score)

if strength == "Weak":
    print("Improve your password:")
    
    if len(password) < 8:
        print("- Use at least 8 characters")
    if not re.search(r"[A-Z]", password):
        print("- Add uppercase letter")
    if not re.search(r"[0-9]", password):
        print("- Add numbers")
    if not re.search(r"[!@#$%^&*]", password):
        print("- Add symbols")

elif strength == "Medium":
    print("Improve your password:")
    
    if len(password) < 8:
        print("- Use at least 8 characters")
    if not re.search(r"[A-Z]", password):
        print("- Add uppercase letter")
    if not re.search(r"[0-9]", password):
        print("- Add numbers")
    if not re.search(r"[!@#$%^&*]", password):
        print("- Add symbols")
