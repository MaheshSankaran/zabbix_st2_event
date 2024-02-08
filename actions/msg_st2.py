import argparse

# Import the required modules
from st2common.runners.base_action import Action

class HelloSt2Action(Action):
    def run(self, alert_message):
        # Access the alert_message parameter passed to the action
        print("Received alert message:", alert_message)

        # Here you can perform further processing or actions based on the alert message
        # For example, you can send it to another system, log it, or analyze its content

        # Return a response indicating the action was successfully executed
        return alert_message

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Process alert message')

    # Add an argument for the alert message
    parser.add_argument('alert_message', type=str, help='Alert message to process')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Instantiate the action and run it with the provided alert message
    action = HelloSt2Action()
    action.run(args.alert_message)

if __name__ == "__main__":
    main()

