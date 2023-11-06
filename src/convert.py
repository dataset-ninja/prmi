# https://zenodo.org/record/5974905#.YlAJtn9Bzmg

import os
import shutil
from urllib.parse import unquote, urlparse

import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from dataset_tools.convert import unpack_if_archive
from dotenv import load_dotenv
from supervisely.io.fs import (
    file_exists,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from tqdm import tqdm

import src.settings as s

def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count
    
def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:

    # project_name = "diverse plant root"
    dataset_path = "/home/grokhi/rawdata/prmi/PRMI_official"
    batch_size = 30

    images_folder_name = "images"
    masks_folder_name = "masks_pixel_gt"
    masks_prefix = "GT_"
    masks_ext = ".png"

    def create_ann(image_path):
        labels = []

        mask_name = masks_prefix + get_file_name(image_path) + masks_ext
        mask_path = os.path.join(masks_path, mask_name)
        if file_exists(mask_path):
            mask_np = sly.imaging.image.read(mask_path)[:, :, 0]
            img_height = mask_np.shape[0]
            img_wight = mask_np.shape[1]
            mask = mask_np == 255
            ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
            for i in range(1, ret):
                obj_mask = curr_mask == i
                curr_bitmap = sly.Bitmap(obj_mask)
                if curr_bitmap.area > 15:
                    curr_label = sly.Label(curr_bitmap, obj_class)
                    labels.append(curr_label)

        tag_species_name = get_file_name(image_path).split("_")[0].lower()
        tags = [sly.Tag(tag_meta) for tag_meta in tag_metas if tag_meta.name == tag_species_name]
        
        tag_has_root_val = 'true' if len(labels)> 0 else 'false'
        tag_location_val = get_file_name(image_path).split("_")[5]
        tag_tube_num_val = get_file_name(image_path).split("_")[1]
        tag_date_val = get_file_name(image_path).split("_")[3]
        tag_depth_val = get_file_name(image_path).split("_")[2]
        tag_dpi_val = int(get_file_name(image_path).split("_")[6][3:])

        tgs = [tag_has_root, tag_location, tag_tube_num, tag_date, tag_depth, tag_dpi]
        tgs_val = [tag_has_root_val, tag_location_val, tag_tube_num_val, tag_date_val, tag_depth_val, tag_dpi_val]

        tags += [sly.Tag(tag, value=val) for tag, val in zip(tgs, tgs_val)]

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)


    obj_class = sly.ObjClass("root", sly.Bitmap)
    tag_names = [
        "cotton",
        "papaya",
        "peanut",
        "sesame",
        "sunflower",
        "switchgrass",        
    ]
    tag_has_root = sly.TagMeta("has_root", sly.TagValueType.ONEOF_STRING, possible_values=["true", "false"])
    tag_location = sly.TagMeta("location", sly.TagValueType.ANY_STRING)
    tag_tube_num = sly.TagMeta("tube_num", sly.TagValueType.ANY_STRING)
    tag_date = sly.TagMeta("date", sly.TagValueType.ANY_STRING)
    tag_depth = sly.TagMeta("depth", sly.TagValueType.ANY_STRING)
    tag_dpi = sly.TagMeta("DPI", sly.TagValueType.ANY_NUMBER)
    tag_metas = [sly.TagMeta(name, sly.TagValueType.NONE) for name in tag_names] + [tag_has_root, tag_location, tag_tube_num, tag_date, tag_depth, tag_dpi]


    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class],tag_metas=tag_metas)
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in os.listdir(dataset_path):
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        curr_images_data = os.path.join(dataset_path, ds_name, images_folder_name)

        for curr_subfolder in os.listdir(curr_images_data):
            images_path = os.path.join(curr_images_data, curr_subfolder)
            masks_path = os.path.join(dataset_path, ds_name, masks_folder_name, curr_subfolder)
            images_names = os.listdir(images_path)

            progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

            for img_names_batch in sly.batched(images_names, batch_size=batch_size):
                images_pathes_batch = [
                    os.path.join(images_path, image_name) for image_name in img_names_batch
                ]

                img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]

                if curr_subfolder != "Switchgrass_720x510_DPI300_noMask":
                    anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]
                    api.annotation.upload_anns(img_ids, anns_batch)

                progress.iters_done_report(len(img_names_batch))
    return project


