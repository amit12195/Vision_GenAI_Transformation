# Vision_GenAI_Transformation

# Object Detection, Segmentation & Realistic Replacement with GenAI

## Overview
This project presents an end-to-end pipeline that:
- Detects and segments a kitchen object (**bottle** and **bowl**)
- Replaces it with a **style-matched generative variant** using diffusion model
- Generates a **3–5 second animation** of the transformed scene

## Option B – Kitchen Object Replacement

- Detected and segmented kitchen objects using **YOLOv8** and **SAM model** 
- Replaced the original object with a stylized or generative version using the **stable diffusion inpainting** method
- Maintained **visual realism** — lighting, shadow, and scene consistency.
- Generated a short **animated video/GIF file**  to illustrate the transformation using the Python-Pillow library and also the Kling Tool 

## Libraries & framework

- **Object Detection & Segmentation**: YOLOv8, Segment Anything Model, Pytorch
- **Image Transformation**: Stable Diffusion, inpainting & image-to-image generation
- **Animation Generation**: Pillow for GIF, [Other options: Pika, FramePack, SVD]
- **Preprocessing**: OpenCV, NumPy, PIL
- **Environment**: Python 3.10, Google Colab, Jupyter Notebook, Visual Studio Code

## GPU & Inference
- **GPU**: NVIDIA Tesla T4 — 15 GB VRAM (used Google Colab Free Tier)  
- **CUDA Version**: 12.4
- 
**Approximate Inference Time:**
| Task                          | Time (per frame)    |
|-------------------------------|----------------------------|
|  Detection + Segmentation   | ~3 seconds/image           |
|  Stable Diffusion           | ~6–8 seconds/image         |
|  giff/Animation Generation       | ~1 second/frame (using Pillow library; Kling tool generation time not measurable) |

## References

- [object detection & segmentation](https://blog.roboflow.com/how-to-use-yolov8-with-sam/)
- [YOLOv-8](https://docs.ultralytics.com/tasks/detect/)
- [SAM](https://github.com/facebookresearch/segment-anything)
- [Stable Diffusion](https://huggingface.co/stabilityai/stable-diffusion-2-inpainting)
- [Unsplash – Product Lifestyle Images](https://unsplash.com/s/photos/product-lifestyle)
- [Pexels – Lifestyle Product Photos](https://www.pexels.com/search/lifestyle%20product/)

