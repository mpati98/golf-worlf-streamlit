import os
from pyairtable import Api
api = Api(os.environ['AIRTABLE_API_KEY'])


def create_customer(name, email, phone, message):
    table = api.table(os.environ["AIRTABLE_BASE_ID"], os.environ["AIRTABLE_TABLE_ID"])
    table.create({"Name": name, "Email": email, "Phone": phone, "Message": message})