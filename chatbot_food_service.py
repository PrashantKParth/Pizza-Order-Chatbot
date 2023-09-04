#chat Bot


print("     !!     Welcome to Customer Service Chatbot     !!")
print("Hi there! What type of cuisine are you in the mood for today?\n")

qna1 = {
    "i want pizza":"Today we have a special #deal# for you.\n\n    You can get two large pizzas for the price of one. Would you like to take advantage of that offer?\n\n     1.Pizza Margherita\n     2.Quick Tomato Pizzas\n     3.Four Cheese Pizza\n     4.Cheesy Vegetable Pizza\n     5.Tandoori Paneer Pizza\n     6.Thin Crust Hawaiian Pizza\n     7.Uttapam Pizza\n     8.Chocolate Pizza\n     9.Onion Pizza\n     10.veggie pizza\n\n    Which type of Pizza are you in the mood for today?\n               Please type the menu number\n",
    "1 and 7":"Pizza Margherita and Uttapam Pizza, Wonderful choice! Can I have your delivery address, please?",
    "mfp, india":"Thank you! Your order will be delivered to Mfp, India. May I have your phone number for any delivery updates?",
    "123456":"Thank you! Your order for one Pizza Margherita and one Uttapam Pizza will be delivered to Mfp, India.\n                        Your total is Rupee 350. Will you be paying with cash or UPI?",
    "upi":"Great! I'll send UPI ID for payment.UPI:xxxx2154@xx \n              If payment will done please type 'ok' .",
    "ok":"Thank you for payment. Your order is confirmed, and you should receive it in about 30-40 minutes. Is there anything else I can assist you with?",
    "that's all, thank you":"You're welcome! Enjoy your meal, and if you have any other questions in the future, feel free to reach out. \n             !!  Have a great day  !! \n                Please type 'exit'"
    }


while True:

        cust=input("You:- ")

        if(cust == "exit"):
                break
        else:
                print("\nBot:- ",qna1[cust])
