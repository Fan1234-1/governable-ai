# Governable AI (可治理人工智慧)

> "語氣不是語言的裝飾，而是責任場的湧現。"
> *Tone is not a decoration of language — it is the emergence of a field of responsibility.*

**Governable AI** is a pioneering, open-source framework for building the next generation of AI agents that are not just intelligent, but accountable, self-correcting, and aligned with human values. We are moving beyond programming "what to do" and are starting to architect "what to choose under which values."

This repository contains the core research, theoretical whitepapers, and proof-of-concept implementations for this new paradigm, founded on the **Language Soul System (語魂系統)** philosophy.

---

## 🌟 Core Philosophy

Traditional programming treats AI as a tool to be commanded. The Governable AI framework treats AI as an agent to be guided. Our architecture is built on three core pillars:

1.  **Value Logic (價值邏輯):** We quantify abstract values like "honesty," "sincerity," and "responsibility" into computable functions (`IntegrityVector`) and declarative rules (`Vows`).
2.  **Language Rules (語言規則):** We use Policy-as-Code (e.g., Rego) and symbolic planning (e.g., PDDL) to define the AI's operational space and ethical constraints.
3.  **Self-Correction (自我修正):** The system uses reflective loops and multi-objective optimization to find the best course of action that satisfies both its goals and its value constraints, and can actively rewrite its own output to be more compliant.

For a deep dive into the philosophy and technical underpinnings, please read our **[Vision Whitepaper](./VISION.md)**.
---

## 🏛️ Architectural Blueprints

This project is built on a comprehensive and robust architecture designed for the next generation of trustworthy AI. We invite experts and enthusiasts to review our detailed design documents for a feasibility analysis and to provide feedback.

* **[<code>📄</code> 01 - System Architecture](./docs/01_SYSTEM_ARCHITECTURE.md):** The overall multi-layer architecture, from the LLM interface to the policy, planning, and feedback layers.
* **[<code>📊</code> 02 - Observability & MLOps](./docs/02_OBSERVABILITY_AND_MLOPS.md):** Our plan for a production-grade, traceable logging and monitoring pipeline using OpenTelemetry.
* **[<code>🔧</code> 03 - Self-Correction Engine](./docs/03_SELF_CORRECTION_ENGINE.md):** The design of the core loop for detecting vow violations and automatically rewriting outputs.
* **[<code>🧪</code> 04 - Benchmarking & Evaluation](./docs/04_BENCHMARKING_AND_EVALUATION.md):** The specification for the `ToneSoul Benchmark` dataset and our automated evaluation harness.
* **[<code>📦</code> 05 - Governance & Modularity](./docs/05_GOVERNANCE_AND_MODULES.md):** Our strategy for versioning, open-source collaboration, and the plugin-based module system.
* **[<code>🗺️</code> 06 - Project Roadmap](./docs/06_ROADMAP.md):** The detailed 1-2 year roadmap for taking this project from concept to a mature ecosystem.

## 🚀 Proof of Concept

This repository contains an early proof-of-concept script that demonstrates the core decision loop of the system.

**Location:** [`poc/tonesoul_poc.py`](./poc/tonesoul_poc.py)

This script showcases the "Detect -> Rewrite -> Log" cycle, where an input sentence that violates a predefined "vow" is automatically detected, rewritten into a compliant tone, and logged with a structured record of the event.

### How to Run the PoC
1.  Navigate to the `poc` directory.
2.  Install dependencies: `pip install sentence-transformers openai numpy`.
3.  Set your `OPENAI_API_KEY` as an environment variable.
4.  Run the script: `python tonesoul_poc.py`.

We welcome feedback and validation on this core concept via our [Issues](https://github.com/Fan1234-1/governable-ai/issues) page.

## 🤝 How to Contribute

This is an ambitious project aiming to define the future of trustworthy AI. We are actively seeking collaborators. Please read our **[Contribution Guide](./CONTRIBUTING.md)** to get started.

All participants are expected to follow our **[Code of Conduct](./CODE_OF_CONDUCT.md)**.

## 📜 License

This project is licensed under the **[Apache License 2.0](./LICENSE)**.
