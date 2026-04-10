from flask import request, Flask , jsonify , send_from_directory
from datetime import datetime
app=Flask(__name__)

def get_response(user_input):
    user_input=user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return"Bot: Hey there!"
        
    elif "good morning" in user_input:
        return"Bot: Good morning sir/mam! "

    elif "good evening" in user_input:
        return"Bot: Good evening sir/mam! "

    elif "thank you" in user_input or "thanks" in user_input:
        return"Bot: You're welcome!"

    elif "who created you" in user_input:
        return"Bot: I was created by a Python developer"

    elif "how are you" in user_input:
        return"Bot: I'm just code, but I'm doing great"

    elif "bye" in user_input:
        return"Bot: Goodbye!"
        

    elif "help" in user_input:
        return"Bot: Yes Ofcourse!, Try to ask something."
        
    elif "book room" in user_input:
        return"Bot: Okay! What is your preferred time.<br> Day or Night"
            
    elif "day" in user_input:
        return"Bot: Available rooms:<br> single->5 <br> double->3 <br> triple->4"

    elif "night" in user_input:
        return"Bot: Available rooms:<br> single->9 <br> double->1 <br> triple->5"

    elif "tomorrow" in user_input:
        return"Bot: Available rooms:<br> single->5 <br> double->4 <br> triple->2"
        
    elif "price" in user_input:
        return"Bot: for Single: 2K rupees per day <br>For Double: 2.5k rupees per day <br>For Triple: 3k rupees per day."

    elif "available rooms" in user_input:
        return"Bot: We have Single, Double, and Triple rooms available."

    elif "facilities" in user_input:
        return"Bot: We offer WiFi, AC, TV, Room Service, and Parking for two wheeler and four wheeler"

    elif "wifi" in user_input:
        return"Bot: Yes, free WiFi is available "

    elif "parking" in user_input:
        return"Bot: Yes, parking is available "

    elif "check in" in user_input:
        return"Bot: Check-in time is 12 PM."

    elif "check out" in user_input:
        return"Bot: Check-out time is 11 AM."

    elif "location" in user_input:
        return"Bot: We are located near noida city center "
    
    elif "single" in user_input or "double" in user_input or "triple" in user_input:
        return"Bot: okay sir! your booking is confirmed."

    elif "contact" in user_input:
        return"Bot: You can call us at +91-98765xxxxx "

    elif "cancel booking" in user_input:
        return"Bot: Please provide your booking ID to cancel."

    elif "modify booking" in user_input:
        return"Bot: Sure! Tell me what changes you want."

    elif "confirm booking" in user_input:
        return"Bot: Your booking has been confirmed "

    elif "payment" in user_input:
        return"Bot: We accept Cash, UPI, and Cards "

    elif "upi" in user_input:
        return"Bot: UPI is accepted. ID: hotel@upi"

    elif "refund" in user_input:
        return"Bot: Refund will be processed within 5-7 days."

    elif "food" in user_input:
        return"Bot: We have an in-house restaurant "

    elif "menu" in user_input:
        return"Bot: We offer Indian, Chinese, and Continental cuisine."

    elif "breakfast" in user_input:
        return"Bot: yes, breakfast is included "

    elif "room service" in user_input:
        return"Bot: Room service is available 24/7 "

    elif "weather" in user_input:
        return"Bot: Please check your weather app for latest updates "

    elif "time" in user_input:
        return f"Bot: {datetime.now().strftime('%H:%M:%S')}"

    elif "date" in user_input:
        return f"Bot: {datetime.now().strftime('%d-%m-%Y')}"

    elif "owner" in user_input:
        return"Bot: The hotel is privately owned."

    elif "security" in user_input:
        return"Bot: We have 24/7 CCTV and security staff "
        
    else:
        return"Bot: Sorry, I didn't understand that"

       
@app.route("/")
def home():
    return send_from_directory('.','test.html')

@app.route("/chat", methods=["POST"])

def chat():
    data=request.json
    user_message=data.get("message")
    response = get_response(user_message)
    return jsonify({"response":response})

if __name__=="__main__":
    print("Chatbot is runnin! please visit http://127.0.0.1:5000 in your browser")
    print ("Serving test.html file")
    app.run(debug=True)
