import threading
import time
import json

with open('inventory.dat', 'r') as f:
    inventory = json.load(f)

def bot_clerk(items):
    """Simulate the clerk dispatching robots to fetch items."""
    if not items:
        return []

    cart = []  
    lock = threading.Lock() 

    robot_fetchers = [[] for _ in range(3)]
    for i, item in enumerate(items):
        robot_fetchers[i % 3].append(item)

    threads = []  # List to hold threads
    for fetcher_list in robot_fetchers:
        thread = threading.Thread(target=bot_fetcher, args=(fetcher_list, cart, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return cart

def bot_fetcher(items, cart, lock):
    """Simulate a robot fetching items from the warehouse."""
    for item in items:
        if item not in inventory:
            continue
        description, seconds = inventory[item]
        time.sleep(seconds)  
        with lock:
            cart.append([item, description])  