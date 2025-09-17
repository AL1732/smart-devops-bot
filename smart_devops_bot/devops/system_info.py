import subprocess

def get_system_info():
    """
    Return basic system information as a dictionary
    """
    info = {}
    info['hostname'] = subprocess.getoutput("hostname")
    info['uptime'] = subprocess.getoutput("uptime")
    info['disk_usage'] = subprocess.getoutput("df -h /")
    return info
