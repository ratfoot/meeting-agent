#!/usr/bin/env python3
"""Meeting Processor"""

import os
import subprocess
from pathlib import Path
from flask import Flask, render_template, request, jsonify

ROOT = Path(__file__).parent
app = Flask(__name__, template_folder=ROOT / "app" / "templates")


def get_agents():
    agents = {}
    for f in (ROOT / "agents").glob("*.md"):
        agents[f.stem] = f.read_text()
    return agents


def call_llm(prompt):
    """Call Gemini API if key set, otherwise Claude CLI locally."""
    if os.environ.get("GEMINI_API_KEY"):
        import google.generativeai as genai
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        model = genai.GenerativeModel("gemini-1.5-flash-lite")
        response = model.generate_content(prompt)
        return response.text
    else:
        result = subprocess.run(
            ["claude", "-p", prompt],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise Exception(result.stderr or "Claude CLI failed")
        return result.stdout


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

    try:
        result = call_llm(full_prompt)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))

    if os.environ.get("RAILWAY_ENVIRONMENT"):
        app.run(host="0.0.0.0", port=port)
    else:
        import webbrowser
        print(f"Agents: {list(get_agents().keys())}")
        print(f"http://localhost:{port}")
        webbrowser.open(f"http://localhost:{port}")
        app.run(port=port)
