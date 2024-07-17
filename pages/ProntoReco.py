import streamlit as st
import PyPDF2

def extract_po_data(po_file):
    po_data = {}
    reader = PyPDF2.PdfReader(po_file)
    text = reader.pages[0].extract_text()
    po_data['po_number'] = text.split("PO #")[1].split("\n")[0].strip()
    
    items = text.split("EACH")[1:]
    po_data['items'] = []
    for item in items:
        try:
            quantity = int(item.split()[0].strip())
            unit_price = float(item.split()[1].replace(',', '').strip())
            total_price = float(item.split()[2].replace(',', '').strip())
            po_data['items'].append({'quantity': quantity, 'unit_price': unit_price, 'total_price': total_price})
        except (ValueError, IndexError):
            pass
    
    po_data['total_amount'] = float(text.split("TOTAL in INR")[1].split("\n")[0].replace(',', '').strip())
    return po_data

def extract_invoice_data(invoice_file):
    invoice_data = {}
    reader = PyPDF2.PdfReader(invoice_file)
    text = reader.pages[0].extract_text()
    invoice_data['invoice_number'] = text.split("INVOICE #")[1].split("\n")[0].strip()
    
    items = text.split("EACH")[1:]
    invoice_data['items'] = []
    for item in items:
        try:
            quantity = int(item.split()[0].strip())
            unit_price = float(item.split()[1].replace(',', '').strip())
            total_price = float(item.split()[2].replace(',', '').strip())
            invoice_data['items'].append({'quantity': quantity, 'unit_price': unit_price, 'total_price': total_price})
        except (ValueError, IndexError):
            pass
    
    try:
        invoice_data['total_before_taxes'] = float(text.split("TOTAL BEFORE TAXES")[1].split("\n")[0].replace(',', '').strip())
    except ValueError:
        invoice_data['total_before_taxes'] = None

    return invoice_data

def extract_delivery_note_data(delivery_note_file):
    delivery_note_data = {}
    reader = PyPDF2.PdfReader(delivery_note_file)
    text = reader.pages[0].extract_text()
    delivery_note_data['po_number'] = text.split("PO #")[1].split("\n")[0].strip()
    
    items = text.split("NOS")[1:]
    delivery_note_data['items'] = []
    for item in items:
        try:
            quantity = int(item.split()[0].strip())
            delivery_note_data['items'].append({'quantity': quantity})
        except (ValueError, IndexError):
            pass

    return delivery_note_data

def reconcile_documents(po_data, invoice_data, delivery_note_data):
    discrepancies = []

    for i, po_item in enumerate(po_data['items']):
        invoice_item = invoice_data['items'][i] if i < len(invoice_data['items']) else {}
        delivery_note_item = delivery_note_data['items'][i] if i < len(delivery_note_data['items']) else {}

        po_quantity = po_item.get('quantity')
        invoice_quantity = invoice_item.get('quantity')
        delivery_note_quantity = delivery_note_item.get('quantity')

        if po_quantity != invoice_quantity or po_quantity != delivery_note_quantity:
            discrepancies.append(f"Quantity mismatch for Item {i+1}: PO({po_quantity}), Invoice({invoice_quantity}), Delivery Note({delivery_note_quantity})")
        
        po_total = po_item.get('total_price')
        invoice_total = invoice_item.get('total_price')

        if po_total != invoice_total:
            discrepancies.append(f"Total price mismatch for Item {i+1}: PO({po_total}), Invoice({invoice_total})")

    if po_data['total_amount'] != invoice_data.get('total_before_taxes'):
        discrepancies.append(f"Total amount mismatch: PO({po_data['total_amount']}), Invoice({invoice_data.get('total_before_taxes')})")

    return discrepancies

def print_details(title, data):
    st.subheader(f"{title} Details:")
    for key, value in data.items():
        if key == 'items':
            st.write("Items:")
            for i, item in enumerate(value):
                st.write(f"  Item {i+1}: {item}")
        else:
            st.write(f"{key}: {value}")
    st.write("\n")

# Streamlit application
# st.title("Document Reconciliation")
st.title("ProntoReco")
st.header("Document Reconciliation")

po_file = st.file_uploader("Upload Purchase Order (PO) PDF", type="pdf")
invoice_file = st.file_uploader("Upload Invoice PDF", type="pdf")
delivery_note_file = st.file_uploader("Upload Delivery Note PDF", type="pdf")

if st.button("Submit"):
    if po_file and invoice_file and delivery_note_file:
        po_data = extract_po_data(po_file)
        invoice_data = extract_invoice_data(invoice_file)
        delivery_note_data = extract_delivery_note_data(delivery_note_file)
        
        print_details("PO", po_data)
        print_details("Invoice", invoice_data)
        print_details("Delivery Note", delivery_note_data)

        discrepancies = reconcile_documents(po_data, invoice_data, delivery_note_data)
        st.subheader("Discrepancies:")
        if discrepancies:
            for d in discrepancies:
                st.write(d)
        else:
            st.write("No discrepancies found.")
    else:
        st.write("Please upload all three documents.")
