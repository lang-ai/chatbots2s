# Chatbot_s2s
Code and Configuration for **[Bringing self-attention architectures into real world scenarios](https://drive.google.com/open?id=1eROR13rDH14sMkT2bE9t_piL12uelz0T)**.

## Introduction

Under the umbrella of self-attentional networks, many papers claiming to have advanced the SotA of
NLP-related tasks have been recently presented. In
this paper we validate the performance of this architecture when applied to a real enterprise scenario:
a customer service chatbot. The rationale is to test whether the differences between research and
enterprise scenarios, its specific challenges and its impact on performance may limit the application
scope of these novel proposals. 

## Dataset

For the experimentation in a real enterprise scenario, the [Customer Support on Twitter dataset](https://www.kaggle.com/thoughtvector/customer-support-on-twitter/home) has been used. The dataset contains 794,299 question-answer pairs in Twitter related to customer service support from different companies.

![](https://i.imgur.com/nTv3Iuu.png)

_(Extracted from https://www.kaggle.com/thoughtvector/customer-support-on-twitter/home)_

The [preprocess.py script](data_preprocessing/preprocess.py) has been applied to process and clean the dataset and to create the training, validation and testing files. Additionaly, the [prepare_data.sh script](data_preprocessing/prepare_data.sh) creates the files needed by sockeye to train the models.

## Models

The [Sockeye toolkit](https://github.com/awslabs/sockeye/) has been used for building and training the systems, as well as for evaluating the experimental results. In particular, the following models, implemented in Sockeye, has been tested.

- **CNN:** CNNs are expected to better capture semantic relationships between different parts of the text, such as long range dependencies. 

- **RNN:** RNNs rely on the use of additional information from previous steps for generating an output, which makes it a highly suitable architecture for sequential problems, such as textual representation.

- **Transformer:** This model is an implementation of the idea of self-attentional networks, replacing
recurrent or convolutional layers for building the encoder-decoder. These self-attention layers connect all the tokens in
the instance. Additionally, the attention layers are divided in sub-layers, each one of
them representing a (learned) linear projection of the inputs, in a smaller dimension. This mechanism allows the model
to pay attention to information from different sub-spaces of the input space.


## Evaluation

The following table summarizes the results of the different models.

| System      	| BLEU  	| CHRF  	| Rouge-1 	| Rouge-2 	| Rouge-L 	|
|-------------	|-------	|-------	|---------	|---------	|---------	|
| **RNN_S2S**     	| 0.064 	| 0.250 	| 0.223   	| 0.074   	| 0.179   	|
| **CNN_S2S**     	| _0.073_ 	| 0.255 	| _0.229_   	| _0.081_   	| _0.187_   	|
| **Transformer** 	| 0.071 	| _0.258_ 	| 0.226   	| 0.079   	| 0.184   	|

### Examples
