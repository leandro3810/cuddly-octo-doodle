import psutil
import platform
from datetime import datetime
import json

def get_system_info():
    info = {}
    
    # Informações da CPU
    info['cpu_count'] = psutil.cpu_count(logical=True)
    info['cpu_usage'] = psutil.cpu_percent(interval=1)
    
    # Informações da Memória
    memory = psutil.virtual_memory()
    info['total_memory'] = memory.total
    info['available_memory'] = memory.available
    info['used_memory'] = memory.used
    info['memory_usage'] = memory.percent
    
    # Informações do Disco
    disk = psutil.disk_usage('/')
    info['total_disk'] = disk.total
    info['used_disk'] = disk.used
    info['free_disk'] = disk.free
    info['disk_usage'] = disk.percent
    
    # Informações do Sistema
    info['system'] = platform.system()
    info['node_name'] = platform.node()
    info['release'] = platform.release()
    info['version'] = platform.version()
    info['machine'] = platform.machine()
    info['processor'] = platform.processor()
    
    # Data e Hora
    info['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return info

def save_info_to_file(info, filename='system_info.json'):
    with open(filename, 'w') as file:
        json.dump(info, file, indent=4)

if __name__ == "__main__":
    system_info = get_system_info()
    save_info_to_file(system_info)
    print(f"Informações do sistema salvas em {filename}")
