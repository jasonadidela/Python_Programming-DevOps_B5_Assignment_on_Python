import psutil
import time

def monitor_cpu_usage(threshold=80):
    print("Monitoring CPU usage...")
    
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)
            if cpu_percent > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_percent:.2f}%")
            time.sleep(0)
    except KeyboardInterrupt:
        print("\nMonitoring stopped. Have a great day!")

if __name__ == "__main__":
    monitor_cpu_usage()