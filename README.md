# y spam?
![Screenshot of the website before inputting text](https://github.com/yenn01/NLP_Front/assets/48972583/4f31eeab-98c7-43ca-b0a5-51e8066494bb)
A spam detection website built with a Svelte front-end and a Flask back-end to serve the prediction model as part of _TARUMT - BMCS2123 Natural Language Processing_ assignment to utilise Meta's [Open Pre-trained Transformers](https://github.com/facebookresearch/metaseq/tree/main/projects/OPT) to solve real world problems. 

To reduce user waiting time, `distilbert-base-uncased`, a smaller and faster BERT model  \(available [here](https://huggingface.co/distilbert-base-uncased)\), has been used to ensure fast tokenisation while having optimal accuracies.

Due to hardware limitations, `OPT-350M` was used for the final product.

Both Zero-Shot Learning and Few-Shot Learning was applied in this assignment where we used a test sentence: "Congratulation, you have won an iPhone 14. Click this link to claim." to test the accuracy of the model under different conditions. 

In our few-shot learning attempt, we had trained `OPT-350M` on 5574 rows of SMS spam messages \(available [here](https://huggingface.co/datasets/sms_spam)\).  

### Results from comparing Zero-Shot / Few Shot Learning
#### Zero-Shot Learning with 350M parameters
![53% Ham vs 46% Spam](https://github.com/yenn01/NLP_Front/assets/48972583/956b3a85-0c57-4871-be64-88f47535501f)
#### Few-Shot Learning with 350M parameters
![73% Spam vs 27% Ham](https://github.com/yenn01/NLP_Front/assets/48972583/f84dc482-ccc2-4e05-967e-bcaa58dd98ff)
#### Zero-Shot Learning with 1.3B parameters
![51% Spam vs 49% Ham](https://github.com/yenn01/NLP_Front/assets/48972583/99acd16a-c6e9-4490-9b8e-23d28d930c1f)

## Screenshots
![Screenshot of the website after inputting the text "You have won a free iPhone 14, Click the link below to claim it" with it scoring 66.39% as spam ](https://github.com/yenn01/NLP_Front/assets/48972583/48b36ec1-49cd-420b-8739-334be9b9a7b3)
![Screenshot of the website after inputting the text "This chicken rice is delicious, you should try it one day." with it scoring 53.78% as ham ](https://github.com/yenn01/NLP_Front/assets/48972583/511d2d97-d186-4ce0-9e3a-71738e9e8b04)


