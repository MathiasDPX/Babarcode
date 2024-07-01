from barcode import Code128

for i in range(0, 30):
    content = f"{i+1:02d}"
    code = Code128(content)
    code.save(f"tools/barcodes/{content}")