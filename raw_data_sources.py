import pandas as pd
import numpy as np
import random

# 1. Set up list for defined SKUs and vendors

master_skus = ["GV-BUN-001", "GV-BUN-002", "BG-BREAD-001", "BG-BREAD-002", "GV-ROLL-001", "GV-ROLL-002", "BG-BAGUETTE-001", "BG-BAGUETTE-002", "GV-CROISSANT-001", "GV-CROISSANT-002", "BG-MUFFIN-001", "BG-MUFFIN-002", "GV-DONUT-001", "GV-DONUT-002", "BG-PANINI-001", "BG-PANINI-002", "GV-BAGEL-001", "GV-BAGEL-002", "BG-FLATBREAD-001", "BG-FLATBREAD-002"]
master_vendors = ["V-0098", "V-0102", "V-0115", "V-0120", "V-0133", "V-0147", "V-0155", "V-0168", "V-0179", "V-0184"]


#2. When generating the data, randomly pick from the above lists to create the messy data for the purchase orders.

raw_sap_purchase_orders = []
for i in range(5000):

    # Capture the random selections for this row FIRST
    current_sku = random.choice(master_skus)
    current_vendor = random.choice(master_vendors)

    # Evaluate the variable current_sku, not the string 'SKU'

    if 'BREAD' in current_sku or 'ROLL' in current_sku or 'BAGUETTE' in current_sku or 'DONUT' in current_sku:
        units_per_case = 12
    elif 'CROISSANT' in current_sku or 'BUN' in current_sku:
        units_per_case = 6
    elif 'MUFFIN' in current_sku or 'FLATBREAD' in current_sku:
        units_per_case = 8
    elif 'PANINI' in current_sku:
        units_per_case = 4
    elif 'BAGEL' in current_sku:
        units_per_case = 6
    else:
        units_per_case = 0

    # Append to dictionary using my variables, not the string names of the variables
    raw_sap_purchase_orders.append({
        'PO_Number': f'PO-{i:05d}',
        'Vendor_ID': current_vendor,
        'SKU': current_sku,
        'Case_Quantity': random.randint(40, 200),
        'Units_Per_Case': units_per_case,
    })

sapdf = pd.DataFrame(raw_sap_purchase_orders, columns= ['PO_Number', 'Vendor_ID', 'SKU', 'Case_Quantity', 'Units_Per_Case'])
sapdf.to_csv('/Users/jordaan/Documents/Analytics_Engineering/Analytics_Engineering_Vault/Sandbox_CSVs/raw_sap_purchase_orders.csv', index=False)

print("Raw SAP Purchase Orders Ready!")

# Generate the Messy Vendor ASN Data
raw_retaillink_asns = []

# Not every PO generated in SAP ships the same day
# Randomly sample 4000 out of 5000 POs to simulate what would actually be in transit
# random.sample() picks unique items so we don't grab the same PO twice
shipped_pos = random.sample(raw_sap_purchase_orders, 4000)

for po_record in shipped_pos:
    # Grab the baseline "Source of Truth" data from the SAP POs to use as the basis for the ASN data
    po_number = po_record['PO_Number']
    vendor_id = po_record['Vendor_ID']
    sku = po_record['SKU']
    expected_cases = po_record['Case_Quantity']
    expected_units = po_record['Units_Per_Case']

    # Assume a perfect shipment to start
    shipped_cases = expected_cases
    shipped_units = expected_units

    # Introduce some variability to simulate real-world discrepancies
    chance = random.random()

    if chance < 0.10: 
        # The 10% ANOMALY: The short shipment
        # Vendor shipped 5 to 20 cases LESS than what we ordered
        # Use max() to ensure the subtraction doesn't result in negative shipped cases
        shipped_cases = max(0, expected_cases - random.randint(5,20))
    
    elif chance < 0.15:
        # The 5% ANOMALY: The Wrong Case Pack (between 0.10 and 0.15)
        # Vendor shipped 10 packs instead of the expected 12 packs
        shipped_units = expected_units - 2

    elif chance < 0.18:
        # The 3% ANOMALY: Missing Data Entry
        # Vendor left the field blank in retail link
        shipped_cases = np.nan

    # Append the final generated vendor record
    raw_retaillink_asns.append({
        'PO_Number': po_number,
        'Vendor_ID': vendor_id,
        'SKU': sku,
        'Shipped_Cases': shipped_cases,
        'Shipped_Units_Per_Case': shipped_units
    })
asndf = pd.DataFrame(raw_retaillink_asns, columns= ['PO_Number', 'Vendor_ID', 'SKU', 'Shipped_Cases', 'Shipped_Units_Per_Case'])
asndf.to_csv('/Users/jordaan/Documents/Analytics_Engineering/Analytics_Engineering_Vault/Sandbox_CSVs/raw_retaillink_asns.csv', index=False)

print("Raw Retail Link ASNs Ready!")


