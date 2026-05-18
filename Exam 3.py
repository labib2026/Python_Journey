#task 1(File Handling & Regex)
try:
    with open("firmware_log.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File does not exist")
try:
    import re
    pattern = r"labib9690@gmail.com"
    pattern2 = r"0x([0-9a-f]+)"
    admin_email = re.findall(pattern, content)
    memory_address = re.findall(pattern2,content)
    print(admin_email)
    print(memory_address)
except NameError:
    print("Cannot Access this file")

#task 2 (Class, Constructor & Inheritance)
model_name = "Redmi Note 14 5G"

class device:
    def __init__(self, model_name, memory_address):
        self.model_name = model_name
        self.memory_address = memory_address
        
    def device_info(self):
        print(f"Device: {self.model_name} is monitoring sector {self.memory_address}")

class SecurityGuard(device):

    def __init__(self, model_name, memory_address, admin_email):
        super().__init__(model_name, memory_address)
        self.admin_email = admin_email
        print(f"Admin email is {self.admin_email}")

#task 3 (Japanese Sync & Lock)
    def system_lock(self):
        print(f"System Locked! Security Alert sent to {self.admin_email}")
        
        with open("secured_report.txt", "w") as secured_file:
            secured_file.write("Mission Accomplished: Ganbatte!")
        print("secured_report.txt has been generated successfully!")

guard = SecurityGuard(model_name, memory_address[0], admin_email[0])

guard.device_info()
guard.system_lock()

