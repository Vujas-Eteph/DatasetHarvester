"""
------------------------------------------------------------
Goal: Create annotation first only folders
Quick Use: python annotation_first_only.py
------------------------------------------------------------
"""

# - IMPORTS ---
import os
from utils.utils import read_yaml
import json
from PIL import Image
import numpy as np


# - FUNCTIONS ---
def read_json(json_loc):
    with open(json_loc) as f:
        return json.load(f)


# - CONSTANTES ---
# !TODO: Change the constance and use a yaml config file instead
dataset_name = "LVOS_2"
extension = ".png"


# - MAIN ---
def main():
    yaml_config = read_yaml("config.yaml")

    dataset_location = os.path.join(yaml_config["destination"], dataset_name)
    all_subset = [subset for subset in os.listdir(dataset_location) if
                  os.path.isdir(os.path.join(dataset_location, subset))]

    # List all sequences in the subset
    for subset in all_subset:
        if subset != 'valid':
            continue

        all_sequences = os.listdir(os.path.join(dataset_location, subset,
                                                "Annotations"))
        meta_subset = read_json(os.path.join(dataset_location, subset,
                                             f"{subset}_meta.json")).get('videos')

        for sequence_name in all_sequences:
            os.makedirs(os.path.join(dataset_location, subset, "Annotations_first_only",
                                     sequence_name), exist_ok=True)
            meta_seq = meta_subset.get(sequence_name)

            prev_fdx = None
            for obj, meta_obj in (meta_seq.get('objects').items()):
                fdx_start = meta_obj.get('frame_range').get('start')

                # Will proceed only if the current frame idx is seen for the first 
                # time, or if another object appears somewhere later in the sequence
                if prev_fdx == fdx_start:
                    continue

                # Re-construct current path to annotation
                anno_loc_root = os.path.join(dataset_location, subset, "Annotations",
                                             sequence_name, f"{fdx_start}{extension}")
                anno_loc_dest = os.path.join(dataset_location, subset, "Annotations_first_only",
                                             sequence_name, f"{fdx_start}{extension}")

                first_mask_frame = Image.open(anno_loc_root)
                # Remove the object indixes of the objects that I have been
                # listed as present before the current observed obj
                if int(obj) > 1:
                    color_palette = first_mask_frame.getpalette()
                    first_mask_frame_to_adapt = np.array(first_mask_frame)

                    # Replace all obj indexs below int(obj) by the background id, i.e., 0.
                    # convert to a palette image
                    # and reapply the palette from the original image to maintain the same color mapping
                    first_mask_frame_to_adapt[first_mask_frame_to_adapt < int(obj)] = 0
                    first_mask_frame = Image.fromarray(first_mask_frame_to_adapt, mode='P')
                    first_mask_frame.putpalette(color_palette)

                first_mask_frame.save(anno_loc_dest)

                prev_fdx = fdx_start


if __name__ == '__main__':
    main()
