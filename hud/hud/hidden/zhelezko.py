import psutil
import platform


def eating():
    cpu_frequency = psutil.cpu_freq()
    cpu_cores = psutil.cpu_count(logical=False)
    ram = psutil.virtual_memory()
    ram2 = round(ram[0] / 1073741824)
    my_system = platform.uname()

    data_list = {
        'cpu_cores': cpu_cores,
        'cpu_frequency': cpu_frequency[0],
        'ram': ram2,
        'system': f"{my_system.system} {my_system.release}"
    }
    return data_list
