import json

from PIL import Image, ImageFont
from pydantic import BaseModel

u32 = int
f32 = float


class BaseConfig(BaseModel):
    name: str
    filename: str


class OverlayConfig(BaseConfig):
    coords: tuple[u32, u32]
    resize: tuple[u32, u32]
    input_size: u32


class TextDrawConfig(BaseConfig):
    mids: list[tuple[u32, u32]]
    color: tuple[u32, u32, u32]
    scale: tuple[f32, f32]
    max_width: int


class Config(BaseModel):
    textdraws: list[TextDrawConfig]
    overlays: list[OverlayConfig]


def load(filename: str):
    with open(filename) as f:
        data = json.load(f)
    return data


overlays = load("config/image_overlays.json")
textdraws = load("config/image_textdraws.json")

full_config = Config(
    textdraws=textdraws,
    overlays=overlays,
)


ImageFont.truetype("config/font.ttf")
for config in [*full_config.overlays, *full_config.textdraws]:
    Image.open(config.filename)
