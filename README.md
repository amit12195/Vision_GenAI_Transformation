# Vision_GenAI_Transformation

# 🍽️ Kitchen Object Replacement with Gen AI

## Overview
This project presents an end-to-end pipeline that:
- Detects and segments a kitchen object (e.g., **bottle** or **bowl**)
- Replaces it with a **style-matched generative variant** using diffusion model
- Generates a **3–5 second animation** of the transformed scene

## Option B – Kitchen Object Replacement

- Detected and segmented kitchen objects (bottle, bowl).
- Replaced the original object with a stylized or generative version using the **stable diffusion inpainting** method
- Maintained **visual realism** — lighting, shadow, and scene consistency.
- Produced a short **animated video** (GIF) to illustrate the transformation.

## Libraries & framework

- **Object Detection & Segmentation**: YOLOv8, Segment Anything Model, Pytorch
- **Image Transformation**: Stable Diffusion, inpainting & image-to-image generation
- **Animation Generation**: Pillow for GIF, [Other options: Pika, FramePack, SVD]
- **Preprocessing**: OpenCV, NumPy, PIL
- **Environment**: Python 3.10, Google Colab, Jupyter Notebook, Visual Studio Code

## GPU & Inference
- **GPU**: NVIDIA Tesla T4 — 15 GB VRAM (used Google Colab Free Tier)
- **CUDA version**: 12.4
- **Approx inference time**:   Detection + Segmentation: ~3 seconds/image,
                              - Inpainting: ~6–8 seconds/image,
                              - Animation generation: ~1 second/frame
