import tkinter as tk
import customtkinter as ctk

# Sample menu
menu = {
    'pizza': 40,
    'pasta': 26,
    'burger': 48,
    'salad': 80,
    'coffee': 100,
}

# Initialize the application
app = ctk.CTk()
app.title("Mini Restaurant")

# Calculate the position to center the window
window_width = 400
window_height = 500
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
app.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

order_total = 0
order_items = []

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Function to add item to order
def add_item():
    global order_total
    item = item_entry.get().lower()
    if item in menu:
        order_total += menu[item]
        order_items.append(item)
        order_listbox.insert(tk.END, f"{item.capitalize()}: Rs{menu[item]}")
        result_label.configure(text=f"Your item {item} has been added to your order.")
    else:
        result_label.configure(text=f"Ordered item {item} is not available yet.")
    total_label.configure(text=f"Total Amount: Rs{order_total}")

# Function to finalize the order
def finalize_order():
    global order_total, order_items
    if order_items:
        result_label.configure(text=f"The total amount of your order to pay is Rs{order_total}")
    else:
        result_label.configure(text="No items ordered yet.")
    total_label.configure(text=f"Total Amount: Rs{order_total}")

# Create frames
menu_frame = ctk.CTkFrame(app, corner_radius=15)
order_frame = ctk.CTkFrame(app, corner_radius=15)

for frame in (menu_frame, order_frame):
    frame.grid(row=0, column=0, sticky='nsew')

# Menu Frame
welcome_label = ctk.CTkLabel(menu_frame, text="Welcome to Mini Restaurant", font=("Arial", 20))
welcome_label.pack(pady=10)

menu_label = ctk.CTkLabel(menu_frame, text="Menu:\nPizza: Rs40\nPasta: Rs26\nBurger: Rs48\nSalad: Rs80\nCoffee: Rs100", font=("Arial", 14))
menu_label.pack(pady=10)

navigate_to_order_button = ctk.CTkButton(menu_frame, text="Go to Order Form", command=lambda: show_frame(order_frame))
navigate_to_order_button.pack(pady=20)

# Order Frame
item_label = ctk.CTkLabel(order_frame, text="Enter the name of the item you want to order:")
item_label.pack(pady=5)

item_entry = ctk.CTkEntry(order_frame)
item_entry.pack(pady=5)

add_item_button = ctk.CTkButton(order_frame, text="Add Item", command=add_item)
add_item_button.pack(pady=5)

order_listbox = tk.Listbox(order_frame, height=10)
order_listbox.pack(pady=10)

total_label = ctk.CTkLabel(order_frame, text="Total Amount: Rs0", font=("Arial", 14))
total_label.pack(pady=10)

finalize_button = ctk.CTkButton(order_frame, text="Finalize Order", command=finalize_order)
finalize_button.pack(pady=10)

result_label = ctk.CTkLabel(order_frame, text="")
result_label.pack(pady=10)

navigate_to_menu_button = ctk.CTkButton(order_frame, text="Back to Menu", command=lambda: show_frame(menu_frame))
navigate_to_menu_button.pack(pady=20)

# Show the menu frame initially
show_frame(menu_frame)

# Run the application
app.mainloop()
