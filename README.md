# BuzzBot

**BuzzBot** is a versatile chatbot designed to assist users with queries related to "The Chef Story," including information about the menu, special offers, and engaging quiz games. It integrates with Google Generative AI for conversational responses and provides an interactive experience with menu browsing and quizzes.

## Features

- **Conversational AI**: Provides responses to user queries about "The Chef Story" using advanced language models.
- **Interactive Menu**: Displays a paginated menu with items, prices, and offers.
- **Quiz Game**: Engages users with a quiz about "The Chef Story" with scoring and quiz management.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/SarahPendhari/BuzzBot.git
   cd BuzzBot
   
2. **Set Up the Environment**

Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```

3. **Install Dependencies**

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

4. **Set Up API Keys**

Create a .streamlit/secrets.toml file in the project root and add your API keys:

```toml
[general]
GOOGLE_API_KEY = "your_google_api_key"
```
Replace "your_google_api_key" with your actual Google API key.

5. **Usage**
     Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

   Explore the Tabs

***Chat Tab***: Enter queries related to "The Chef Story" and receive responses. You can also view and clear chat history.
***Menu Tab***: Browse through a paginated menu with item details and current offers.
***Quiz Tab***: Start and participate in a quiz about "The Chef Story" to test your knowledge.

**Configuration**

***API Keys***: Ensure you have a valid API key for the Google Generative AI service. Add it to the secrets.toml file.
***Menu and Quiz Content***: Customize menu items and quiz questions directly in the app.py file as needed.

**Troubleshooting**

***API Key Error***: Verify that the API key in secrets.toml is correct and properly formatted.
***Dependency Issues***: Ensure all required libraries are installed. If you encounter issues, check the library documentation or update the dependencies.
***File Not Found***: Make sure the .streamlit/secrets.toml file is correctly placed in the project directory.

**Contributing**

If you want to contribute to BuzzBot:

***Fork the repository***

Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your-feature).
Create a Pull Request.

**License**

BuzzBot is licensed under the MIT License.

**Contact**

For questions or feedback:

Name: Sarah Pendhari

Email: sarahpendhari@gmail.com

GitHub: SarahPendhari
