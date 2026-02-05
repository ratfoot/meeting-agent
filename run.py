#!/usr/bin/env python3
"""Meeting Processor - uses Claude Code for API access."""

import subprocess
from pathlib import Path

try:
    from flask import Flask, render_template, request, jsonify
except ImportError:
    import os, sys
    print("Installing flask...")
    os.system(f"{sys.executable} -m pip install -q flask")
    from flask import Flask, render_template, request, jsonify

ROOT = Path(__file__).parent
app = Flask(__name__, template_folder=ROOT / "app" / "templates")


def get_agents():
    agents = {}
    for f in (ROOT / "agents").glob("*.md"):
        agents[f.stem] = f.read_text()
    return agents


@app.route("/")
def index():
    return render_template("index.html", agents=list(get_agents().keys()))


@app.route("/process", methods=["POST"])
def process():
    data = request.json
    agents = get_agents()
    agent_prompt = agents.get(data.get("agent", ""))
    transcript = data.get("transcript", "").strip()

    if not agent_prompt:
        return jsonify({"error": "No agent selected"}), 400
    if not transcript:
        return jsonify({"error": "No transcript"}), 400

    full_prompt = f"{agent_prompt}\n\nIMPORTANT: Generate ALL outputs automatically. Do not ask for confirmation.\n\n---\n\nINPUT:\n\n{transcript}"

    result = subprocess.run(
        ["claude", "-p", full_prompt],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return jsonify({"error": result.stderr or "Claude CLI failed"}), 500

    return jsonify({"result": result.stdout})


if __name__ == "__main__":
    import webbrowser
    print(f"Agents: {list(get_agents().keys())}")
    print("http://localhost:5001")
    webbrowser.open("http://localhost:5001")
    app.run(port=5001)
