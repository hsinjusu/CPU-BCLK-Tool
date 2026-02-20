# BCLK Aware Adaptive Voltage Calculator

這是一個專為 **Intel® Core™ Ultra 7 270K** 等 Arrow Lake 處理器設計的超頻計算工具。

## 核心功能
在拉高 BCLK（如 120MHz）時，自動計算對應的 P-Core 與 E-Core 倍頻 (Ratio)，以確保開啟 **BCLK Aware Adaptive Voltage** 後系統能穩定運行。

## BIOS 操作建議 (ASUS Z系列主機板)
1. **CPU Power Management**: 將 `Boot performance mode` 設為 `Turbo Performance`。
2. **Ai Overclock Tuner**: 設為 `Manual` 並將 `CPU BCLK Frequency` 設為您要的目標 (如 120)。
3. **Thermal Velocity Boost**: 關閉 `TVB Voltage Optimization`。
4. **Voltage 設定**:
   - `BCLK Aware Adaptive Voltage`: **Enabled**
   - `Additional Turbo mode CPU Core Voltage`: 建議設為 **1.30V** 以上進行測試。

## 計算公式
本工具採用向上取整邏輯：
- `Ratio = ceil(Target_Freq / BCLK)`
- 例如：`5500MHz / 120 BCLK = 45.83 -> 設定為 46`

## 使用環境
- Python 3.10 或 3.11
- 無須額外套件，直接執行 `python BCLK_Tool.py` 即可。
