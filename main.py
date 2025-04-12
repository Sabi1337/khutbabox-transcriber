from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/beamer")
def beamer():
    original = "..."
    übersetzung = "..."

    if os.path.exists("textbuffer.txt"):
        with open("textbuffer.txt", "r") as f:
            content = f.read()
            parts = content.split("###UEBERSETZT###")
            if len(parts) == 2:
                original = parts[0].replace("###ORIGINAL###", "").strip()
                übersetzung = parts[1].strip()

    return render_template("beamer.html", original=original, translation=übersetzung)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
