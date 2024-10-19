# Community Nodes

These are nodes that have been developed by the community, for the community. If you're not sure what a node is, you can learn more about nodes [here](overview.md).

If you'd like to submit a node for the community, please refer to the [node creation overview](contributingNodes.md).

To use a node, add the node to the `nodes` folder found in your app install location. 

The suggested method is to use `git clone` to clone the repository the node is found in. This allows for easy updates of the node in the future. 

If you'd prefer, you can also just download the whole node folder from the linked repository and add it to the `nodes` folder. 

To use a community workflow, download the `.json` node graph file and load it into Aittor AI via the **Load Workflow** button in the Workflow Editor. 

- Community Nodes
    + [Adapters-Linked](#adapters-linked-nodes)
    + [Autostereogram](#autostereogram-nodes)
    + [Average Images](#average-images)
    + [Clean Image Artifacts After Cut](#clean-image-artifacts-after-cut)
    + [Close Color Mask](#close-color-mask) 
    + [Clothing Mask](#clothing-mask)
    + [Contrast Limited Adaptive Histogram Equalization](#contrast-limited-adaptive-histogram-equalization)
    + [Depth Map from Wavefront OBJ](#depth-map-from-wavefront-obj)
    + [Enhance Detail](#enhance-detail)
    + [Film Grain](#film-grain)
    + [Generative Grammar-Based Prompt Nodes](#generative-grammar-based-prompt-nodes)
    + [GPT2RandomPromptMaker](#gpt2randompromptmaker)
    + [Grid to Gif](#grid-to-gif)
    + [Halftone](#halftone)
    + [Hand Refiner with MeshGraphormer](#hand-refiner-with-meshgraphormer)
    + [Image and Mask Composition Pack](#image-and-mask-composition-pack)
    + [Image Dominant Color](#image-dominant-color)
    + [Image to Character Art Image Nodes](#image-to-character-art-image-nodes)
    + [Image Picker](#image-picker)
    + [Image Resize Plus](#image-resize-plus)
    + [Latent Upscale](#latent-upscale)
    + [Load Video Frame](#load-video-frame)
    + [Make 3D](#make-3d)
    + [Mask Operations](#mask-operations)
    + [Match Histogram](#match-histogram)
    + [Metadata-Linked](#metadata-linked-nodes)
    + [Negative Image](#negative-image)
    + [Nightmare Promptgen](#nightmare-promptgen)
    + [Ollama](#ollama-node)
    + [One Button Prompt](#one-button-prompt)
    + [Oobabooga](#oobabooga)
    + [Prompt Tools](#prompt-tools)
    + [Remote Image](#remote-image)
    + [BriaAI Background Remove](#briaai-remove-background)
    + [Remove Background](#remove-background)    
    + [Retroize](#retroize)
    + [Size Stepper Nodes](#size-stepper-nodes)
    + [Simple Skin Detection](#simple-skin-detection)
    + [Text font to Image](#text-font-to-image)
    + [Thresholding](#thresholding)
    + [Unsharp Mask](#unsharp-mask)
    + [XY Image to Grid and Images to Grids nodes](#xy-image-to-grid-and-images-to-grids-nodes)
- [Example Node Template](#example-node-template)
- [Disclaimer](#disclaimer)
- [Help](#help)


--------------------------------
### Adapters Linked Nodes

**Description:** A set of nodes for linked adapters (ControlNet, IP-Adaptor & T2I-Adapter). This allows multiple adapters to be chained together without using a `collect` node which means it can be used inside an `iterate` node without any collecting on every iteration issues.

- `ControlNet-Linked` - Collects ControlNet info to pass to other nodes.
- `IP-Adapter-Linked` - Collects IP-Adapter info to pass to other nodes.
- `T2I-Adapter-Linked` - Collects T2I-Adapter info to pass to other nodes.

Note: These are inherited from the core nodes so any update to the core nodes should be reflected in these. --------------------------------
### Autostereogram Nodes

**Description:** Generate autostereogram images from a depth map. This is not a very practically useful node but more a 90s nostalgic indulgence as I used to love these images as a kid.

**Node Link:** https://github.com/skunkworxdark/autostereogram_nodes

**Example Usage:**
</br>
<img src="https://raw.githubusercontent.com/skunkworxdark/autostereogram_nodes/refs/heads/main/images/spider.png" width="200" /> -> <img src="https://raw.githubusercontent.com/skunkworxdark/autostereogram_nodes/refs/heads/main/images/spider-depth.png" width="200" /> -> <img src="https://raw.githubusercontent.com/skunkworxdark/autostereogram_nodes/refs/heads/main/images/spider-dots.png" width="200" /> <img src="https://raw.githubusercontent.com/skunkworxdark/autostereogram_nodes/refs/heads/main/images/spider-pattern.png" width="200" />

--------------------------------
### Average Images

**Description:** This node takes in a collection of images of the same size and averages them as output. It converts everything to RGB mode first.--------------------------------
### Clean Image Artifacts After Cut

Description: Removes residual artifacts after an image is separated from its background.

--------------------------------
### Close Color Mask

Description: Generates a mask for images based on a closely matching color, useful for color-based selections.

--------------------------------
### Clothing Mask

Description: Employs a U2NET neural network trained for the segmentation of clothing items in images.--------------------------------
### Contrast Limited Adaptive Histogram Equalization

Description: Enhances local image contrast using adaptive histogram equalization with contrast limiting.

--------------------------------
### Depth Map from Wavefront OBJ

**Description:** Render depth maps from Wavefront .obj files (triangulated) using this simple 3D renderer utilizing numpy and matplotlib to compute and color the scene. There are simple parameters to change the FOV, camera position, and model orientation.

To be imported, an .obj must use triangulated meshes, so make sure to enable that option if exporting from a 3D modeling program. This renderer makes each triangle a solid color based on its average depth, so it will cause anomalies if your .obj has large triangles. In Blender, the Remesh modifier can be helpful to subdivide a mesh into small pieces that work well given these limitations.--------------------------------
### Enhance Detail

**Description:** A single node that can enhance the detail in an image. Increase or decrease details in an image using a guided filter (as opposed to the typical Gaussian blur used by most sharpening filters.) Based on the `Enhance Detail` ComfyUI node from  https://github.com/spacepxl/ComfyUI-Image-Filters

**Node Link:** https://github.com/skunkworxdark/enhance-detail-node

**Example Usage:**
</br>
<img src="https://raw.githubusercontent.com/skunkworxdark/enhance-detail-node/refs/heads/main/images/Comparison.png" />

--------------------------------
### Film Grain

**Description:** This node adds a film grain effect to the input image based on the weights, seeds, and blur radii parameters. It works with RGB input images only.--------------------------------
### Generative Grammar-Based Prompt Nodes

**Description:** This set of 3 nodes generates prompts from simple user-defined grammar rules (loaded from custom files - examples provided below). The prompts are made by recursively expanding a special template string, replacing nonterminal "parts-of-speech" until no nonterminal terms remain in the string.

This includes 3 Nodes:
- *Lookup Table from File* - loads a YAML file "prompt" section (or of a whole folder of YAML's) into a JSON-ified dictionary (Lookups output)
- *Lookups Entry from Prompt* - places a single entry in a new Lookups output under the specified heading
- *Prompt from Lookup Table* - uses a Collection of Lookups as grammar rules from which to randomly generate prompts.--------------------------------
### GPT2RandomPromptMaker

**Description:** A node for app utilizes the GPT-2 language model to generate random prompts based on a provided seed and context.--------------------------------
### Grid to Gif

**Description:** One node that turns a grid image into an image collection, one node that turns an image collection into a gif.

--------------------------------
### Halftone

**Description**: Halftone converts the source image to grayscale and then performs halftoning. CMYK Halftone converts the image to CMYK and applies a per-channel halftoning to make the source image look like a magazine or newspaper. For both nodes, you can specify angles and halftone dot spacing.

--------------------------------

### Hand Refiner with MeshGraphormer

**Description**: Hand Refiner takes in your image and automatically generates a fixed depth map for the hands along with a mask of the hands region that will conveniently allow you to use them along with ControlNet to fix the wonky hands generated by Stable Diffusion--------------------------------

### Image and Mask Composition Pack

**Description:** This is a pack of nodes for composing masks and images, including a simple text mask creator and both image and latent offset nodes. The offsets wrap around, so these can be used in conjunction with the Seamless node to progressively generate centered on different parts of the seamless tiling.

This includes 15 Nodes:

- *Adjust Image Hue Plus* - Rotate the hue of an image in one of several different color spaces.
- *Blend Latents/Noise (Masked)* - Use a mask to blend part of one latents tensor [including Noise outputs] into another. Can be used to "renoise" sections during a multi-stage [masked] denoising process.
- *Enhance Image* - Boost or reduce color saturation, contrast, brightness, sharpness, or invert colors of any image at any stage with this simple wrapper for pillow [PIL]'s ImageEnhance module.
- *Equivalent Achromatic Lightness* - Calculates image lightness accounting for Helmholtz-Kohlrausch effect based on a method described by High, Green, and Nussbaum (2023).
- *Text to Mask (Clipseg)* - Input a prompt and an image to generate a mask representing areas of the image matched by the prompt.
- *Text to Mask Advanced (Clipseg)* - Output up to four prompt masks combined with logical "and", logical "or", or as separate channels of an RGBA image.
- *Image Layer Blend* - Perform a layered blend of two images using alpha compositing. Opacity of top layer is selectable, with optional mask and several different blend modes/color spaces.
- *Image Compositor* - Take a subject from an image with a flat backdrop and layer it on another image using a chroma key or flood select background removal.
- *Image Dilate or Erode* - Dilate or expand a mask (or any image!). This is equivalent to an expand/contract operation.
- *Image Value Thresholds* - Clip an image to pure black/white beyond specified thresholds.
- *Offset Latents* - Offset a latents tensor in the vertical and/or horizontal dimensions, wrapping it around.
- *Offset Image* - Offset an image in the vertical and/or horizontal dimensions, wrapping it around.
- *Rotate/Flip Image* - Rotate an image in degrees clockwise/counterclockwise about its center, optionally resizing the image boundaries to fit, or flipping it about the vertical and/or horizontal axes.
- *Shadows/Highlights/Midtones* - Extract three masks (with adjustable hard or soft thresholds) representing shadows, midtones, and highlights regions of an image.
- *Text Mask (simple 2D)* - create and position a white on black (or black on white) line of text using any font locally available to Aittor.--------------------------------
### Image Dominant Color

Description: Identifies and extracts the dominant color from an image using k-means clustering.--------------------------------
### Image to Character Art Image Nodes

**Description:** Group of nodes to convert an input image into ascii/unicode art Image--------------------------------

### Image Picker

**Description:** This app node takes in a collection of images and randomly chooses one. This can be useful when you have a number of poses to choose from for a ControlNet node, or a number of input images for another purpose.--------------------------------
### Image Resize Plus

Description: Provides various image resizing options such as fill, stretch, fit, center, and crop.--------------------------------
### Latent Upscale

**Description:** This node uses a small (~2.4mb) model to upscale the latents used in a Stable Diffusion 1.5 or Stable Diffusion XL image generation, rather than the typical interpolation method, avoiding the traditional downsides of the latent upscale technique.--------------------------------
### Load Video Frame

**Description:** This is a video frame image provider + indexer/video creation nodes for hooking up to iterators and ranges and ControlNets and such for app node experimentation. Think animation + ControlNet outputs.

**Node Link:** https://github.com/helix4u/load_video_frame

**Output Example:** 
<img src="https://raw.githubusercontent.com/helix4u/load_video_frame/refs/heads/main/_git_assets/dance1736978273.gif" width="500" />

--------------------------------
### Make 3D

**Description:** Create compelling 3D stereo images from 2D originals.--------------------------------
### Mask Operations

Description: Offers logical operations (OR, SUB, AND) for combining and manipulating image masks.--------------------------------
### Match Histogram

**Description:** An app node to match a histogram from one image to another.  This is a bit like the `color correct` node in the main app but this works in the YCbCr colourspace and can handle images of different sizes. Also does not require a mask input.
- Option to only transfer luminance channel.
- Option to save output as grayscale

A good use case for this node is to normalize the colors of an image that has been through the tiled scaling workflow of my XYGrid Nodes. 

See full docs here: https://github.com/skunkworxdark/Prompt-tools-nodes/edit/main/README.md

**Node Link:** https://github.com/skunkworxdark/match_histogram

**Output Examples** 

<img src="https://github.com/skunkworxdark/match_histogram/assets/21961335/ed12f329-a0ef-444a-9bae-129ed60d6097" />

--------------------------------
### Metadata Linked Nodes

**Description:** A set of nodes for Metadata. Collect Metadata from within an `iterate` node & extract metadata from an image.

- `Metadata Item Linked` - Allows collecting of metadata while within an iterate node with no need for a collect node or conversion to metadata node
- `Metadata From Image` - Provides Metadata from an image
- `Metadata To String` - Extracts a String value of a label from metadata
- `Metadata To Integer` - Extracts an Integer value of a label from metadata
- `Metadata To Float` - Extracts a Float value of a label from metadata
- `Metadata To Scheduler` - Extracts a Scheduler value of a label from metadata
- `Metadata To Bool` - Extracts Bool types from metadata
- `Metadata To Model` - Extracts model types from metadata
- `Metadata To SDXL Model` - Extracts SDXL model types from metadata
- `Metadata To LoRAs` - Extracts Loras from metadata. 
- `Metadata To SDXL LoRAs` - Extracts SDXL Loras from metadata
- `Metadata To ControlNets` - Extracts ControNets from metadata
- `Metadata To IP-Adapters` - Extracts IP-Adapters from metadata
- `Metadata To T2I-Adapters` - Extracts T2I-Adapters from metadata
- `Denoise Latents + Metadata` - This is an inherited version of the existing `Denoise Latents` node but with a metadata input and output. --------------------------------
### Negative Image

Description: Creates a negative version of an image, effective for visual effects and mask inversion.--------------------------------
### Nightmare Promptgen

**Description:** Nightmare Prompt Generator - Uses a local text generation model to create unique imaginative (but usually nightmarish) prompts for app. By default, it allows you to choose from some gpt-neo models I finetuned on over 2500 of my own app prompts in Compel format, but you're able to add your own, as well. Offers support for replacing any troublesome words with a random choice from list you can also define.--------------------------------
### Ollama Node

**Description:** Uses Ollama API to expand text prompts for text-to-image generation using local LLMs. Works great for expanding basic prompts into detailed natural language prompts for Flux. Also provides a toggle to unload the LLM model immediately after expanding, to free up VRAM for Aittor to continue the image generation workflow.

**Node Link:** https://github.com/Jonseed/Ollama-Node

**Example Node Graph:**  https://github.com/Jonseed/Ollama-Node/blob/main/Ollama-Node-Flux-example.json

**View:** 

![ollama node](https://raw.githubusercontent.com/Jonseed/Ollama-Node/a3e7cdc55e394cb89c1ea7ed54e106c212c85e8c/ollama-node-screenshot.png)

--------------------------------
### One Button Prompt

<img src="https://raw.githubusercontent.com/AIrjen/OneButtonPrompt_X_AittorAI/refs/heads/main/images/background.png" width="800" />

**Description:** an extensive suite of auto prompt generation and prompt helper nodes based on extensive logic. Get creative with the best prompt generator in the world. 

The main node generates interesting prompts based on a set of parameters. There are also some additional nodes such as Auto Negative Prompt, One Button Artify, Create Prompt Variant and other cool prompt toys to play around with.

**Node Link:** [https://github.com/AIrjen/OneButtonPrompt_X_AittorAI](https://github.com/AIrjen/OneButtonPrompt_X_AittorAI)

**Nodes:**

<img src="https://raw.githubusercontent.com/AIrjen/OneButtonPrompt_X_AittorAI/refs/heads/main/images/OBP_nodes_app.png" width="800" />

--------------------------------
### Oobabooga

**Description:** asks a local LLM running in Oobabooga's Text-Generation-Webui to write a prompt based on the user input.**Requirement**

a Text-Generation-Webui instance (might work remotely too, but I never tried it) and obviously app 3.x

**Note**

This node works best with SDXL models, especially as the style can be described independently of the LLM's output.

--------------------------------
### Prompt Tools 

**Description:** A set of app nodes that add general prompt (string) manipulation tools.  Designed to accompany the `Prompts From File` node and other prompt generation nodes.

1. `Prompt To File` - saves a prompt or collection of prompts to a file. one per line. There is an append/overwrite option.
2. `PTFields Collect` - Converts image generation fields into a Json format string that can be passed to Prompt to file. 
3. `PTFields Expand` - Takes Json string and converts it to individual generation parameters. This can be fed from the Prompts to file node.
4. `Prompt Strength` - Formats prompt with strength like the weighted format of compel 
5. `Prompt Strength Combine` - Combines weighted prompts for .and()/.blend()
6. `CSV To Index String` - Gets a string from a CSV by index. Includes a Random index option

The following Nodes are now included in v3.2 of Aittor and are no longer in this set of tools.<br>
- `Prompt Join` -> `String Join`
- `Prompt Join Three` -> `String Join Three`
- `Prompt Replace` -> `String Replace`
- `Prompt Split Neg` -> `String Split Neg`


See full docs here: https://github.com/skunkworxdark/Prompt-tools-nodes/edit/main/README.md

**Node Link:** https://github.com/skunkworxdark/Prompt-tools-nodes

**Workflow Examples** 

<img src="https://raw.githubusercontent.com/skunkworxdark/prompt-tools/refs/heads/main/images/CSVToIndexStringNode.png"/>

--------------------------------
### Remote Image

**Description:** This is a pack of nodes to interoperate with other services, be they public websites or bespoke local servers. The pack consists of these nodes:

- *Load Remote Image* - Lets you load remote images such as a realtime webcam image, an image of the day, or dynamically created images.
- *Post Image to Remote Server* - Lets you upload an image to a remote server using an HTTP POST request, eg for storage, display or further processing.--------------------------------

### BriaAI Remove Background

**Description**: Implements one click background removal with BriaAI's new version 1.4 model which seems to be producing better results than any other previous background removal tool.--------------------------------
### Remove Background

Description: An integration of the rembg package to remove backgrounds from images using multiple U2NET models.--------------------------------
### Retroize

**Description:** Retroize is a collection of nodes for app to "Retroize" images. Any image can be given a fresh coat of retro paint with these nodes, either from your gallery or from within the graph itself. It includes nodes to pixelize, quantize, palettize, and ditherize images; as well as to retrieve palettes from existing images.--------------------------------
### Simple Skin Detection

Description: Detects skin in images based on predefined color thresholds.--------------------------------
### Size Stepper Nodes

**Description:** This is a set of nodes for calculating the necessary size increments for doing upscaling workflows. Use the *Final Size & Orientation* node to enter your full size dimensions and orientation (portrait/landscape/random), then plug that and your initial generation dimensions into the *Ideal Size Stepper* and get 1, 2, or 3 intermediate pairs of dimensions for upscaling. Note this does not output the initial size or full size dimensions: the 1, 2, or 3 outputs of this node are only the intermediate sizes.

A third node is included, *Random Switch (Integers)*, which is just a generic version of Final Size with no orientation selection.--------------------------------
### Text font to Image

**Description:** text font to text image node for app, download a font to use (or if in font cache uses it from there), the text is always resized to the image size, but can control that with padding, optional 2nd line--------------------------------
### Thresholding

**Description:** This node generates masks for highlights, midtones, and shadows given an input image. You can optionally specify a blur for the lookup table used in making those masks from the source image.--------------------------------
### Unsharp Mask

**Description:** Applies an unsharp mask filter to an image, preserving its alpha channel in the process.--------------------------------
### XY Image to Grid and Images to Grids nodes

**Description:** These nodes add the following to AI:
- Generate grids of images from multiple input images
- Create XY grid images with labels from parameters
- Split images into overlapping tiles for processing (for super-resolution workflows)
- Recombine image tiles into a single output image blending the seams 

The nodes include:
1. `Images To Grids` - Combine multiple images into a grid of images
2. `XYImage To Grid` - Take X & Y params and creates a labeled image grid.
3. `XYImage Tiles` - Super-resolution (embiggen) style tiled resizing
4. `Image Tot XYImages` - Takes an image and cuts it up into a number of columns and rows.
5. Multiple supporting nodes - Helper nodes for data wrangling and building `XYImage` collections

See full docs here: https://github.com/skunkworxdark/XYGrid_nodes/edit/main/README.md

**Node Link:** https://github.com/skunkworxdark/XYGrid_nodes

**Output Examples** 

<img src="https://raw.githubusercontent.com/skunkworxdark/XYGrid_nodes/refs/heads/main/images/collage.png" />


--------------------------------
### Example Node Template

**Description:** This node allows you to do super cool things with AI.