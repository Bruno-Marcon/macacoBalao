from utils.textures import load_texture

TOWER_TYPES = {
    "basic": {
        "texture_path": "assets/img/monkeys/monkey1.png",
        "range": 150,
        "cooldown": 1.0,
        "cost": 25
    },
    "sniper": {
        "texture_path": "assets/img/monkeys/sniper.png",
        "range": 300,
        "cooldown": 2.0,
        "cost": 40
    }
}
#     "rapid": {
#         "texture_path": "assets/img/monkeys/monkey3.png",
#         "range": 120,
#         "cooldown": 0.4,
#         "cost": 30
#     }
# }

def load_tower_textures():
    for tower_id, props in TOWER_TYPES.items():
        texture_id, w, h = load_texture(props["texture_path"])
        props["texture_id"] = texture_id
        props["width"] = w
        props["height"] = h
