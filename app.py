import streamlit as st
from contact_operations import add_contact, view_contacts, search_contact, remove_contact
from file_handler import load_contacts, save_contacts

st.set_page_config(page_title="Contact Book CLI Web", page_icon="📒")

st.title("📒 Contact Book Web App")

menu = ["Add Contact", "View Contacts", "Search Contact", "Remove Contact"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Contact":
    st.subheader("Add New Contact")
    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    address = st.text_area("Address")

    if st.button("Add Contact"):
        if not name or not phone:
            st.warning("Name and Phone are required.")
        elif not phone.isdigit():
            st.error("Phone must be numeric.")
        else:
            contacts = load_contacts()
            duplicate = any(c['Phone'] == phone for c in contacts)
            if duplicate:
                st.error("Phone number already exists.")
            else:
                contacts.append({'Name': name, 'Phone': phone, 'Email': email, 'Address': address})
                save_contacts(contacts)
                st.success("✅ Contact added successfully!")

elif choice == "View Contacts":
    st.subheader("All Contacts")
    contacts = load_contacts()
    if contacts:
        st.table(contacts)
    else:
        st.info("No contacts found.")

elif choice == "Search Contact":
    st.subheader("Search Contacts")
    term = st.text_input("Search by Name / Phone / Email")
    if st.button("Search"):
        found = None
        for c in load_contacts():
            if term.lower() in c['Name'].lower() or term in c['Phone'] or term.lower() in c['Email'].lower():
                found = c
                break
        if found:
            st.success("Contact Found:")
            st.json(found)
        else:
            st.warning("No matching contact found.")

elif choice == "Remove Contact":
    st.subheader("Remove Contact")
    phone = st.text_input("Enter Phone Number to Delete")
    if st.button("Delete"):
        contacts = load_contacts()
        index = next((i for i, c in enumerate(contacts) if c['Phone'] == phone), None)
        if index is not None:
            contacts.pop(index)
            save_contacts(contacts)
            st.success("Contact deleted successfully.")
        else:
            st.error("Contact not found.")
