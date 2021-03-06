from enum import Enum


class Command(Enum):
    """
    ELRO Connects send commands copied from decompiled android app
    """
    SWITCH_TIMER = -34
    DELETE_EQUIPMENT_DETAIL = -4
    EQUIPMENT_CONTROL = 1
    INCREACE_EQUIPMENT = 2
    REPLACE_EQUIPMENT = 3
    DELETE_EQUIPMENT = 4
    MODIFY_EQUIPMENT_NAME = 5
    CHOOSE_SCENE_GROUP = 6
    CANCEL_INCREACE_EQUIPMENT = 7
    INCREACE_SCENE = 8
    MODIFY_SCENE = 9
    DELETE_SCENE = 10
    GET_DEVICE_NAME = 14
    GET_ALL_EQUIPMENT_STATUS = 15
    GET_ALL_SCENE_INFO = 18
    TIME_CHECK = 21
    INCREACE_SCENE_GROUP = 23
    MODIFY_SCENE_GROUP = 24
    SYN_DEVICE_STATUS = 29
    SYN_DEVICE_NAME = 30
    SYN_SCENE = 31
    SCENE_HANDLE = 32
    SCENE_GROUP_DELETE = 33
    MODEL_SWITCH_TIMER = 34
    MODEL_TIMER_SYN = 35
    UPLOAD_MODEL_TIMER = 36
    MODEL_TIMER_DEL = 37
    SEND_TIMEZONE = 251

    # ELRO Connects receive commands
    # Reverse engineered
    DEVICE_STATUS_UPDATE = 19
    DEVICE_ALARM_TRIGGER = 25
    SCENE_STATUS_UPDATE = 26
    DEVICE_NAME_REPLY = 17
