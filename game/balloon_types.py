from utils.textures import load_texture

BALLOON_TYPES = {
    '1': {"speed": 100, "health": 1, "texture_path": "assets/img/balloons/red.png"},
    '2': {"speed": 150, "health": 3, "texture_path": "assets/img/balloons/purble.png"},
    '3': {"speed": 80, "health": 5, "texture_path": "assets/img/balloons/green.png"},
    '4': {"speed": 120, "health": 10, "texture_path": "assets/img/balloons/boss.png"},
    '5': {"speed": 80, "health": 5, "texture_path": "assets/img/balloons/green.png"},
    '6': {"speed": 80, "health": 5, "texture_path": "assets/img/balloons/green.png"},
    # Adicione mais tipos com diferentes texturas se desejar
}

def load_balloon_textures():
    for btype, props in BALLOON_TYPES.items():
        texture_id, w, h = load_texture(props["texture_path"])
        props["texture_id"] = texture_id
        props["width"] = w
        props["height"] = h
