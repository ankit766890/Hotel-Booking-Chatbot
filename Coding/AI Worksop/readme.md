🏨 Hotel Booking Chatbot (Flask)
A lightweight, interactive web-based chatbot designed for hotel room inquiries and bookings. This project uses a Python (Flask) backend to handle logic and an HTML/CSS/JS frontend for a smooth user experience.

🚀 Features
Real-time Interaction: Chat with the bot via a clean, fixed chat window.

Room Inquiries: Get availability and pricing for Single, Double, and Triple rooms.

Automated Bookings: Quick confirmation based on room type selection.

Information Hub: Instant details on hotel facilities (WiFi, Parking), location, and contact info.

Utility Tools: Check current date and time directly through the bot.

Responsive UI: A navigation-based landing page with a smooth-scroll layout.

🛠️ Tech Stack
Backend: Python 3.12, Flask

Frontend: HTML5, CSS3, JavaScript (Fetch API)

Logic: Conditional Pattern Matching

📂 Project Structure
Plaintext
hotel-chatbot/
│
├── app.py              # Flask server and Chatbot logic
├── test.html           # Frontend landing page and Chat UI
└── README.md           # Project documentation
🔧 Installation & Setup
1. Prerequisites
Ensure you have Python installed. You will also need to install Flask:

Bash
pip install flask
2. Clone/Save the Files
Place app.py and test.html in the same directory.

3. Run the Application
Navigate to your project folder and run:

Bash
python app.py
4. Access the Bot
Open your browser and visit:
http://127.0.0.1:5000

💬 Example Queries
You can try typing the following into the chat:

"I want to book a room"

"What is the price for a single room?"

"Do you have wifi?"

"What is the current time?"

"Where are you located?"

📝 Important Notes
Formatting: The backend uses <br> tags to ensure room availability lists are displayed correctly in the HTML chat body.

JavaScript: The frontend uses async/await to handle asynchronous requests to the Flask /chat endpoint.

Logic: The bot uses a case-insensitive matching system to understand user intent.

👨‍💻 Developed By
Python Developer Customizable Hotel Bot Framework