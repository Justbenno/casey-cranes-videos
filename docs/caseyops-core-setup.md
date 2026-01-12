# CaseyOps Core Setup (Swift) – Pick Your Path

All good — this is normal. You don’t need to be a terminal wizard to get this moving. We’ll make it idiot-proof (with love). Choose the option that matches what you’re using.

## Option A (Easiest): GitHub Codespaces – no installs
1. Open your `caseyops-core` repo on GitHub.
2. Click the green **Code** button → **Codespaces** → **Create Codespace on main**.
3. In the terminal that opens, run:
   ```bash
   swift build
   swift test
   ```
4. If it passes, commit and push:
   ```bash
   git commit -am "Initial CaseyOpsCore domain + template + evidence engine"
   git push
   ```
5. Reply back: **Commit 1 done**.

## Option B: On your Mac (Xcode installed)
1. Install Xcode from the App Store if needed.
2. In Terminal, go to the repo:
   ```bash
   cd path/to/caseyops-core
   swift build
   swift test
   ```
3. If green, commit and push:
   ```bash
   git add -A
   git commit -m "Initial CaseyOpsCore domain + template + evidence engine"
   git push
   ```

## Option C: One-command Docker (Mac/Windows/Linux)
From the repo folder run:
- PowerShell (Windows):
  ```bash
  docker run --rm -v "%cd%":/workspace -w /workspace swift:5.9 swift test
  ```
- macOS/Linux:
  ```bash
  docker run --rm -v "$PWD":/workspace -w /workspace swift:5.9 swift test
  ```

## Option D: “No idea, I just have a browser”
- Choose **Option A (Codespaces)** — it’s click-only and runs in the browser.

---

### What to tell us
Reply with which one you’re using:
**A)** GitHub Codespaces  
**B)** Mac with Xcode  
**C)** Docker  
**D)** “No idea, I just have a browser”

Once you confirm, we’ll give exact click-by-click steps for your path. After Commit 1 is green, the rest will feel like loading ammo into a magazine.
