# import os
import streamlit as st
from pyairtable import Api
# api = Api(os.environ['AIRTABLE_API_KEY'])
api = Api(st.secrets["AIRTABLE_API_KEY"])


def create_customer(name, email, phone, message):
    # table = api.table(os.environ["AIRTABLE_BASE_ID"], os.environ["AIRTABLE_TABLE_ID"])
    table = api.table(st.secrets["AIRTABLE_BASE_ID"], st.secrets["AIRTABLE_TABLE_ID"])
    table.create({"Name": name, "Email": email, "Phone": phone, "Message": message})