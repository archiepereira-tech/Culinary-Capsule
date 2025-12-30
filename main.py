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

    html_recipe_card = """
    <!--
    * This email was built using Tabular.
    * For more information, visit https://tabular.email
    -->
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">
    <head>
    <title></title>
    <meta charset="UTF-8" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <!--[if !mso]>-->
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <!--<![endif]-->
    <meta name="x-apple-disable-message-reformatting" content="" />
    <meta content="target-densitydpi=device-dpi" name="viewport" />
    <meta content="true" name="HandheldFriendly" />
    <meta content="width=device-width" name="viewport" />
    <meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no" />
    <style type="text/css">
    table {
    border-collapse: separate;
    table-layout: fixed;
    mso-table-lspace: 0pt;
    mso-table-rspace: 0pt
    }
    table td {
    border-collapse: collapse
    }
    .ExternalClass {
    width: 100%
    }
    .ExternalClass,
    .ExternalClass p,
    .ExternalClass span,
    .ExternalClass font,
    .ExternalClass td,
    .ExternalClass div {
    line-height: 100%
    }
    body, a, li, p, h1, h2, h3 {
    -ms-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%;
    }
    html {
    -webkit-text-size-adjust: none !important
    }
    body {
    min-width: 100%;
    Margin: 0px;
    padding: 0px;
    }
    body, #innerTable {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale
    }
    #innerTable img+div {
    display: none;
    display: none !important
    }
    img {
    Margin: 0;
    padding: 0;
    -ms-interpolation-mode: bicubic
    }
    h1, h2, h3, p, a {
    overflow-wrap: normal;
    white-space: normal;
    word-break: break-word
    }
    a {
    text-decoration: none
    }
    h1, h2, h3, p {
    min-width: 100%!important;
    width: 100%!important;
    max-width: 100%!important;
    display: inline-block!important;
    border: 0;
    padding: 0;
    margin: 0
    }
    a[x-apple-data-detectors] {
    color: inherit !important;
    text-decoration: none !important;
    font-size: inherit !important;
    font-family: inherit !important;
    font-weight: inherit !important;
    line-height: inherit !important
    }
    u + #body a {
    color: inherit;
    text-decoration: none;
    font-size: inherit;
    font-family: inherit;
    font-weight: inherit;
    line-height: inherit;
    }
    a[href^="mailto"],
    a[href^="tel"],
    a[href^="sms"] {
    color: inherit;
    text-decoration: none
    }
    </style>
    <style type="text/css">
    @media (min-width: 481px) {
    .hd { display: none!important }
    }
    </style>
    <style type="text/css">
    @media (max-width: 480px) {
    .hm { display: none!important }
    }
    </style>
    <style type="text/css">
    @media (max-width: 480px) {
    .t31{text-align:left!important}.t30{vertical-align:top!important;width:800px!important}
    }
    </style>
    <!--[if !mso]>-->
    <link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;700;800&amp;display=swap" rel="stylesheet" type="text/css" />
    <!--<![endif]-->
    <!--[if mso]>
    <xml>
    <o:OfficeDocumentSettings>
    <o:AllowPNG/>
    <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
    </xml>
    <![endif]-->
    </head>
    <body id="body" class="t41" style="min-width:100%;Margin:0px;padding:0px;background-color:#ffffff;"><div class="t40" style="background-color:#ffffff;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td class="t39" style="font-size:0;line-height:0;mso-line-height-rule:exactly;background-color:#ffffff;" valign="top" align="center">
    <!--[if mso]>
    <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false">
    <v:fill color="#ffffff"/>
    </v:background>
    <![endif]-->
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center" id="innerTable"><tr><td align="center">
    <table class="t38" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr><td width="620" class="t37" style="width:620px;">
    <table class="t36" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t35" style="background-color:#FFFFFF;padding:40px 40px 40px 40px;"><div class="t34" style="width:100%;text-align:left;"><div class="t33" style="display:inline-block;"><table class="t32" role="presentation" cellpadding="0" cellspacing="0" align="left" valign="top">
    <tr class="t31"><td></td><td class="t30" width="540" valign="top">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t29" style="width:100%;"><tr><td class="t28"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100% !important;"><tr><td align="center">
    <table class="t27" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr><td width="540" class="t26" style="width:600px;">
    <table class="t25" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t24" style="overflow:hidden;background-color:#EADDCA;border-radius:20px 20px 20px 20px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100% !important;"><tr><td><div class="t2" style="mso-line-height-rule:exactly;mso-line-height-alt:15px;line-height:15px;font-size:1px;display:block;">&nbsp;&nbsp;</div></td></tr><tr><td align="left">
    <table class="t6" role="presentation" cellpadding="0" cellspacing="0" style="Margin-right:auto;"><tr><td width="540" class="t5" style="width:800px;">
    <table class="t4" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t3" style="padding:0 15px 0 15px;"><h1 class="t1" style="margin:0;Margin:0;font-family:Inter Tight,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:34px;font-weight:800;font-style:normal;font-size:24px;text-decoration:none;text-transform:none;direction:ltr;color:#222222;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px;">Recipe Title<span class="t0" style="margin:0;Margin:0;font-weight:700;mso-line-height-rule:exactly;"></span></h1></td></tr></table>
    </td></tr></table>
    </td></tr><tr><td><div class="t7" style="mso-line-height-rule:exactly;mso-line-height-alt:10px;line-height:10px;font-size:1px;display:block;">&nbsp;&nbsp;</div></td></tr><tr><td align="left">
    <table class="t12" role="presentation" cellpadding="0" cellspacing="0" style="Margin-right:auto;"><tr><td width="540" class="t11" style="width:800px;">
    <table class="t10" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t9" style="padding:0 15px 0 15px;"><p class="t8" style="margin:0;Margin:0;font-family:Inter Tight,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:28px;font-weight:500;font-style:normal;font-size:18px;text-decoration:none;text-transform:none;direction:ltr;color:#777777;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px;">Instructions</p></td></tr></table>
    </td></tr></table>
    </td></tr><tr><td><div class="t13" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;&nbsp;</div></td></tr><tr><td><div class="t19" style="mso-line-height-rule:exactly;mso-line-height-alt:91px;line-height:91px;font-size:1px;display:block;">&nbsp;&nbsp;</div></td></tr><tr><td align="center">
    <table class="t23" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr><td width="540" class="t22" style="width:620px;">
    <table class="t21" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t20" style="overflow:hidden;background-color:#CFC0A9;padding:5px 25px 5px 25px;border-radius:20px 20px 20px 20px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100% !important;"><tr><td align="center">
    <table class="t18" role="presentation" cellpadding="0" cellspacing="0" style="Margin-left:auto;Margin-right:auto;"><tr><td width="490" class="t17" style="width:600px;">
    <table class="t16" role="presentation" cellpadding="0" cellspacing="0" width="100%" style="width:100%;"><tr><td class="t15"><h1 class="t14" style="margin:0;Margin:0;font-family:Inter Tight,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:34px;font-weight:700;font-style:normal;font-size:20px;text-decoration:none;text-transform:none;direction:ltr;color:#333333;text-align:center;mso-line-height-rule:exactly;mso-text-raise:4px;">Sent using Culinary Capsule</h1></td></tr></table>
    </td></tr></table>
    </td></tr></table></td></tr></table>
    </td></tr></table>
    </td></tr></table></td></tr></table>
    </td></tr></table>
    </td></tr></table></td></tr></table>
    </td>
    <td></td></tr>
    </table></div></div></td></tr></table>
    </td></tr></table>
    </td></tr></table></td></tr></table></div><div class="gmail-fix" style="display: none; white-space: nowrap; font: 15px courier; line-height: 0;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</div></body>
    </html>"""

    try:
        smtp.login(gmail, password)
    
        for email in emails_to_send:

            try:
                message = EmailMessage()
                if email["body"] == None:
                    message.set_content(f"Sorry, no recipe was found. This may have been an accident!\n\n\n\n\n\n\n\nSent using Culinary Capsule")
                else:
                    message.set_content(f"Here's your recipe:\n\n{email['body']}\n\n\n\n\n\n\n\nSent using Culinary Capsule")
                    message.add_alternative(html_recipe_card, subtype='html')
                
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
