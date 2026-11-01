login_logs = [
    "SUCCESS",
    "FAILED",
    "FAILED",
    "SUCCESS",
    "FAILED",
    "FAILED"
]

failed = 0
successful = 0

for log in login_logs:
    if log == "FAILED":
        failed += 1
    elif log == "SUCCESS":
        successful += 1

print("Successful logins:", successful)
print("Failed logins:", failed)

if failed >= 3:
    print("Warning: Multiple failed login attempts!")
