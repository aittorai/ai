# IP-Adapter Model Formats

## CLIP Vision Models

CLIP Vision models are organized in `diffusers`` format. The expected directory structure is:

```bash
ip_adapter_sd_image_encoder/
├── config.json
└── model.safetensors
```

## IP-Adapter Models

IP-Adapter models are stored in a directory containing two files
- `image_encoder.txt`: A text file containing the model identifier for the CLIP Vision encoder that is intended to be used with this IP-Adapter model.
- `ip_adapter.bin`: The IP-Adapter weights.

Sample directory structure:
```bash
ip_adapter_sd15/
├── image_encoder.txt
└── ip_adapter.bin
```

### Why save the weights in a .safetensors file?

The weights in `ip_adapter.bin` are stored in a nested dict, which is not supported by `safetensors`. This could be solved by splitting `ip_adapter.bin` into multiple files, but for now we have decided to maintain consistency with the checkpoint structure used in the official [h94/IP-Adapter](https://huggingface.co/h94/IP-Adapter) repo.