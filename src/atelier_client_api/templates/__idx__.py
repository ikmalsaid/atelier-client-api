<!DOCTYPE html>
<html>
<head>
    <title>Atelier Client API Docs</title>
    <style>
        @import url('https://db.onlinewebfonts.com/c/91365a119c448bf9da6d8f710e3bdda6?family=Nokia+Sans+S60+Regular');

        @font-face {
            font-family: "Nokia Sans S60 Regular";
            src: url('https://db.onlinewebfonts.com/c/91365a119c448bf9da6d8f710e3bdda6?family=Nokia+Sans+S60+Regular') format('woff2');
        }

        * {
            font-family: "Nokia Sans S60 Regular";
            color: #ffffff;
        }

        body {
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #000000;
            background-image: linear-gradient(45deg, #111111 25%, #000000 25%, #000000 50%, #111111 50%, #111111 75%, #000000 75%, #000000 100%);
            background-size: 40px 40px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: rgba(20, 20, 20, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }

        th, td {
            border: 1px solid #333;
            padding: 12px;
            text-align: left;
        }

        th {
            background-color: #1a1a1a;
            background-image: linear-gradient(180deg, #2a2a2a, #1a1a1a);
        }

        tr:nth-child(even) {
            background-color: rgba(30, 30, 30, 0.7);
        }

        tr:nth-child(odd) {
            background-color: rgba(25, 25, 25, 0.7);
        }

        code {
            background-color: #333;
            padding: 2px 6px;
            border-radius: 3px;
            color: #fff;
            font-family: monospace;
        }

        ul {
            margin: 0;
            padding-left: 20px;
        }
    </style>
</head>
<body>
    <h2 style="font-size: 22px; text-align: center; margin-bottom: 10px;">Atelier Client API 1.0.0</h2>
    <p style="font-size: 14px; text-align: center; margin-top: 0;">Copyright (C) 2023-<script>document.write(new Date().getFullYear())</script> Ikmal Said. All rights reserved</p>
    <table>
        <tr>
            <th>POST Endpoints</th>
            <th>Description</th>
            <th>Parameters</th>
        </tr>
        <tr>
            <td>/v1/api/image/generate</td>
            <td>Generate images from text prompts</td>
            <td>
                <ul>
                    <li><code>prompt</code> (required): Text prompt</li>
                    <li><code>negative_prompt</code>: Negative prompt</li>
                    <li><code>model_name</code>: Model name (default: "flux-turbo")</li>
                    <li><code>image_size</code>: Size ratio (default: "1:1")</li>
                    <li><code>lora_svi</code>: LoRA SVI preset</li>
                    <li><code>lora_flux</code>: LoRA Flux preset</li>
                    <li><code>image_seed</code>: Generation seed</li>
                    <li><code>style_name</code>: Style preset</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/image/variation</td>
            <td>Create variations of existing images</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                    <li><code>prompt</code> (required): Text prompt</li>
                    <li><code>negative_prompt</code>: Negative prompt</li>
                    <li><code>model_name</code>: Model name (default: "flux-turbo")</li>
                    <li><code>image_size</code>: Size ratio (default: "1:1")</li>
                    <li><code>strength</code>: Variation strength</li>
                    <li><code>lora_svi</code>: LoRA SVI preset</li>
                    <li><code>lora_flux</code>: LoRA Flux preset</li>
                    <li><code>image_seed</code>: Generation seed</li>
                    <li><code>style_name</code>: Style preset</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/image/structure</td>
            <td>Apply structural guidance to images</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                    <li><code>prompt</code> (required): Text prompt</li>
                    <li><code>negative_prompt</code>: Negative prompt</li>
                    <li><code>model_name</code>: Model name (default: "svi-realistic")</li>
                    <li><code>image_size</code>: Size ratio (default: "1:1")</li>
                    <li><code>strength</code>: Guidance strength</li>
                    <li><code>lora_svi</code>: LoRA SVI preset</li>
                    <li><code>image_seed</code>: Generation seed</li>
                    <li><code>style_name</code>: Style preset</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/image/facial</td>
            <td>Apply facial guidance to images</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                    <li><code>prompt</code> (required): Text prompt</li>
                    <li><code>negative_prompt</code>: Negative prompt</li>
                    <li><code>model_name</code>: Model name (default: "svi-realistic")</li>
                    <li><code>image_size</code>: Size ratio (default: "1:1")</li>
                    <li><code>strength</code>: Guidance strength</li>
                    <li><code>lora_svi</code>: LoRA SVI preset</li>
                    <li><code>image_seed</code>: Generation seed</li>
                    <li><code>style_name</code>: Style preset</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/image/style</td>
            <td>Apply style guidance to images</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                    <li><code>prompt</code> (required): Text prompt</li>
                    <li><code>negative_prompt</code>: Negative prompt</li>
                    <li><code>model_name</code>: Model name (default: "svi-realistic")</li>
                    <li><code>image_size</code>: Size ratio (default: "1:1")</li>
                    <li><code>strength</code>: Style strength</li>
                    <li><code>lora_svi</code>: LoRA SVI preset</li>
                    <li><code>image_seed</code>: Generation seed</li>
                    <li><code>style_name</code>: Style preset</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/image/outpaint</td>
            <td>Extend images beyond their borders</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                    <li><code>image_size</code>: Size ratio (default: "16:9")</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/image/consistency</td>
            <td>Generate consistent images with face and style references</td>
            <td>
                <ul>
                    <li><code>prompt</code> (required): Text prompt</li>
                    <li><code>face_image</code> (required): Face reference</li>
                    <li><code>style_image</code> (required): Style reference</li>
                    <li><code>negative_prompt</code>: Negative prompt</li>
                    <li><code>image_size</code>: Size ratio (default: "1:1")</li>
                    <li><code>face_strength</code>: Face consistency (default: 1.2)</li>
                    <li><code>style_strength</code>: Style strength (default: 0.7)</li>
                    <li><code>image_seed</code>: Generation seed</li>
                    <li><code>style_name</code>: Style preset</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/face/identity</td>
            <td>Generate images with face identity preservation</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Face reference</li>
                    <li><code>prompt</code> (required): Text prompt</li>
                    <li><code>negative_prompt</code>: Negative prompt</li>
                    <li><code>image_size</code>: Size ratio (default: "1:1")</li>
                    <li><code>strength</code>: Face strength (default: 1.0)</li>
                    <li><code>image_seed</code>: Generation seed</li>
                    <li><code>style_name</code>: Style preset</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/realtime/canvas</td>
            <td>Real-time canvas processing</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                    <li><code>prompt</code> (required): Text prompt</li>
                    <li><code>negative_prompt</code>: Negative prompt</li>
                    <li><code>lora_rt</code>: LoRA RT preset</li>
                    <li><code>strength</code>: Creativity level (default: 0.9)</li>
                    <li><code>image_seed</code>: Generation seed</li>
                    <li><code>style_name</code>: Style preset</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/realtime/generate</td>
            <td>Real-time image generation</td>
            <td>
                <ul>
                    <li><code>prompt</code> (required): Text prompt</li>
                    <li><code>negative_prompt</code>: Negative prompt</li>
                    <li><code>image_size</code>: Size ratio (default: "1:1")</li>
                    <li><code>lora_rt</code>: LoRA RT preset</li>
                    <li><code>image_seed</code>: Generation seed</li>
                    <li><code>style_name</code>: Style preset</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/image/inpaint</td>
            <td>Fill masked areas in images</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                    <li><code>mask</code> (required): Mask image</li>
                    <li><code>prompt</code> (required): Text prompt</li>
                    <li><code>negative_prompt</code>: Negative prompt</li>
                    <li><code>strength</code>: Inpainting strength (default: 0.5)</li>
                    <li><code>cfg</code>: Prompt scale (default: 9.0)</li>
                    <li><code>style_name</code>: Style preset</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/image/erase</td>
            <td>Remove content from masked areas</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                    <li><code>mask</code> (required): Mask image</li>
                    <li><code>cfg</code>: Prompt scale (default: 9.0)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/image/enhance</td>
            <td>Enhance image quality</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                    <li><code>prompt</code>: Text prompt</li>
                    <li><code>negative_prompt</code>: Negative prompt</li>
                    <li><code>creativity</code>: Creativity level (default: 0.3)</li>
                    <li><code>resemblance</code>: Resemblance level (default: 1)</li>
                    <li><code>hdr</code>: HDR strength (default: 0)</li>
                    <li><code>style_name</code>: Style preset</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/image/controlnet</td>
            <td>Apply ControlNet guidance</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                    <li><code>prompt</code> (required): Text prompt</li>
                    <li><code>negative_prompt</code>: Negative prompt</li>
                    <li><code>model_name</code>: Model name (default: "sd-toon")</li>
                    <li><code>controlnet</code>: Control type (default: "scribble")</li>
                    <li><code>strength</code>: Control strength (default: 70)</li>
                    <li><code>cfg</code>: Prompt scale (default: 9.0)</li>
                    <li><code>image_seed</code>: Generation seed</li>
                    <li><code>style_name</code>: Style preset</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/face/gfpgan</td>
            <td>Face restoration using GFPGAN</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                    <li><code>model_version</code>: Model version (default: "1.3")</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/face/codeformer</td>
            <td>Face restoration using CodeFormer</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/image/upscale</td>
            <td>Upscale image resolution</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/image/bgremove</td>
            <td>Remove image background</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/image/caption</td>
            <td>Generate image captions</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>/v1/api/image/prompt</td>
            <td>Generate prompts from images</td>
            <td>
                <ul>
                    <li><code>image</code> (required): Source image</li>
                </ul>
            </td>
        </tr>
    </table>
</body>
</html> 