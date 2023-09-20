#chatbot v1.2
#ChangeLog - Made the code more modular, readable and maintainable
# Welcome message
print("     !!     Welcome to Customer Service Chatbot     !!")
print("Hi there! What type of cuisine are you in the mood for today?\n")

# Dictionary of questions and responses
qna = {
    "i want pizza": {
        "response": "Today we have a special #deal# for you.\n\nYou can get two large pizzas for the price of one. Would you like to take advantage of that offer?",
        "options": {
            "1": "Pizza Margherita",
            "2": "Quick Tomato Pizzas",
            "3": "Four Cheese Pizza",
            "4": "Cheesy Vegetable Pizza",
            "5": "Tandoori Paneer Pizza",
            "6": "Thin Crust Hawaiian Pizza",
            "7": "Uttapam Pizza",
            "8": "Chocolate Pizza",
            "9": "Onion Pizza",
            "10": "Veggie pizza"
        },
        "followup": "Which type of Pizza are you in the mood for today?\nPlease type the menu number",
    },
    "1 and 7": "Pizza Margherita and Uttapam Pizza, Wonderful choice! Can I have your delivery address, please?",
    "mfp, india": "Thank you! Your order will be delivered to Mfp, India. May I have your phone number for any delivery updates?",
    "123456": "Thank you! Your order for one Pizza Margherita and one Uttapam Pizza will be delivered to Mfp, India.\nYour total is Rupee 350. Will you be paying with cash or UPI?",
    "upi": "Great! I'll send UPI ID for payment. UPI: xxxx2154@xx\nIf payment will done please type 'ok'.",
    "ok": "Thank you for payment. Your order is confirmed, and you should receive it in about 30-40 minutes. Is there anything else I can assist you with?",
    "that's all, thank you": "You're welcome! Enjoy your meal, and if you have any other questions in the future, feel free to reach out.\n!! Have a great day !!\nPlease type 'exit'",
}

# Main chat loop
while True:
    cust = input("You: ").lower()  # Convert input to lowercase for case-insensitive matching

    # Check for exit command
    if cust == "exit":
        break
    else:
        # Respond to customer input using the predefined responses from the dictionary
        if cust in qna:
            response_data = qna[cust]

            if isinstance(response_data, str):
                print("\nBot:", response_data)
            else:
                print("\nBot:", response_data["response"])

                if "options" in response_data:
                    for key, value in response_data["options"].items():
                        print(f"{key}. {value}")

                    followup_input = input(response_data["followup"] + "\nYou: ").strip()
                    if followup_input in response_data["options"]:
                        print("\nBot:", response_data["options"][followup_input])
                    else:
                        print("\nBot: Invalid choice. Please select a valid option.")
                else:
                    print("\nBot: Invalid response configuration. Please contact customer support.")

        else:
            print("\nBot: I'm sorry, I don't understand. Please try a different query.")
