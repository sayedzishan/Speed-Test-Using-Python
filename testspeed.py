import tkinter as tk
from tkinter import messagebox
from speedtest import Speedtest

def test_internet_speed():
    st = Speedtest()
    try:
        download_speed = st.download() / 1e+6  # Convert from bits to Megabits
        upload_speed = st.upload() / 1e+6  # Convert from bits to Megabits
        messagebox.showinfo("Speed Test Results", 
                            "Download Speed: {:.2f} Mbps\nUpload Speed: {:.2f} Mbps".format(download_speed, upload_speed))
    except Exception as e:
        messagebox.showerror("Error", "Failed to test internet speed. Please check your internet connection.\n{}".format(e))

def main():
    root = tk.Tk()
    root.title("Internet Speed Test")

    label = tk.Label(root, text="Click the button to test your internet speed")
    label.pack(pady=10)

    button = tk.Button(root, text="Test Speed", command=test_internet_speed)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
