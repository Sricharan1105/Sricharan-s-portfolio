import tkinter as tk
import random

# Node class for the linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Queue class using a linked list
class Queue:
    def __init__(self, max_size=100):
        self.front = None
        self.rear = None
        self.size = 0
        self.max_size = max_size

    def enqueue(self, value):
        if self.size == self.max_size:
            return "Queue is full"
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        return "Element added"

    def dequeue(self):
        if self.front is None:
            return None
        removed_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return removed_value

    def is_empty(self):
        return self.front is None

    def clear(self):
        self.front = self.rear = None
        self.size = 0

    def peek(self):
        return self.front.value if self.front else None

    def get_queue(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    def search_by_value(self, value):
        current = self.front
        position = 1  # Start counting from 1
        while current:
            if current.value == value:
                return position
            current = current.next
            position += 1
        return -1

    def search_by_position(self, pos):
        if pos > self.size or pos < 1:
            return None
        current = self.front
        for _ in range(pos - 1):  # Adjust for 1-based indexing
            current = current.next
        return current.value if current else None

# GUI for Queue Visualization using Tkinter
class QueueVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.queue = Queue(max_size=10)
        self.title("Queue Implementation with Linked List")
        self.geometry("900x600")
        self.configure(bg="#f0f0f0")

        # Heading
        self.heading = tk.Label(self, text="Queue Visualization Using Linked List", font=("Helvetica", 16), bg="#f0f0f0")
        self.heading.pack(pady=10)

        # Canvas for queue visualization
        self.canvas = tk.Canvas(self, width=800, height=300, bg="white")
        self.canvas.pack(pady=20)

        # Status message label
        self.status_label = tk.Label(self, text="Enter a value and click 'Enqueue' to add to the queue.", font=("Helvetica", 12), bg="#f0f0f0")
        self.status_label.pack(pady=5)

        # Label above the input entry box
        self.entry_label = tk.Label(self, text="Enter the number:", font=("Helvetica", 12), bg="#f0f0f0")
        self.entry_label.pack()

        # Entry box for input
        self.entry = tk.Entry(self, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        # Frame for buttons
        button_frame = tk.Frame(self, bg="#f0f0f0")
        button_frame.pack(pady=10)

        # Button styles
        button_style = {"bg": "black", "fg": "white", "font": ("Helvetica", 12), "borderwidth": 2}

        # Enqueue button
        self.enqueue_button = tk.Button(button_frame, text="Enqueue", command=self.enqueue, **button_style)
        self.enqueue_button.pack(side=tk.LEFT, padx=5)

        # Dequeue button
        self.dequeue_button = tk.Button(button_frame, text="Dequeue", command=self.dequeue, **button_style)
        self.dequeue_button.pack(side=tk.LEFT, padx=5)

        # Search by Data button
        self.search_data_button = tk.Button(button_frame, text="Search by Data", command=self.search_by_data, **button_style)
        self.search_data_button.pack(side=tk.LEFT, padx=5)

        # Search by Position button
        self.search_position_button = tk.Button(button_frame, text="Search by Position", command=self.search_by_position, **button_style)
        self.search_position_button.pack(side=tk.LEFT, padx=5)

        # Is Empty button
        self.is_empty_button = tk.Button(button_frame, text="Is Empty", command=self.check_empty, **button_style)
        self.is_empty_button.pack(side=tk.LEFT, padx=5)

        # Clear Queue button
        self.clear_button = tk.Button(button_frame, text="Clear Queue", command=self.clear_queue, **button_style)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Peek button
        self.peek_button = tk.Button(button_frame, text="Peek", command=self.peek, **button_style)
        self.peek_button.pack(side=tk.LEFT, padx=5)

        # Exit button
        self.exit_button = tk.Button(button_frame, text="Exit", command=self.exit_app, **button_style)
        self.exit_button.pack(side=tk.LEFT, padx=5)

        self.update_canvas()

    def random_color(self):
        colors = ["#ff8a65", "#ffd54f", "#81c784", "#64b5f6", "#ba68c8", "#f06292"]
        return random.choice(colors)

    def enqueue(self):
        value = self.entry.get()
        if value:
            message = self.queue.enqueue(value)
            self.entry.delete(0, tk.END)
            self.update_canvas()
            self.status_label.config(text=message)
        else:
            self.status_label.config(text="Please enter a value.")

    def dequeue(self):
        removed_value = self.queue.dequeue()
        if removed_value is not None:
            self.update_canvas()
            self.status_label.config(text=f"Removed element: {removed_value}")
        else:
            self.status_label.config(text="Queue is empty!")

    def check_empty(self):
        if self.queue.is_empty():
            self.status_label.config(text="Queue is empty!")
        else:
            self.status_label.config(text="Queue is not empty!")
        self.entry.delete(0, tk.END)

    def clear_queue(self):
        self.queue.clear()
        self.update_canvas()
        self.status_label.config(text="Queue cleared.")
        self.entry.delete(0, tk.END)

    def peek(self):
        front_value = self.queue.peek()
        if front_value is not None:
            self.status_label.config(text=f"Front element: {front_value}")
        else:
            self.status_label.config(text="Queue is empty!")

    def search_by_data(self):
        value = self.entry.get()
        if value:
            position = self.queue.search_by_value(value)
            if position != -1:
                self.status_label.config(text=f"Element {value} found at position {position}.")
            else:
                self.status_label.config(text=f"Element {value} not found in the queue.")
        else:
            self.status_label.config(text="Please enter a value to search.")
        self.entry.delete(0, tk.END)

    def search_by_position(self):
        pos = self.entry.get()
        if pos.isdigit():
            pos = int(pos)
            value = self.queue.search_by_position(pos)
            if value is not None:
                self.status_label.config(text=f"Element at position {pos} is {value}.")
            else:
                self.status_label.config(text=f"No element found at position {pos}.")
        else:
            self.status_label.config(text="Please enter a valid position.")
        self.entry.delete(0, tk.END)

    def exit_app(self):
        self.quit()

    def update_canvas(self):
        self.canvas.delete("all")
        current = self.queue.front
        x = 50
        y = 100

        if current is None:
            self.status_label.config(text="Queue is empty!")
            return

        while current:
            color = self.random_color()
            self.canvas.create_rectangle(x, y, x + 60, y + 50, fill=color)
            self.canvas.create_rectangle(x + 60, y, x + 120, y + 50, fill="white")
            self.canvas.create_text(x + 30, y + 25, text=current.value, fill="black")
            next_address_text = f"{id(current.next)}" if current.next else "None"
            self.canvas.create_text(x + 90, y + 25, text=next_address_text, fill="blue")

            if current.next is not None:
                self.canvas.create_line(x + 120, y + 25, x + 180, y + 25, arrow=tk.LAST)

            current = current.next
            x += 180

        self.status_label.config(text="Queue visualized.")

if __name__ == "__main__":
    app = QueueVisualizer()
    app.mainloop()

