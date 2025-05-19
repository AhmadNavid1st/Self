# ╔════════════════════════════════════════════════════════╗
# 🎯  Dual Python Scheduler: m.py (10 min) & mm.py (9 min) 🎯
# ╚════════════════════════════════════════════════════════╝

import time           # ⏰ for sleeping
import subprocess     # ⚙️ for running commands
import threading      # 🧵 for concurrency

def run_script(script_name: str, interval_min: int):
    """
    👉 Runs the given script every `interval_min` minutes.
    """
    def _runner():
        # ✨ Run once immediately
        _execute()
        # 🔄 Then loop forever
        while True:
            print(f"⌛ Waiting {interval_min} minutes until next run of {script_name}...")
            time.sleep(interval_min * 60)
            _execute()

    def _execute():
        try:
            subprocess.run(["python", script_name], check=True)
            now = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"✅ {script_name} ran successfully at {now}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running {script_name}: {e}")

    # 🏃 Start in its own thread
    thread = threading.Thread(target=_runner, daemon=True)
    thread.start()

def main():
    # ▶️ Schedule both scripts
    run_script("m.py", 10)   # every 10 minutes
    run_script("mm.py", 9)   # every 9 minutes

    # 🛑 Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Scheduler stopped by user.")

if __name__ == "__main__":
    main()
