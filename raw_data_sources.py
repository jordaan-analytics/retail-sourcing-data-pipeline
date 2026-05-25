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
    elif 'CROISSANT' in current_sku:
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