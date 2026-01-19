# Quick Start Instructions by Environment

Choose your environment and follow the exact steps below.

---

## 🖥️ Using VS Code

### One-Time Setup
1. Open VS Code
2. Open the terminal: **View → Terminal** (or press `` Ctrl+` ``)
3. Install OpenAI:
   ```bash
   pip install openai
   ```
4. Open `scripts/stream_with_log.py`
5. Find line 17: `openai.api_key = "your-api-key-here"`
6. Replace with your actual key: `openai.api_key = "sk-..."`
7. Save the file (**Ctrl+S** or **Cmd+S**)

### Every Time You Want to Use It
1. Open the terminal in VS Code
2. Navigate to scripts:
   ```bash
   cd scripts
   ```
3. Run:
   ```bash
   python stream_with_log.py
   ```
4. Type your question when prompted
5. Check the `responses/` folder for saved conversations

---

## 🐍 Using PyCharm

### One-Time Setup
1. Open PyCharm
2. Open the terminal at the bottom of the screen
3. Install OpenAI:
   ```bash
   pip install openai
   ```
4. In the project explorer, navigate to `scripts/stream_with_log.py`
5. Double-click to open it
6. Find line 17: `openai.api_key = "your-api-key-here"`
7. Replace with your actual key: `openai.api_key = "sk-..."`
8. Save the file (**Ctrl+S** or **Cmd+S**)

### Every Time You Want to Use It
1. Right-click on `stream_with_log.py` in the project explorer
2. Select **Run 'stream_with_log'**
3. Type your question in the console at the bottom
4. Check the `responses/` folder for saved conversations

**Alternative**: Use the terminal:
```bash
cd scripts
python stream_with_log.py
```

---

## 💻 Using Plain Terminal (Mac/Linux)

### One-Time Setup
1. Open Terminal
2. Navigate to the project:
   ```bash
   cd /path/to/casey-cranes-videos
   ```
3. Install OpenAI:
   ```bash
   pip3 install openai
   ```
   or
   ```bash
   python3 -m pip install openai
   ```
4. Edit the script with your favorite editor:
   ```bash
   nano scripts/stream_with_log.py
   ```
   or
   ```bash
   open -a TextEdit scripts/stream_with_log.py
   ```
5. Find line 17 and replace `"your-api-key-here"` with your actual API key
6. Save and close

### Every Time You Want to Use It
```bash
cd /path/to/casey-cranes-videos/scripts
python3 stream_with_log.py
```

---

## 🪟 Using Command Prompt (Windows)

### One-Time Setup
1. Press **Win+R**, type `cmd`, press Enter
2. Navigate to the project:
   ```cmd
   cd C:\path\to\casey-cranes-videos
   ```
3. Install OpenAI:
   ```cmd
   pip install openai
   ```
4. Edit the script:
   ```cmd
   notepad scripts\stream_with_log.py
   ```
5. Find line 17 and replace `"your-api-key-here"` with your actual API key
6. Save and close Notepad

### Every Time You Want to Use It
```cmd
cd C:\path\to\casey-cranes-videos\scripts
python stream_with_log.py
```

---

## 🔷 Using PowerShell (Windows)

### One-Time Setup
1. Press **Win+X** and select **Windows PowerShell**
2. Navigate to the project:
   ```powershell
   cd C:\path\to\casey-cranes-videos
   ```
3. Install OpenAI:
   ```powershell
   pip install openai
   ```
4. Edit the script:
   ```powershell
   notepad scripts\stream_with_log.py
   ```
5. Find line 17 and replace `"your-api-key-here"` with your actual API key
6. Save and close Notepad

### Every Time You Want to Use It
```powershell
cd C:\path\to\casey-cranes-videos\scripts
python stream_with_log.py
```

---

## 📓 Using Jupyter Notebook

### One-Time Setup
1. Install the OpenAI package in a notebook cell:
   ```python
   !pip install openai
   ```
2. Copy the script content from `stream_with_log.py` into notebook cells
3. Replace the API key in the appropriate cell

### Every Time You Want to Use It
Run all cells in sequence. The last cell will prompt for input.

**Note**: Streaming output in Jupyter may not work perfectly. Consider using a regular terminal for the best experience.

---

## 🚀 Quick Command Summary

| Environment | Command to Run |
|-------------|----------------|
| VS Code / PyCharm Terminal | `cd scripts && python stream_with_log.py` |
| Mac/Linux Terminal | `cd scripts && python3 stream_with_log.py` |
| Windows CMD | `cd scripts && python stream_with_log.py` |
| Windows PowerShell | `cd scripts; python stream_with_log.py` |

---

## 💡 Pro Tips

### For Complete Beginners
If you've never used a terminal before:
1. The **terminal** is just a text-based way to give commands to your computer
2. `cd` means "change directory" (like clicking into a folder)
3. `python` means "run this Python file"
4. Hit **Enter** after typing each command

### Check Python is Installed
```bash
python --version
```
or
```bash
python3 --version
```

Should show something like `Python 3.8.10` or higher.

### Where's My API Key?
Get it from: https://platform.openai.com/api-keys

It starts with `sk-` and is about 50 characters long.

---

**Still stuck?** Check out the full guide: `OPENAI_SETUP_GUIDE.md`
