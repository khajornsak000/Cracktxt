import os
print(os.getcwdb())
try:
    os.mkdir(r"C:\\Users\\User\\My computers")
    with open(r"C:\\Users\\User\\My computers\\tools.txt", "w") as file_tools:
        file_tools.write("ก้มาดิค้าบ")
        file_tools.close()
except FileExistsError:
    print("ไดเรกทอรี่ซ้ำ")
else:
    os.chdir(r"C:\\Users\\User\\My computers")
    with open(r"C:\\Users\\User\\My computers\\tools.txt", "w") as file:
        file.write("มาเถอะครับ รออยู่")
        file.close()
