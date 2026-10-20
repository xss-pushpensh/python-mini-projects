
import time

print("===== Python Digital Clock =====")
print("Press Ctrl+C to stop.\n")

try:
    while True:
        current_time = time.strftime("%I:%M:%S %p")
        current_date = time.strftime("%d-%m-%Y")

        print(
            f"\rDate: {current_date} | Time: {current_time}",
            end="",
            flush=True
        )

        time.sleep(1)

except KeyboardInterrupt:
    print("\nClock stopped.")
