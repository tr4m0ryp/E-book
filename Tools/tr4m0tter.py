import os
import time
import threading
from datetime import datetime
import pyautogui
import keyboard
from tkinter import Tk, Canvas, Toplevel, Label, simpledialog
import winsound

class AreaSelector:
    def __init__(self):
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.bbox = None

        self.root = Tk()
        self.root.title("Select Area")
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.3)
        self.root.attributes("-topmost", True)
        self.root.configure(bg='gray80')

        self.canvas = Canvas(self.root, cursor="cross", bg="gray80")
        self.canvas.pack(fill="both", expand=True)

        self.instruction_label = Label(
            self.root, 
            text="Click and drag to select an area. Release to confirm.",
            font=("Helvetica", 16, "bold"), 
            bg="gray80", 
            fg="black"
        )
        self.instruction_label.place(relx=0.5, rely=0.05, anchor="center")

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.selection_complete = False

    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y,
            outline='red', width=3
        )

    def on_move_press(self, event):
        cur_x, cur_y = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        end_x, end_y = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        self.bbox = (
            int(round(min(self.start_x, end_x))),
            int(round(min(self.start_y, end_y))),
            int(round(max(self.start_x, end_x))),
            int(round(max(self.start_y, end_y)))
        )
        self.selection_complete = True
        self.root.quit()

    def get_bbox(self):
        self.root.mainloop()
        self.root.destroy()
        return self.bbox

def play_sound():
    frequency = 1500
    duration = 150
    try:
        winsound.Beep(frequency, duration)
    except RuntimeError as e:
        print(f"Error playing sound: {e}")

def take_screenshot(bbox, save_folder):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        filepath = os.path.join(save_folder, filename)
        region = (bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1])
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save(filepath)
        print(f"Screenshot saved: {filepath}")
        play_sound()
    except Exception as e:
        print(f"Error taking screenshot: {e}")

def flash_screen(bbox, duration=0.2):
    try:
        def flash():
            flash_root = Toplevel()
            flash_root.overrideredirect(True)
            flash_root.attributes("-topmost", True)
            flash_root.attributes("-alpha", 0.8)
            flash_root.configure(bg='white')
            x1, y1, x2, y2 = bbox
            width = x2 - x1
            height = y2 - y1
            flash_root.geometry(f"{width}x{height}+{x1}+{y1}")
            flash_root.update()
            time.sleep(duration)
            flash_root.destroy()

        threading.Thread(target=flash).start()
    except Exception as e:
        print(f"Error displaying flash: {e}")

def monitor_changes(bbox, save_folder, interval=1):
    last_screenshot = None
    while True:
        screenshot = pyautogui.screenshot(
            region=(bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1])
        )
        if last_screenshot is None or screenshot != last_screenshot:
            last_screenshot = screenshot
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = os.path.join(save_folder, f"autoscreenshot_{timestamp}.png")
            screenshot.save(filepath)
            print(f"Change detected. Screenshot saved: {filepath}")
            play_sound()
        time.sleep(interval)

def main():
    try:
        selector = AreaSelector()
        print("Select an area for screenshots by clicking and dragging.")
        bbox = selector.get_bbox()
        if not bbox:
            print("No area selected. Exiting script.")
            return

        print(f"Selected area: {bbox}")

        root = Tk()
        root.withdraw()
        save_folder = simpledialog.askstring("Output Folder", "Enter a name for the output folder:")
        if not save_folder:
            save_folder = f"screenshots_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.makedirs(save_folder, exist_ok=True)
        print(f"Screenshots will be saved in: {save_folder}")

        print("Choose a mode: Ctrl + Shift + K for manual screenshots or automatic on change.")
        mode = simpledialog.askstring("Mode", "Type 'manual' for manual or 'auto' for automatic:")
        if mode == 'manual':
            def on_activate():
                print("Hotkey detected. Taking screenshot...")
                take_screenshot(bbox, save_folder)
                flash_screen(bbox)

            print("Press Ctrl + Shift + K to take a screenshot. Press Esc to stop.")
            keyboard.add_hotkey('ctrl+shift+k', on_activate)
            keyboard.wait('esc')
            print("Esc detected. Exiting script.")
        elif mode == 'auto':
            print("Automatic mode started. Screenshots will be taken when changes are detected.")
            monitor_changes(bbox, save_folder)
        else:
            print("Invalid mode selected. Exiting script.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
