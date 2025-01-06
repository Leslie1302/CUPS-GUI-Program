import tkinter as tk
from tkinter import messagebox
import cups
import subprocess

# Start CUPS
def start_cups():
    try:
        # Start the CUPS service (Linux-based command)
        sudo_password = sudo_password_var.get()
        if sudo_password:
            process = subprocess.run(
                ['sudo', '-S', 'systemctl', 'start', 'cups'],
                input=f'{sudo_password}\n', text=True, capture_output=True
            )

            if process.returncode != 0:
                raise subprocess.CalledProcessError(process.returncode, 'sudo')
            
            # Connect to CUPS
            connection = cups.Connection()
            printers = connection.getPrinters()
            printer_names = "\n".join([f"{printer}: {info['device-uri']}" for printer, info in printers.items()])
            
            label.config(text=f"CUPS started!\nAvailable Printers:\n{printer_names}")
            update_printer_list()
        else:
            messagebox.showerror("Error", "Please enter the sudo password.")

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error starting CUPS: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Stop CUPS
def stop_cups():
    try:
        # Start the CUPS service (Linux-based command)
        sudo_password = sudo_password_var.get()
        if sudo_password:
            process = subprocess.run(
                ['sudo', '-S', 'systemctl', 'stop', 'cups'],
                input=f'{sudo_password}\n', text=True, capture_output=True
            )

            if process.returncode != 0:
                raise subprocess.CalledProcessError(process.returncode, 'sudo')
            
            label.config(text="CUPS stopped successfully!")
            clear_printer_list()
        else:
            messagebox.showerror("Error", "Please enter the sudo password.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error stopping CUPS: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Update printer list (interactive)
def update_printer_list():
    # List available printers and categorize them
    connection = cups.Connection()
    printers = connection.getPrinters()
    
    printer_listbox.delete(0, tk.END)  # Clear the listbox

    for printer, info in printers.items():
        printer_listbox.insert(tk.END, printer)  # Add printer to the listbox

# Clear printer list
def clear_printer_list():
    printer_listbox.delete(0, tk.END)

# Handle printer selection
def on_printer_select(event):
    selected_item = printer_listbox.get(tk.ANCHOR)
    if selected_item:
        show_printer_options(selected_item)

# Show options for a selected printer
def show_printer_options(printer_name):
    # Show options: View Jobs, Reconnect, Disconnect
    options_frame.pack_forget()  # Hide previous options frame

    options_frame.pack()  # Show options
    reconnect_button.config(command=lambda: reconnect_printer(printer_name))
    disconnect_button.config(command=lambda: remove_printer(printer_name))
    view_jobs_button.config(command=lambda: view_jobs(printer_name))

# View jobs of a selected printer
def view_jobs(printer_name):
    connection = cups.Connection()
    jobs = connection.getJobs(where='all')
    job_list = [f"Job {job_id}: {job['job-name']}" for job_id, job in jobs.items() if job['printer'] == printer_name]
    if job_list:
        messagebox.showinfo("Printer Jobs", "\n".join(job_list))
    else:
        messagebox.showinfo("Printer Jobs", "No jobs found.")

# Reconnect a printer
def reconnect_printer(printer_name):
    try:
        connection = cups.Connection()
        connection.enablePrinter(printer_name)
        messagebox.showinfo("Printer Status", f"Printer {printer_name} reconnected.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to reconnect printer: {e}")

# Remove/disconnect a printer
def remove_printer(printer_name):
    try:
        connection = cups.Connection()
        connection.deletePrinter(printer_name)
        messagebox.showinfo("Printer Status", f"Printer {printer_name} disconnected.")
        update_printer_list()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to disconnect printer: {e}")

# Initialize Tkinter GUI
root = tk.Tk()
root.title("Printer Configuration")

# Password input frame
password_frame = tk.Frame(root)
password_frame.pack()

label = tk.Label(root, text="Enter sudo password to start/stop CUPS")
label.pack()

sudo_password_var = tk.StringVar()
password_entry = tk.Entry(password_frame, textvariable=sudo_password_var, show="*")
password_entry.pack()

# Buttons for start and stop CUPS
start_button = tk.Button(root, text="Start CUPS", command=start_cups)
start_button.pack()

stop_button = tk.Button(root, text="Stop CUPS", command=stop_cups)
stop_button.pack()

# Printer listbox and options
printer_listbox = tk.Listbox(root, height=10, width=50)
printer_listbox.pack()

printer_listbox.bind('<<ListboxSelect>>', on_printer_select)

options_frame = tk.Frame(root)

view_jobs_button = tk.Button(options_frame, text="View Jobs")
view_jobs_button.pack()

reconnect_button = tk.Button(options_frame, text="Reconnect")
reconnect_button.pack()

disconnect_button = tk.Button(options_frame, text="Disconnect")
disconnect_button.pack()

root.mainloop()
