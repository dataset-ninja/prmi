**PRMI: A Dataset of Minirhizotron Images for Diverse Plant Root Study** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the agricultural industry. 

The dataset consists of 72567 images with 114676 labeled objects belonging to 1 single class (*root*).

Images in the PRMI dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 37052 (51% of the total) unlabeled images (i.e. without annotations). There are 3 splits in the dataset: *test* (14100 images), *train* (46682 images), and *val* (11785 images). Alternatively, the dataset could be split into 6 species: ***cotton*** (2412 images), ***papaya*** (546 images), ***peanut*** (36667 images), ***sesame*** (16506 images), ***sunflower*** (3900 images), and ***switchgrass*** (3912 images). Additionally, every image preserves information about its ***DPI***. The dataset was released in 2022 by the US-FR joint research group.

Here is the visualized example grid with animated annotations:

[animated grid](https://github.com/dataset-ninja/prmi/raw/main/visualizations/horizontal_grid.webm)
