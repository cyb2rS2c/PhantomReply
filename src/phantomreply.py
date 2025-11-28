import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from validation import is_valid_email
from termcolor import colored
import sys
from animation import print_ascii_art

class BOT:
    def __init__(self, sender, app_password, server='smtp.gmail.com'):
        self.sender = sender
        self.app_password = app_password
        self.server = server

    def send_email(self, receiver, subject, content, text_subtype='html'):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = receiver
        msg.attach(MIMEText(content, text_subtype))

        try:
            conn = smtplib.SMTP(self.server, 587)
            conn.ehlo()
            conn.starttls()
            conn.login(self.sender, self.app_password)
            conn.sendmail(self.sender, receiver, msg.as_string())
            conn.quit()
            print(colored(f"Email sent successfully to {colored(receiver, 'green')}", 'grey'))
        except Exception as e:
            print(colored(f"Failed to send email to {receiver}: {e}", 'red'))

class FETCHER:
    def __init__(self, config_file='assets/config.json'):
        self.config_file = config_file
    
    def get_config(self):
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return config
        except Exception as e:
            print(colored(f"Error loading configuration file: {e}", 'red'))
            return None
    
    def extract_details(self):
        config = self.get_config()
        if not config:
            return {}

        senders = config.get('senders', [])        
        receivers = config.get('groups', {})      
        message = config.get('message', {})

        return {
            'senders': senders,
            'receivers': receivers,
            'subject': message.get('subject', ''),
            'content': message.get('content', ''),
            'load_file': message.get('load_file', None),
            'text_type': message.get('text_type', 'plain'),
            'server': config.get('server', 'smtp.gmail.com'),
            'app_password': config.get('app_password', None)
        }

def load_html_template(filepath):
    """Load the HTML template."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(colored(f"Error reading HTML file {filepath}: {e}", 'red'))
        return None

def load_file(filepath):
    """Load the content from a specified file."""
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(colored(f"Error reading file {filepath}: {e}", 'red'))
            return None
    else:
        print(colored(f"File {filepath} not found.", 'red'))
        return None

def write_msg():
    """Function to allow manual entry of content."""
    print("Enter your message (press Enter for new lines, type 'DONE' on a new line to finish):")
    message = []
    while True:
        try:
            line = input()
            if line.strip().lower() == 'done':
                break
            message.append(line)
        except EOFError:
            break
    return '\n'.join(message)
def generate_html_email(template_html, subject, content, button_url):
    """Generate the final HTML email by replacing placeholders with actual content."""
    if not template_html:
        print("Error: HTML template not found.")
        return None

    paragraphs = content.split('\n\n')
    formatted_content = ''.join([f'<p>{p}</p>' for p in paragraphs])

    html_email = template_html.replace("{{subject}}", subject)
    html_email = html_email.replace("{{content}}", formatted_content)
    html_email = html_email.replace("{{button_url}}", button_url)

    return html_email

def main():
    try:
        print_ascii_art()
        config_file = 'assets/config.json'
        fetcher = FETCHER(config_file)
        details = fetcher.extract_details()

        if not details:
            print(colored("Error: Could not extract details from configuration.", 'red'))
            return

        sender_email = details['senders'][0]
        app_password = details['app_password']
        
        if not is_valid_email(sender_email):
            print(f"Invalid sender email: {sender_email}")
            return
        
        print(colored("How would you like to provide the content?", 'cyan', attrs=['bold']))
        print(colored("1. Manually", 'yellow'))
        print(colored("2. Load from config.json", 'yellow'))
        print(colored("3. Load from a file", 'yellow'))
        choice = input(colored("Enter 1, 2, or 3: ", 'green')).strip()
        

        if choice == '1':
            content_text = write_msg()
        elif choice == '2':
            content_text = details['content']
            if not content_text:
                print(colored("No content found in config.json, please enter manually.", 'yellow'))
                content_text = write_msg()
        elif choice == '3':
            filepath =  details['load_file']  or input("Enter the file path to load the content from: ").strip()
            content_text = load_file(filepath)
            if not content_text:
                print("No content found or file not found, please try again.")
                return
        else:
            print(colored("Invalid choice. Exiting.", 'red'))
            return

        html_template = load_html_template('templates/email_template.html')

        button_url = input("Enter any URL to attach or leave it empty e.g. https://github.com: ").strip() or 'https://github.com'
        
        html_email = generate_html_email(html_template, details['subject'], content_text, button_url)
        
        if html_email is None:
            print("Error generating HTML email.")
            return

        bot = BOT(sender_email, app_password, details['server'])
        group1_receivers = details['receivers'].get('group1', [])

        if not group1_receivers:
            print("No receivers found in group1.")
            return

        for receiver in group1_receivers:
            if receiver == '':
                print('Skipping empty email address.')
                continue
            
            if is_valid_email(receiver):
                bot.send_email(receiver, details['subject'], html_email, 'html')
            else:
                print(f"Invalid email address: {receiver}")

    except KeyboardInterrupt:
        print(colored("\nExiting gracefully... Bye!", 'blue'))
        sys.exit(0)
if __name__ == '__main__':
    main()
