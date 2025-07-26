# GPU support | Docker Docs

**URL:** https://docs.docker.com/desktop/features/gpu/
**Word Count:** 1355
**Links Count:** 647
**Scraped:** 2025-07-16 01:48:09
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# GPU support in Docker Desktop for Windows

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

> Note >  > Currently GPU support in Docker Desktop is only available on Windows with the WSL2 backend.

Docker Desktop for Windows supports NVIDIA GPU Paravirtualization \(GPU-PV\) on NVIDIA GPUs, allowing containers to access GPU resources for compute-intensive workloads like AI, machine learning, or video processing.

## Prerequisites

To enable WSL 2 GPU Paravirtualization, you need:

  * A Windows machine with an NVIDIA GPU   * Up to date Windows 10 or Windows 11 installation   * [Up to date drivers](https://developer.nvidia.com/cuda/wsl) from NVIDIA supporting WSL 2 GPU Paravirtualization   * The latest version of the WSL 2 Linux kernel. Use `wsl --update` on the command line   * To make sure the [WSL 2 backend is turned on](https://docs.docker.com/desktop/features/wsl/#turn-on-docker-desktop-wsl-2) in Docker Desktop

## Validate GPU support

To confirm GPU access is working inside Docker, run the following:               $ docker run --rm -it --gpus=all nvcr.io/nvidia/k8s/cuda-sample:nbody nbody -gpu -benchmark     

This runs an n-body simulation benchmark on the GPU. The output will be similar to:               Run "nbody -benchmark [-numbodies=<numBodies>]" to measure performance.             -fullscreen       (run n-body simulation in fullscreen mode)             -fp64             (use double precision floating point values for simulation)             -hostmem          (stores simulation data in host memory)             -benchmark        (run benchmark to measure performance)             -numbodies=<N>    (number of bodies (>= 1) to run in simulation)             -device=<d>       (where d=0,1,2.... for the CUDA device to use)             -numdevices=<i>   (where i=(number of CUDA devices > 0) to use for simulation)             -compare          (compares simulation results running once on the default GPU and once on the CPU)             -cpu              (run n-body simulation on the CPU)             -tipsy=<file.bin> (load a tipsy model file for simulation)          > NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.          > Windowed mode     > Simulation data stored in video memory     > Single precision floating point simulation     > 1 Devices used for simulation     MapSMtoCores for SM 7.5 is undefined.  Default to use 64 Cores/SM     GPU Device 0: "GeForce RTX 2060 with Max-Q Design" with compute capability 7.5          > Compute 7.5 CUDA device: [GeForce RTX 2060 with Max-Q Design]     30720 bodies, total time for 10 iterations: 69.280 ms     = 136.219 billion interactions per second     = 2724.379 single-precision GFLOP/s at 20 flops per interaction     

## Run a real-world model: Llama2 with Ollama

Use the [official Ollama image](https://hub.docker.com/r/ollama/ollama) to run the Llama2 LLM with GPU acceleration:               $ docker run --gpus=all -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama     

Then start the model:               $ docker exec -it ollama ollama run llama2