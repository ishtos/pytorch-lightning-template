#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   ishtos_transforms.py
@Time    :   2022/07/04 14:14:15
@Author  :   ishtos
@Version :   1.0
@License :   (C)Copyright 2022 ishtos
"""

import albumentations as A
from albumentations.pytorch import ToTensorV2

IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)


def get_train_transforms_v1(config, pretrained):
    augmentations = [A.Resize(config.height, config.width)]
    if pretrained:
        augmentations.append(A.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD))
    else:
        augmentations.append(A.Normalize(mean=0, std=1))
    augmentations.append(ToTensorV2())
    return A.Compose(augmentations)


def get_valid_transforms_v1(config, pretrained):
    augmentations = [A.Resize(config.height, config.width)]
    if pretrained:
        augmentations.append(A.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD))
    else:
        augmentations.append(A.Normalize(mean=0, std=1))
    augmentations.append(ToTensorV2())
    return A.Compose(augmentations)


# --------------------------------------------------
# getter
# --------------------------------------------------
def get_transforms(config, phase):
    if phase == "train":
        return eval(f"get_train_transforms_{config.transforms.train_version}")(
            config.transforms.params,
            config.model.params.pretrained,
        )
    elif phase in ["valid", "test"]:
        return eval(f"get_valid_transforms_{config.transforms.valid_version}")(
            config.transforms.params,
            config.model.params.pretrained,
        )
    else:
        raise ValueError(f"Not supported transforms phase: {phase}.")


if __name__ == "__main__":
    from utils.loader import load_config

    config = load_config("config.yaml")

    train_transform = get_transforms(config, "train")
    valid_transform = get_transforms(config, "valid")

    assert isinstance(train_transform, A.Compose)
    assert isinstance(valid_transform, A.Compose)
