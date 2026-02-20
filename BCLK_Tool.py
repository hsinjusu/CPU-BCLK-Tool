import tkinter as tk
from tkinter import messagebox
import math


def calculate():
    try:
        bclk = float(entry_bclk.get())
        target_p = float(entry_p.get())
        target_e = float(entry_e.get())

        # 計算倍頻 (向上取整)
        p_ratio = math.ceil(target_p / bclk)
        e_ratio = math.ceil(target_e / bclk)

        actual_p = p_ratio * bclk
        actual_e = e_ratio * bclk

        result_text = (
            f"--- 計算結果 ---\n"
            f"P-Core 倍頻設為: {p_ratio} (實際 {actual_p:.1f} MHz)\n"
            f"E-Core 倍頻設為: {e_ratio} (實際 {actual_e:.1f} MHz)\n\n"
            f"--- BIOS 設定參考 ---\n"
            f"> BCLK Frequency: {bclk}\n"
            f"> P-Core Ratio: {p_ratio}\n"
            f"> E-Core Ratio: {e_ratio}\n"
            f"> BCLK Aware Adaptive: Enabled\n"
            f"> TVB Voltage Opt: Disable\n"
            f"> Additional Turbo Voltage: 1.30V"
        )
        label_result.config(text=result_text, fg="#004da8")
    except ValueError:
        messagebox.showerror("錯誤", "請輸入有效的數字")


# 建立視窗
root = tk.Tk()
root.title("BCLK Aware 電壓計算器")
root.geometry("400x500")

# 介面元件
tk.Label(root, text="BCLK Aware Adaptive Voltage", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="1. 設定 BCLK (外頻):").pack()
entry_bclk = tk.Entry(root, justify='center')
entry_bclk.insert(0, "120")
entry_bclk.pack(pady=5)

tk.Label(root, text="2. P-Core 目標頻率 (MHz):").pack()
entry_p = tk.Entry(root, justify='center')
entry_p.insert(0, "5500")
entry_p.pack(pady=5)

tk.Label(root, text="3. E-Core 目標頻率 (MHz):").pack()
entry_e = tk.Entry(root, justify='center')
entry_e.insert(0, "4700")
entry_e.pack(pady=5)

tk.Button(root, text="開始計算", command=calculate, bg="#0078d4", fg="white", width=20).pack(pady=20)

label_result = tk.Label(root, text="", justify="left", font=("Consolas", 10))
label_result.pack(pady=10)

root.mainloop()