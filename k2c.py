import os
import json

coco_labels = {
    "categories": [],
    "images": [],
    "annotations": []
}

categories = {} # name, category_id


for file_num, kitti_label_file in enumerate(os.listdir("./kitti_dataset/labels")):

    coco_labels["images"].append({
        "id": file_num,
        "license": 1,
        "file_name": kitti_label_file,
        "height": 0,  # TODO: get actual image h/w
        "width": 0
    })

    with open("./kitti_dataset/labels/" + kitti_label_file) as f:

        for line in f.readlines():
            katti_fields = line.split(" ")
            
            cat = katti_fields[0]
            x1, y1, x2, y2 = katti_fields[4:8]
            x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
            w, h = x2-x1, y2-y1

            if cat not in categories:
                categories[cat] = len(categories) + 1  # first id is 1
                coco_labels["categories"].append({
                    "id": categories[cat],
                    "name": cat,
                    "supercategory": "later"  # need another value in categories dict?
                })
            
            coco_labels["annotations"].append({
                "id": len(coco_labels["annotations"]) + 1,  # first id is 1
                "image_id": file_num,
                "category_id": categories[cat],
                "bbox": [x1, y1, w, h],
                "area": w*h
            })


coco_labels_file = open(os.path.join(os.getcwd(), "coco_dataset\labels.json"), "w")

json.dump(coco_labels, coco_labels_file, indent=2)

coco_labels_file.close()