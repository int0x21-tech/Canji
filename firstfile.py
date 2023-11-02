# Import necessary libraries
import webbrowser

# Define the questions and their correct answers
questions = {
    "Have you completed your workout for the day?": "Yes",
    "Awesome, how do you feel about yourself": "Great",
    "Are you ready to take some Cybersecurity training today?": "Yes"
}

# Define the SharePoint video site link
sharepoint_link = "https://learn.acloud.guru/?_ga=2.231790551.975485264.1698964049-485692977.1698964045"
# Create a function to ask questions and check answers
def ask_questions():
    # Loop through each question in the dictionary
    for question in questions:
        # Print the question and get user's input
        answer = input(question + " ")

        # Check if the answer is correct
        if answer.lower() == questions[question].lower():
            print("Correct!")
        else:
            print("Wrong answer, please try again.")
            # Call the function again to ask the same question
            ask_questions()

    # If all answers are correct, open the SharePoint video site
    webbrowser.open(sharepoint_link)

# Call the ask_questions function to start the quiz
ask_questions()