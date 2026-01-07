import os

if not os.path.exists("Data"):
    os.mkdir("Data")

for i in range(1, 101):
    folder = f"Data/Tutorial{i}"
    if not os.path.exists(folder):
        os.mkdir(folder)

print(os.listdir("Data"))
for i in range(1, 101):
    os.rmdir(f"Data/Tutorial{i}")
os.rmdir("Data")