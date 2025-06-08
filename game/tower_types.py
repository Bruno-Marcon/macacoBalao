from utils.textures import load_texture

TOWER_TYPES = {
    "vasco": {
        "texture_path": "assets/img/monkeys/vasco.png",
        "range": 150,
        "cooldown": 1.0,
        "cost": 25
    },
    "botafogo": {
        "texture_path": "assets/img/monkeys/botafogo.png",
        "range": 150,
        "cooldown": 0.5,
        "cost": 35
    },
    "flamengo": {
        "texture_path": "assets/img/monkeys/flamengo.png",
        "range": 300,
        "cooldown": 2.0,
        "cost": 40
    }
}

def load_tower_textures():
    for tower_id, props in TOWER_TYPES.items():
        texture_id, w, h = load_texture(props["texture_path"])
        props["texture_id"] = texture_id
        props["width"] = w
        props["height"] = h
