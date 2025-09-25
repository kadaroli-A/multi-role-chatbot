---

#### 2. `chatbot.py`  
Main Python file.  

```python
# Multi-role Chatbot

def chatbot(role, message):
    if role == "student":
        return f"📘 Student mode: I can help you with learning. You asked: {message}"
    elif role == "teacher":
        return f"👨‍🏫 Teacher mode: Let me explain. You asked: {message}"
    elif role == "support":
        return f"💡 Support mode: I will try to solve your issue. You asked: {message}"
    else:
        return "🤖 Unknown role. Please choose: student, teacher, or support."

# Example usage
if __name__ == "__main__":
    while True:
        role = input("Enter role (student/teacher/support): ").strip().lower()
        msg = input("Enter your message: ")
        reply = chatbot(role, msg)
        print(reply)