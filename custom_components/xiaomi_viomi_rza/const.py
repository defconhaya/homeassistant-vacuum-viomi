"""Constants for Xiaomi Viomi integration."""

DOMAIN = "xiaomi_viomi_rza"
CONF_DEVICE = "device"
CONF_MODEL = "model"
CONF_MAC = "mac"
CONF_FLOW_TYPE = "config_flow_device"

MODELS_VACUUM = ["viomi.vacuum.v8"]

DEVICE_PROPERTIES = [
    "battery",
    "bin_type",
    "charging",
    "clean_area",
    "clean_time",
    "current_map_id",
    "edge_state",
    "error",
    "error_code",
    "fanspeed",
    "has_map",
    "has_new_map",
    "hw_info",
    "is_on",
    "light_state",
    "map_number",
    "mop_installed",
    "mop_mode",
    "mop_route",
    "remember_map",
    "repeat_cleaning",
    "sound_volume",
    "state",
    "water_grade"
    # "is_charge",
    # "is_mop",
    # "is_work",
    # "light_state",
    # "map_num",
    # # "mode",
    # "mop_route",
    # "mop_type",
    # "remember_map",
    # "repeat_state",
    # "run_state",
    # "s_area",
    # "s_time",
    # "suction_grade",
    # "v_state",
    # "water_grade",
    # "order_time",
    # "start_time",
    # "water_percent",
    # "zone_data",
    # "sw_info",
    # "main_brush_hours",
    # "main_brush_life",
    # "side_brush_hours",
    # "side_brush_life",
    # "mop_hours",
    # "mop_life",
    # "hypa_hours",
    # "hypa_life",
]
