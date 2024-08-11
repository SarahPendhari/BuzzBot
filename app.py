import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import pandas as pd
import io

st.title("KitchenWiz")

# Initialize chat history if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Initialize quiz state if not already present
if "quiz_state" not in st.session_state:
    st.session_state.quiz_state = {
        "question_index": 0,
        "score": [],
        "in_progress": False
    }

# Function to get data response
def get_data_response(question):
    prompt = f"Provide information on the following topic for 'The Chef Story': {question}"
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=st.secrets["GOOGLE_API_KEY"])
    response = llm.invoke(prompt)
    if response and hasattr(response, 'content'):
        return response.content
    else:
        return "Sorry, I couldn't generate data for that topic."

# Function to handle the quiz game
def handle_quiz():
    quiz_questions = [
        {"question": "What is the name of our restaurant?", "answer": "The Chef Story"},
        {"question": "What is today's special?", "answer": "Grilled Salmon"},
        {"question": "Do we offer vegan options?", "answer": "Yes"},
        # Add more questions as needed
    ]
   
    quiz_length = len(quiz_questions)
    quiz_state = st.session_state.quiz_state
   
    if quiz_state["in_progress"]:
        if quiz_state["question_index"] < quiz_length:
            question = quiz_questions[quiz_state["question_index"]]
            st.subheader(f"Question {quiz_state['question_index'] + 1}: {question['question']}")
            user_answer = st.text_input("Your Answer:", key=f"quiz_input_{quiz_state['question_index']}")
            if st.button("Submit Answer", key=f"submit_{quiz_state['question_index']}"):
                if user_answer.lower() == question["answer"].lower():
                    st.success("Correct!")
                    quiz_state['score'][quiz_state["question_index"]] = 1
                    # elif quiz_state["question_index"] >= quiz_length & st.button("Get Score"):
                    #     handle_quiz()
                else:
                    st.error("Incorrect!")
            if st.button("Next"):
                quiz_state["question_index"] += 1  # Move to the next question when the answer is submitted
                st.rerun()          
        else:
            st.subheader(f"Quiz Completed! Your Score: {sum(quiz_state['score'])} out of {quiz_length}")
            if st.button("Restart Quiz"):
                restart_quiz(quiz_length)
                st.rerun()
    else:
        if st.button("Start Quiz"):
            start_quiz(quiz_length)
            st.rerun()


def start_quiz(quiz_length):
    st.session_state.quiz_state["in_progress"] = True
    st.session_state.quiz_state["question_index"] = 0
    st.session_state.quiz_state["score"] = [0] * quiz_length

def restart_quiz(quiz_length):
    # st.session_state.quiz_state["in_progress"] = False
    st.session_state.quiz_state["question_index"] = 0
    st.session_state.quiz_state["score"] = [0] * quiz_length

