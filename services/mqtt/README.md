# Description

This script connects to a message broker called HiveMQ and sends two messages to a topic called "Sensores". It waits for confirmation that the messages were received successfully, and if there is a problem, it will try again. Once the messages are confirmed, the script disconnects from the broker.
