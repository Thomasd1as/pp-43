c = 25
f = c * 9 / 5 + 32
print("ფარენგეიტი:",f)
c = 0
f = c * 9 / 5 + 32
print("ფარენგეიტი:", f)
c = -40
f = c * 9 / 5 + 32
print("ფარენგეიტი:",f)
seconds = int(input("წამი"))
hours = seconds // 3600
remaining = seconds % 3600
minutes = remaining // 60
seconds = remaining % 60
print(hours, "საათი", minutes, "წუთი", seconds, "წამი")