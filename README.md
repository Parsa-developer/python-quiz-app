# 🎯 Python Quiz Application

A command-line quiz game with timed questions loaded from a JSON file. Test your knowledge under time pressure!

![Quiz Demo](/assets/main.PNG)

## 🌟 Features

- ⏱️ **Timed Questions**: Individual time limits for each question
- 📝 **Multiple Choice**: Answer with A/B/C/D options
- 📊 **Score Tracking**: See final percentage score
- 🎨 **Color Feedback**: Immediate colored responses (Green=Correct/Red=Wrong)
- 📁 **JSON Question Bank**: Easy to modify/add new questions
- ❌ **Input Validation**: Handles invalid inputs gracefully
- ⏰ **Auto-Advance**: Progresses after time limit expires

## 🛠️ Requirements

- Python 3.8+
- `colorama` library

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/Parsa-developer/python-quiz-app.git
cd python-quiz-app
```
2. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🚀 Usage
1. **Add questions to questions.json (see format below)**

2. **Run the quiz:**
```bash
python quiz.py
```

## Example Output:
```
=== PYTHON QUIZ ===
Total questions: 2

Question 1/2
What is Python?
A. A snake species
B. Programming language
C. Movie title
D. Type of coffee

You have 30 seconds. Enter answer (A/B/C/D): B
Correct! ✅
```

## 📝 Question Format (questions.json)

```json
[
    {
        "question": "What is Python?",
        "options": [
            "A snake species",
            "Programming language",
            "Movie title",
            "Type of coffee"
        ],
        "answer": "B",
        "time_limit": 30
    }
]
```

## 🤝 Contributing

1. Fork the repository

2. Create feature branch (git checkout -b feature/new-questions)

3. Commit changes (git commit -m 'Add new questions')

4. Push to branch (git push origin feature/new-questions)

5. Open Pull Request

Happy Quizzing! 🧠⚡