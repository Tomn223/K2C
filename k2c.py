import os
import json

x = {"test": [{"hi": "bruh"}]}

coco_labels_file = open(os.path.join(os.getcwd(), "coco_dataset\labels.json"), "w")

json.dump(x, coco_labels_file)

coco_labels_file.close()