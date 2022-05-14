import re

# open potential-contacts.txt file
# [x] Find all phone numbers
# [x] store them in phone_numbers.txt
# [x] find all emails
# [x] store them in emails.text

def clean_numbers(number_string):
    number_string = re.sub(r"\(", '', number_string)
    number_string = re.sub(r"\)", '-', number_string)
    number_string = re.sub(r"\.", '-', number_string)

    if len(number_string) == 8:
        number_string = "206-" + number_string

    if len(number_string) == 9:
      number_string = number_string[:3] + '-' + number_string[3:6] + '-' + number_string[6:]

    return number_string


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

  # dashed_list = []
  # for x in cleaned:
  #   final_list = x[:3] + '-' + x[3:6] + '-' + x[6:]
  #   dashed_list.append(final_list)

  without_duplicates_num = list(dict.fromkeys(cleaned))

  with open("automation/phone_numbers.txt", "w+") as phone_list:
    for number in without_duplicates_num:
      phone_list.write(number)
      phone_list.write('\n')
      


  

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

  