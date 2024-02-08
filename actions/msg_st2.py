import json
import sys

def main(alert_message):
    # Your logic here to process the alert message
    print("Alert message:", alert_message)

if __name__ == "__main__":
    # Extracting the alert message from command-line arguments
    alert_message = sys.argv[1]
    main(alert_message)

