# OptiGen_benchmark
OptiGen is a MultiGen complementary and computationally-free benchmark for text-to-image generation models. Its main objective is to test a T2I model in the worst condition possible for multi-categories generation.


## Follow the NoteBook instructions to test your model
Some cells contains the parameter of a OptiGen test. You can modify those parameter to test your model (if needed, use another pipeline than StableDiffusion to load your model).

## set_up_dataset.py
This is the code used to create the word dataset out of the prepared data from MultiGen.

## word_coco_obj_comp_5_1k.json
If you wish to add words to your OptiGen test, you can directly modify this json dataset by adding words at the end of the list.

## Aknowledgement :

This OptiGen dataset was created as a mean to test, with computationnaly cheap benchmark, the model introduced in *TOKENCOMPOSE: Text-to-Image Diffusion with Token-level Supervision* by Zirui Wang , Zhizhou Sha , Zheng Ding Yilin Wang and Zhuowen Tu (https://arxiv.org/pdf/2312.03626). 
I strongly advise you to read there paper and as mentionned in the notebook, OptiGen permit a first dive into multi-category generation efficiency. But to get more exhaustive results it would be interesting to compare it with MultiGen benchmark.
