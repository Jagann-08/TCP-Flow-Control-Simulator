import tkinter as tk
from tkinter import messagebox

total_packets = 12
sender_window = 4
receiver_window = 8

current_packet = 1
current_receiver_window = receiver_window


def start_simulation():
    global current_packet, current_receiver_window

    current_packet = 1
    current_receiver_window = receiver_window

    output.delete("1.0", tk.END)

    status_label.config(
        text="Simulation Started"
    )

    simulate()


def simulate():
    global current_packet, current_receiver_window

    if current_packet > total_packets:
        output.insert(tk.END, "\n================================\n")
        output.insert(tk.END, "All packets transmitted successfully!\n")
        output.insert(tk.END, "TCP Sliding Window Simulation Completed.\n")
        status_label.config(text="Simulation Completed")
        return

    start = current_packet
    end = min(start + sender_window - 1, total_packets)

    output.insert(tk.END, "\n--------------------------------\n")
    output.insert(tk.END, "Sender Window: ")
    output.insert(
        tk.END,
        " ".join(str(i) for i in range(start, end + 1))
    )
    output.insert(tk.END, "\n")

    output.insert(
        tk.END,
        f"Receiver Window: {current_receiver_window} packets\n"
    )

    output.insert(tk.END, "Sending packets...\n")

    ack = end

    output.insert(
        tk.END,
        f"Receiver received packets up to: {ack}\n"
    )

    output.insert(
        tk.END,
        f"ACK received: {ack}\n"
    )

    current_receiver_window -= 1

    if current_receiver_window < 4:
        current_receiver_window = 4

    output.insert(
        tk.END,
        f"Receiver Window Available: {current_receiver_window} packets\n"
    )

    current_packet = ack + 1

    output.insert(
        tk.END,
        f"Window slides to: {current_packet}\n"
    )

    root.after(1000, simulate)


root = tk.Tk()
root.title("TCP Flow Control - Sliding Window Simulator")
root.geometry("850x600")

title = tk.Label(
    root,
    text="TCP FLOW CONTROL SIMULATOR",
    font=("Arial", 22, "bold")
)

title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Sliding Window & Receiver Window Management",
    font=("Arial", 13)
)

subtitle.pack(pady=5)

info = tk.Label(
    root,
    text="Total Packets: 12     Sender Window: 4     Initial Receiver Window: 8",
    font=("Arial", 11)
)

info.pack(pady=10)

start_button = tk.Button(
    root,
    text="START SIMULATION",
    font=("Arial", 12, "bold"),
    command=start_simulation,
    padx=20,
    pady=10
)

start_button.pack(pady=10)

status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 12, "bold")
)

status_label.pack(pady=5)

output = tk.Text(
    root,
    height=22,
    width=90,
    font=("Consolas", 11)
)

output.pack(padx=15, pady=15)

root.mainloop()