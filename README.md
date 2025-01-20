
# nanoGPT for Bai Li (李白) Poetry Generation
This repository is a cloned version of [nanoGPT](https://github.com/karpathy/nanoGPT), originally created by Andrej Karpathy. It serves as the foundation for a unique mini-project aimed at exploring the intersection of technology and literature by mimicking the poetic style of Bai Li, one of the most celebrated poets in Chinese history. The project seeks to demonstrate how state-of-the-art AI models can be adapted to generate culturally rich and stylistically authentic textual content.

For those unfamiliar, nanoGPT is a lightweight and efficient implementation of GPT, tailored for researchers and developers looking for a simpler way to experiment with generative language models. Its minimalistic design allows for customization and accessibility, even for those with limited computational resources. For more details about the nanoGPT project, its features, and its usage, please refer to the [original repository](https://github.com/karpathy/nanoGPT).

## Project Overview
In this mini-project, I used nanoGPT to create a model capable of generating poems in the style of the famous Chinese poet Bai Li (李白). Here are the steps I followed:

1. Data Collection: Wrote a script, `scrape_bai_li_poems.py`, to gather Bai Li’s poems from the internet and record in `input.txt` with correct encoding.
2. Data Preparation: Translated the collected poems into Traditional Chinese and performed data cleaning to ensure the text was consistent and usable for training.
3. Training Configuration: Initially, I used the original configuration parameters from `train_shakespeare_char.py`, but the output was not satisfactory due to mismatched dataset characteristics. For example, the original model used a batch size of 64 and a block size of 256, which were unsuitable for Bai Li’s larger dataset and longer sequences. I tuned the configuration in `train_bai_li_char.py`, reducing the batch size to 12, increasing the block size to 2048, and adjusting the model dimensions (e.g., reducing n_layer, n_head, and n_embd for faster convergence). These changes significantly improved the results, making the output align better with Bai Li’s poetic style.
Original Parameters' Output
````
秋》露姓縵

濯講七
村吮詩薔鴻積露漠滿紙夢伯墀
一違好宦袪蘿忘七
橘吊蒂武乘振
一咿淺講講

一咿 穴村七
一淺步防虛》
```
- Updated Parameters' Output
```
秋殿開徵客，千里看書一身當百戰，
山邊門道戒其如青箬笠如水腸中無辭煩憂。
霓裳曳裾王氣濃前舊水，高失香，桃紅旗十二十水偏逢四人駐顏色，幽。

無無限似儂入寒山中散發洛城頭，唯所歸去，對，前。
柴門前舊枕浮雲臺，唯所是與人畏
```
Training the Model: Ran the training script on the prepared dataset.
```
python train.py config/train_bai_li_char.py
```
Poem Generation: The results captured Bai Li’s poetic style with creative and unique variations. However, the format did not align perfectly with traditional Chinese poetic paradigms. Future work will focus on refining the model to better understand and adhere to the structure and style of classical poetry.
```
python sample.py --out_dir=out-bai-li-char --start="秋"
```
This project demonstrated nanoGPT’s ability to fine-tune models effectively on domain-specific datasets, even for a complex and artistic task like poetry generation. The final generated poems were both stylistically aligned with Bai Li’s work and imaginative in their own right.

## Acknowledgements
I would like to extend my gratitude to Andrej Karpathy for his incredible contribution to the open-source community. His work on nanoGPT has made it possible to embark on creative endeavors like this one, bridging the gap between cutting-edge technology and artistic expression. This project is a testament to the versatility and impact of his efforts in democratizing access to AI tools.
