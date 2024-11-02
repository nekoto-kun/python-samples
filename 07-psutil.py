import psutil

def list_processes():
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}, Cmdline: {process.info['cmdline']}")

list_processes()
