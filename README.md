# CUPS GUI Program  

**CUPS GUI Program** is a Python-based application that provides an intuitive graphical user interface (GUI) for managing printers via the Common UNIX Printing System (CUPS). Designed to simplify printer management tasks, this program allows users to start and stop the CUPS service, view available printers, connect to unconfigured printers, disconnect existing ones, and monitor printer jobs—all from a single interface.  

## Features  

### Core Functionalities  

1. **Start and Stop CUPS Service**  
   - Quickly start or stop the CUPS service with a single click.  
   - Prompts for `sudo` credentials securely via a GUI dialog.  

2. **List Available Printers**  
   - Displays a categorized list of:  
     - **Configured Printers**: Printers already set up in the system.  
     - **Unconfigured Printers**: Detected printers not yet configured.  

3. **Manage Configured Printers**  
   - View print jobs.  
   - Reconnect to printers that might have been disconnected.  
   - Disconnect printers that are no longer required.  

4. **Manage Unconfigured Printers**  
   - Connect to printers by specifying their device URI.  
   - Disconnect or delete unconfigured printers.  

5. **User-friendly Interface**  
   - Built with `tkinter` to provide a clean, straightforward GUI.  
   - Intuitive layout with clear action buttons based on selected printer type.  

## Installation  

### Prerequisites  

Ensure your system has the following:  

1. **CUPS (Common UNIX Printing System)**  
   - Install using your package manager (e.g., `sudo apt install cups` on Debian-based systems).  

2. **Python 3.x**  
   - Verify installation with:  
     ```bash  
     python3 --version  
     ```  

3. **pip**  
   - Install if not already available:  
     ```bash  
     sudo apt install python3-pip  
     ```  

### Required Python Modules  

Install the dependencies using pip:  

```bash  
pip install tkinter cups subprocess  

    Note: tkinter is bundled with Python on most systems. If not, install it via your package manager.

Clone the Repository

git clone https://github.com/Leslie1302/CUPS-GUI-Program.git  
cd CUPS-GUI-Program  

Usage
Running the Program

Launch the program with:

python3 main.py  

How to Use

    Starting the CUPS Service
        Click on the "Start CUPS and list available printers" button.
        Enter your sudo password when prompted.
        View the list of configured and unconfigured printers.

    Stopping the CUPS Service
        Click the "Stop CUPS" button.
        The application will clear the printer list and stop the service.

    Selecting a Printer
        Select a printer from the list displayed in the GUI.
        Depending on the type of printer (configured or unconfigured), the program will show relevant actions:
            View Jobs
            Reconnect
            Disconnect/Delete
            Connect Printer

    Managing Jobs
        Use the "View Jobs" option to monitor the print queue of a selected printer.

    Connecting to Unconfigured Printers
        Choose an unconfigured printer from the list.
        Enter the sudo password and connect using the displayed device URI.

    Disconnecting or Deleting Printers
        Select a printer and use the relevant action button to disconnect or delete the printer configuration.

Project Structure

    main.py: The core program script containing the GUI and CUPS interaction logic.
    README.md: Documentation for understanding and using the project.

Technologies Used

    Python: Main programming language.
    tkinter: For creating the graphical user interface.
    cups: Python library for interacting with the CUPS printing system.
    subprocess: For securely executing system commands.

Troubleshooting

    Error: Module Not Found
        Ensure all required modules are installed:

    pip install tkinter cups subprocess  

CUPS Service Not Starting

    Check if the CUPS service is installed and enabled:

sudo systemctl status cups  

Install it if necessary:

        sudo apt install cups  

    Permission Issues
        Ensure the user has sudo privileges to start and stop the CUPS service.

Contribution

Contributions are welcome! Follow these steps:

    Fork the repository.
    Create a new branch:

git checkout -b feature-name  

Commit your changes:

git commit -m "Add feature-name"  

Push to your branch:

    git push origin feature-name  

    Open a Pull Request on GitHub.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Author

Leslie1302
Leslie Nii-Adjetey
