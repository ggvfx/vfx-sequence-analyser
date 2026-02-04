# VFX Sequence Analyser

**VFX Sequence Analyser** is a professional multi-module utility designed to automate the extraction of shot data from sequence quicktimes. By utilizing local Computer Vision and LLMs, the tool segments footage and generates structured breakdowns, descriptions, and technical metadata. It is engineered to solve the "manual data-wrangling" bottleneck during editorial turnovers and re-bidding phases.

## Project Status
🚦 **Project Status:** Pre-Alpha (Vision & Architecture)
The project is currently in the active architectural phase, focusing on core media engine integration and vision-language model (VLM) benchmarking.
**Current Focus:** Developing the scene detection engine and SMPTE timecode validation logic.
**Next Milestone:** Functional CLI prototype capable of extracting shot-specific thumbnails and performing Zonal OCR on visual burn-ins.

## Strategic Roadmap
* **Phase 1 (Current):** Establish core media processing pipeline using FFmpeg and OpenCV; benchmark Florence-2 vs. Moondream2 for local captioning accuracy.
* **Phase 2 (Immediate):** Implement CLIP-based identity matching to enable stable character and prop tracking across non-contiguous shots.
* **Phase 3 (Q2 2026):** Transition to the PySide6 (Qt) "Human-in-the-Loop" interface, featuring a high-density review table and frame-accurate video player.

## 🚀 Overview
The **VFX Sequence Analyser** is designed to eliminate 70%+ of the repetitive "grunt work" involved in editorial change tracking and shot ingestion. Whether breaking down Previz for initial bidding or updating production databases after an editorial cut change, the tool ensures technical consistency without manual overhead.

The tool follows a **"Security-First"** and **"Human-in-the-Loop"** philosophy:
1. **Local AI:** All processing—including Computer Vision and LLM synthesis—happens 100% offline, ensuring sensitive, unreleased studio IP never leaves the machine.
2. **Professional Oversight:** AI handles the initial metadata and description pass, while a dedicated **Review & Validation UI** empowers VFX Coordinators to verify and edit data before final export.

## 🛠️ Key Features

* **Quicktime Parsing & Scene Detection:** Automates shot segmentation using Histogram diff and SSIM logic to detect hard cuts and fades with frame-accurate SMPTE timecode alignment.
* **Security-First Local Processing:** Leverages local Vision-Language Models (VLM) and Ollama for 100% private analysis of sensitive media assets.
* **Intelligent Element Extraction:** Automatically identifies shot framing (WS, MS, CU, etc.), camera movement, and performs Zonal OCR to classify burn-in data (Shot Name, Timecode) into structured columns.
* **Source & Feature Classification:** Auto-identifies media type (Plate, Previs, Storyboard) and scans for vfx items like Greenscreens and Tracking Markers.
* **Stable Identity Mapping:** Utilizes CLIP embeddings to track characters and hero props across a sequence, allowing users to replace generic IDs with project-specific names.
* **Hardware-Optimized Workflows:** Features "Eco" and "Power" processing modes to manage local compute resources, enabling smooth operation on production laptops or high-speed multi-threaded workstations.
* **Description Synthesis:** Translates raw vision tags into professional, human-readable VFX descriptions (e.g., "WS on John Doe as he manipulates Spanner") using local LLMs.
* **Session & State Management:** Includes robust "Save/Load" functionality via local JSON checkpoints, allowing for non-linear review and audit trails.

## 🛠️ Technical Stack
* **Language:** Python 3.11+
* **UI Framework:** PySide6 (Qt)
* **Media Engine:** FFmpeg, OpenCV, PySceneDetect
* **Vision Models:** Florence-2 / Moondream2, CLIP
* **Intelligence:** Ollama (Llama 3.2)

## 📂 Project Structure
* `src/core/`: Scene detection, timecode engine, and media processing.
* `src/vision/`: VLM integration, OCR, and identity matching logic.
* `src/ai/`: Ollama integration and description synthesis.
* `src/ui/`: PySide6 windows, review table, and video player components.

## 🚦 Status
**Planning Phase:** Currently defining core media ingestion logic and vision model benchmarking.
