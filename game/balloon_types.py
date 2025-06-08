from utils.textures import load_texture

BALLOON_TYPES = {
    '1': {"speed": 100, "health": 1, "texture_path": "assets/img/balloons/normal.png"},
    '2': {"speed": 150, "health": 3, "texture_path": "assets/img/balloons/normal2.png"},
    '3': {"speed": 80, "health": 5, "texture_path": "assets/img/balloons/gordo.png"},
    '4': {"speed": 110, "health": 10, "texture_path": "assets/img/balloons/boss2.png"},
    '5': {"speed": 70, "health": 50, "texture_path": "assets/img/balloons/fabao.png"}
}

def load_balloon_textures():
    for btype, props in BALLOON_TYPES.items():
        texture_id, w, h = load_texture(props["texture_path"])
        props["texture_id"] = texture_id
        props["width"] = w
        props["height"] = h
