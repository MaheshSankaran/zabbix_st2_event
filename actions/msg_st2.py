import sys
from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, message, subject):
        print("Subject:", subject)
        print("Message:", message)

        # Check if subject contains "Zabbix agent"
        if "Zabbix agent" in subject:
            self.handle_zabbix_agent_subject(message)

    def handle_zabbix_agent_subject(self, message):
        # Parse the message to extract relevant details
        lines = message.split("\r\n")
        for line in lines:
            if line.startswith("Problem started at"):
                problem_started = line.split("Problem started at ")[1].strip()
                print("Problem Started At:", problem_started)
            elif line.startswith("Problem name:"):
                problem_name = line.split(":")[1].strip()
                print("Problem Name:", problem_name)
            elif line.startswith("Host:"):
                host = line.split(":")[1].strip()
                print("Host:", host)
            elif line.startswith("Severity:"):
                severity = line.split(":")[1].strip()
                print("Severity:", severity)
            # Add more conditions to extract other details as needed

