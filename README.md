<!-- Improved compatibility of back to top link -->

<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

<!-- PROJECT LOGO -->

<br />
<div align="center">
  <a href="https://github.com/your_username/ComfyUI-Ollama-VL-Prompt-Generator">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">ComfyUI Ollama VL Prompt Generator</h3>

  <p align="center">
    A custom ComfyUI node that uses Ollama vision-language models to generate or refine prompts from an input image and text.
    <br />
    <a href="#usage"><strong>Explore the usage »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    &middot;
    <a href="#">Report Bug</a>
    &middot;
    <a href="#">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](images/screenshot.png)

This project provides a **ComfyUI custom node** that connects to **Ollama** and lets the user choose *any* local vision-language (VL) model to generate or refine prompts based on:

* An input image (for image edit / image-to-image workflows)
* An optional base text prompt

The node is designed to be **model-agnostic**: it does not try to guess which models are VL-capable. If the model is installed in Ollama, the user can select it.

Key goals:

* Seamless prompt generation for image edit pipelines
* Preset-based instruction templates (e.g. SDXL edit, inpaint, style transfer)
* Automatic detection of installed Ollama models
* Zero cloud dependency — everything runs locally

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [Python](https://www.python.org/)
* [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
* [Ollama](https://ollama.com/)
* Vision-Language Models (user-provided via Ollama)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

Make sure you have the following installed:

* **ComfyUI** (working installation)
* **Ollama** running locally
* At least one **VL-capable model** pulled in Ollama (for example: llava, bakllava, qwen-vl, etc.)

You can verify Ollama is running with:

```sh
ollama list
```

### Installation

1. Clone this repository into your ComfyUI custom nodes folder:

   ```sh
   cd ComfyUI/custom_nodes
   git clone https://github.com/your_username/ComfyUI-Ollama-VL-Prompt-Generator.git
   ```

2. Restart ComfyUI

3. Ensure Ollama is running before executing a workflow

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

1. Add the **Ollama VL Prompt Generator** node to your workflow
2. Connect:

   * An **IMAGE** input
   * A **STRING** base prompt (optional)
3. Select:

   * Ollama model (auto-detected from local installation)
   * Preset (e.g. SDXL Edit, Inpaint Description, Style Transfer)
4. Use the generated text output as:

   * Positive prompt
   * Edit instruction
   * Conditioning input for downstream nodes

### Example Presets

* **SDXL Image Edit** – Generates a concise edit instruction
* **Style Expansion** – Extracts visual style and converts it into tags
* **Detail Booster** – Adds missing visual details from the image

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

* [x] Ollama model auto-detection
* [x] Image + text prompt support
* [x] Preset-based system prompts
* [ ] Custom user-defined presets via JSON
* [ ] Streaming token output
* [ ] Multi-image input support
* [ ] Advanced error handling & model validation

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are welcome and appreciated.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/MyFeature`)
3. Commit your changes
4. Push to your fork
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Juan – GitHub: [https://github.com/your_username](https://github.com/your_username)

Project Link: [https://github.com/your_username/ComfyUI-Ollama-VL-Prompt-Generator](https://github.com/your_username/ComfyUI-Ollama-VL-Prompt-Generator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

* ComfyUI community
* Ollama team
* Open-source VL model authors

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/your_username/ComfyUI-Ollama-VL-Prompt-Generator.svg?style=for-the-badge
[contributors-url]: https://github.com/your_username/ComfyUI-Ollama-VL-Prompt-Generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/your_username/ComfyUI-Ollama-VL-Prompt-Generator.svg?style=for-the-badge
[forks-url]: https://github.com/your_username/ComfyUI-Ollama-VL-Prompt-Generator/network/members
[stars-shield]: https://img.shields.io/github/stars/your_username/ComfyUI-Ollama-VL-Prompt-Generator.svg?style=for-the-badge
[stars-url]: https://github.com/your_username/ComfyUI-Ollama-VL-Prompt-Generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/your_username/ComfyUI-Ollama-VL-Prompt-Generator.svg?style=for-the-badge
[issues-url]: https://github.com/your_username/ComfyUI-Ollama-VL-Prompt-Generator/issues
[license-shield]: https://img.shields.io/github/license/your_username/ComfyUI-Ollama-VL-Prompt-Generator.svg?style=for-the-badge
[license-url]: https://github.com/your_username/ComfyUI-Ollama-VL-Prompt-Generator/blob/main/LICENSE
[product-screenshot]: images/screenshot.png
