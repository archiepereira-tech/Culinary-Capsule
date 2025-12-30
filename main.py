import os
import smtplib
from datetime import date
from email.message import EmailMessage
from supabase import create_client

# Supabase
url = "https://bfndmbdcfaaxshazecwh.supabase.co"
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

# Gmail
gmail = "cookbook.culinarycapsule@gmail.com"
password = os.environ.get("GMAIL_PASSWORD")

# Deliver emails
def deliver():
    current_date = date.today().isoformat()

    responses = supabase.table("recipes").select("*").eq("tosend_date", current_date).eq("is_sent", False).execute()
    emails_to_send = responses.data
    
    if not emails_to_send:
        return
    
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    try:
        smtp.login(gmail, password)
    
        for email in emails_to_send:

            try:
                message = EmailMessage()
                if email["body"] == None:
                    message.set_content(f"Sorry, no recipe was found. This may have been an accident!\n\n\n\n\n\n\n\nSent using Culinary Capsule")
                else:
                    message.set_content(f"Here's your recipe:\n\n{email['body']}\n\n\n\n\n\n\n\nSent using Culinary Capsule")
                
                if email["sender_name"] == None:
                    message["Subject"] = f"New Recipe from a Cookbook: {email['title']}"
                    message["From"] = f"Cookbook Capsule <{gmail}>"
                else:
                    message["Subject"] = f"New Recipe from {email['sender_name']}'s Cookbook: {email['title']}"
                    message["From"] = f"{email['sender_name']}'s Cookbook <{gmail}>"
                message["To"] = email["sendto_email"]
                smtp.send_message(message)
                supabase.table("recipes").update({"is_sent": True}).eq("id", email['id']).execute()

            except Exception as e:
                fail_message = EmailMessage()
                fail_message["Subject"] = f"Sorry, your recipe didn't send!"
                fail_message["To"] = email["sender_email"]
                fail_message["From"] = f"Culinary Capsule <{gmail}>"
                if email["sender_name"] == None:
                    fail_message.set_content(f"""Hi,\n\nUnfortunately there was an error sending your recipe and it could not be delivered. Please try again, but make sure that the recipient's email address is still active and correct!\n\nSorry for the error,\nCulinary Capsule\n\n\nRecipe Details:\nName of Recipe: {email['title']}\nInstructions: {email['body']}\nTo: {email['sender_name']} (Email: {email['sendto_email']})\n\nTechnical Error Details:\n{e}""")
                else:
                    fail_message.set_content(f"""Hi {email["sender_name"]},\n\nUnfortunately there was an error sending your recipe and it could not be delivered. Please try again, but make sure that the recipient's email address is still active and correct!\n\nSorry for the error,\nCulinary Capsule\n\n\nRecipe Details:\nName of Recipe: {email['title']}\nInstructions: {email['body']}\nTo: {email['sender_name']} (Email: {email['sendto_email']})\n\nTechnical Error Details:\n{e}""")
                smtp.send_message(fail_message)

    except Exception as e:
        raise e
    
    finally:
        smtp.quit()


if __name__ == "__main__":
    deliver()