# Function to display menu with prices and offers
def display_menu():
    menu_items = [
        {"item": "Grilled Salmon", "price": "$20", "offer": "10% off"},
        {"item": "Vegan Burger", "price": "$15", "offer": "No discount"},
        {"item": "Caesar Salad", "price": "$12", "offer": "5% off"},
        {"item": "Chicken Alfredo", "price": "$18", "offer": "15% off"},
        {"item": "Margherita Pizza", "price": "$14", "offer": "No discount"},
        {"item": "Beef Tacos", "price": "$16", "offer": "20% off"},
        {"item": "Sushi Platter", "price": "$25", "offer": "10% off"},
        {"item": "Pasta Carbonara", "price": "$17", "offer": "No discount"},
        {"item": "BBQ Ribs", "price": "$22", "offer": "10% off"},
        {"item": "Lobster Bisque", "price": "$19", "offer": "5% off"},
        {"item": "Falafel Wrap", "price": "$13", "offer": "No discount"},
        {"item": "Steak Frites", "price": "$27", "offer": "15% off"},
        {"item": "Pad Thai", "price": "$16", "offer": "10% off"},
        {"item": "Chicken Wings", "price": "$14", "offer": "5% off"},
        {"item": "Fish and Chips", "price": "$18", "offer": "No discount"},
        {"item": "Vegetable Stir-fry", "price": "$15", "offer": "10% off"},
        {"item": "Shrimp Scampi", "price": "$21", "offer": "15% off"},
        {"item": "Eggplant Parmesan", "price": "$17", "offer": "No discount"},
        {"item": "Buffalo Chicken Pizza", "price": "$20", "offer": "10% off"},
        {"item": "Quinoa Salad", "price": "$12", "offer": "5% off"},
        {"item": "Turkey Sandwich", "price": "$13", "offer": "No discount"},
        {"item": "Clam Chowder", "price": "$14", "offer": "10% off"},
        {"item": "Beef Stroganoff", "price": "$23", "offer": "15% off"},
        {"item": "Mushroom Risotto", "price": "$18", "offer": "No discount"},
        {"item": "Pork Chops", "price": "$22", "offer": "5% off"},
        {"item": "Greek Salad", "price": "$11", "offer": "No discount"},
        {"item": "Fried Calamari", "price": "$16", "offer": "10% off"},
        {"item": "Spaghetti Bolognese", "price": "$15", "offer": "10% off"},
        {"item": "Chicken Quesadilla", "price": "$14", "offer": "5% off"},
        {"item": "Veggie Pizza", "price": "$17", "offer": "No discount"},
        {"item": "Seafood Paella", "price": "$26", "offer": "15% off"},
        {"item": "Bacon Cheeseburger", "price": "$19", "offer": "10% off"},
        {"item": "Tuna Salad", "price": "$13", "offer": "No discount"},
        {"item": "Lamb Shank", "price": "$24", "offer": "5% off"},
        {"item": "Chicken Tikka Masala", "price": "$18", "offer": "10% off"},
        {"item": "Vegetable Samosa", "price": "$9", "offer": "No discount"},
        {"item": "Stuffed Peppers", "price": "$15", "offer": "10% off"},
        {"item": "Teriyaki Chicken", "price": "$17", "offer": "5% off"},
        {"item": "Pulled Pork Sandwich", "price": "$14", "offer": "No discount"},
        {"item": "Mango Avocado Salad", "price": "$12", "offer": "10% off"},
        {"item": "Ratatouille", "price": "$16", "offer": "15% off"},
        {"item": "Salmon Sushi Roll", "price": "$13", "offer": "No discount"},
        {"item": "Chicken Parmigiana", "price": "$20", "offer": "10% off"},
        {"item": "Beef Burrito", "price": "$15", "offer": "5% off"},
        {"item": "Vegetable Lasagna", "price": "$18", "offer": "10% off"},
        {"item": "Chicken Caesar Wrap", "price": "$13", "offer": "No discount"},
        {"item": "Gnocchi with Pesto", "price": "$19", "offer": "5% off"},
        {"item": "BBQ Chicken Pizza", "price": "$20", "offer": "10% off"},
        {"item": "Fish Tacos", "price": "$16", "offer": "No discount"},
        {"item": "Prawn Cocktail", "price": "$14", "offer": "10% off"},
        {"item": "Miso Soup", "price": "$10", "offer": "5% off"},
        {"item": "Vegetable Tempura", "price": "$13", "offer": "No discount"},
        {"item": "Baked Ziti", "price": "$17", "offer": "10% off"},
        {"item": "Chicken Enchiladas", "price": "$15", "offer": "15% off"}
    ]

    # Create a DataFrame from the menu items
    df = pd.DataFrame(menu_items)

    # Number of items per page
    items_per_page = 10

    # Number of pages
    total_pages = len(df) // items_per_page + (1 if len(df) % items_per_page > 0 else 0)

    # Select the current page
    page = st.selectbox("Select Page", range(1, total_pages + 1))

    # Calculate the start and end indices for the current page
    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page

    # Display the menu items for the current page
    st.dataframe(df.iloc[start_idx:end_idx])


# Add tabs for the different functionalities
tab1, tab2, tab3 = st.tabs(["Chat", "Menu", "Quiz"])

with tab1:
    # Create a form for new input
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_area("Enter Your Query:", key="input")
        submitted = st.form_submit_button("Ask Meow")

        if submitted and user_input:
            response = get_data_response(user_input)
            st.session_state.chat_history.append({"user": user_input, "meow": response})

    # Optionally, allow clearing chat history
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []

    # Display predefined questions in the sidebar
    predefined_questions = [
        "What is on the menu?",
        "Can you show me the menu?",
        "What are the prices of your dishes?",
        "What is today's special?",
        "Are there any vegan/vegetarian options available?",
        "What are the prices of your combo meals?",
        "Can I see your dessert menu?",
        "What are your best-selling dishes?",
        "Do you offer kids' meals?",
        "Can I customize my order?",
        "What drinks do you offer?",
        "Do you have a happy hour menu?",
        "Are there any special weekend offers?",
        "Do you offer family meal packages?",
        "Do you have any low-calorie options?",
        "Can I get a tour of your facility?",
        "Are there any upcoming food festivals?",
        "Do you host cooking classes?",
        "Can I get a schedule of all your events for the month?",
        "Do you have a loyalty program for frequent visitors?",
        "Can I book a table for an event online?",
        "Are there any themed nights?",
        "What is the duration of the Folk Lore show?",
        "Are the shows kid-friendly?",
        "Can I participate in the shows or events?",
        "Do you have a kid's play area?",
        "Can I pre-order meals for a specific time?",
        "Do you offer any discounts for large group bookings?",
        "Is your restaurant wheelchair accessible?",
        "Do you accept digital payments like Apple Pay or Google Pay?",
        "How can I reset my password on your website?",
        "Can I track my delivery order online?",
        "Do you offer online gift cards?",
        "How do I change my delivery address on your website?",
        "Can I cancel my order online?",
        "How can I delete my account?",
        "Do you have an online chat support?",
        "How can I contact you through social media?",
        "Can I see customer reviews on your website?",
        "How do I update my profile information on your website?"
    ]

    st.sidebar.header("Mostly Asked Questions")
    for question in predefined_questions:
        if st.sidebar.button(question):
            user_input = question
            response = get_data_response(user_input)
            st.session_state.chat_history.append({"user": user_input, "meow": response})

    # Display the chat history at the bottom in descending order
    if st.session_state.chat_history:
        #st.header("Chat History")
        for chat in reversed(st.session_state.chat_history):
            st.info(f"You: {chat['user']}")
            st.success(f"Meow: {chat['meow']}")

with tab2:
    display_menu()

with tab3:
    handle_quiz()