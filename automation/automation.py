import re

# open potential-contacts.txt file
# [] Find all phone numbers
# [] store them in phone_numbers.txt
# [] find all emails
# [] store them in emails.text

def clean_numbers(number_string):
  cleaned_number = number_string.replace('(', '')
  cleaned_number = number_string.replace(')', "-")
  cleaned_number = number_string.replace(".", "-")
  
  if len(cleaned_number) == 8:
    cleaned_number = "206-" + cleaned_number 

  return cleaned_number

def validate_phone():

  cleaned = []
  phone_pattern = re.compile(r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}")

  with open("assets/potential-contacts.txt") as numbers:
    lines = numbers.read()
  # print(lines)

  match_numbers = re.findall(phone_pattern, lines)
  # print(match_numbers)

  for x in match_numbers:
    cleaned.append(clean_numbers(x))

  print(cleaned)
  cleaned.sort()

  report = "\n".join(cleaned)

  with open("automation/phone_numbers.txt", "w+") as phone_list:
    phone_list.write(report)

validate_phone()


def validate_email():

  email_pattern = re.compile(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+")

  with open("assets/potential-contacts.txt") as emails:
    lines = emails.read()

  match_emails = re.findall(email_pattern, lines)

  match_emails.sort()
  # print(match_emails)

  email_report = "\n".join(match_emails)

  with open("automation/emails.txt", "w+") as email_string:
    email_string.write(email_report)

validate_email()

  