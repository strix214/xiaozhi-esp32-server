import subprocess
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Stress test for the server')
    parser.add_argument('--thread', type=int, default=5, help='并发进程数设置')
    return parser.parse_args()

script = "main.py"
processes = []
args = parse_args()
thread = args.thread

for _ in range(thread):
    process = subprocess.Popen(["python", script])
    processes.append(process)

for process in processes:
    process.wait()


