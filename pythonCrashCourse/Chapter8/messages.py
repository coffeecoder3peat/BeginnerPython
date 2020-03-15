def show_messages(messages):
    """Displays each messafge in  alist of messages."""
    for message in messages:
        print(message)

def send_messages(send_messages, sent_messages):
    while send_messages:
        current_message = send_messages.pop()
        print(current_message)

        sent_messages.append(current_message)

messages = ["Hey, what's up?", "Not much. You?", 'Same same.']
sent_messages = []

send_messages(messages[:], sent_messages)

print(f"\nMessages to send: {messages}")
print(f"\nSent messages: {sent_messages}")

