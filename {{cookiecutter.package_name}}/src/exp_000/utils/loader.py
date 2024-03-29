#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   loader.py
@Time    :   2022/07/04 14:12:29
@Author  :   ishtos
@Version :   1.0
@License :   (C)Copyright 2022 ishtos
"""


from omegaconf import OmegaConf


def resolve_tuple(*args):
    return tuple(args)


OmegaConf.register_new_resolver("as_tuple", resolver=resolve_tuple)


def load_config(config_name="config.yml"):
    default_config = OmegaConf.load("./configs/default_config.yml")
    config = OmegaConf.load(f"./configs/{config_name}")
    config = OmegaConf.merge(default_config, config)

    return config
