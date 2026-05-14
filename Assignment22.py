#task 1 (Search and Replace (The Log Masker))
import re
pattern = r"secretpassword123"
text = "User: labib2026, Status: Active, Password: secretpassword123"
output = re.sub(pattern,"[MASKED]",text)
print(output)
# task 2 (Meta Characters (The Domain Extractor))
import re
pattern = r"^mtk_firmware.bin$"
text = "mtk_firmware.bin"
if re.match(pattern,"mtk_firmware.bin"):
    print("Matched")
else:
    print("Not matched")
#task 3 (Character Class (The Hex Address Scanner))
import re 
text = "Memory block at 0x4a9f is corrupted but 0xzzzz is stable."
pattern = r"0x([0-9a-f]+)"
matches = re.findall(pattern,text)
print("Hexadecimal characters found:", matches)




