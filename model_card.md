# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Scikit Learn Random Forest Classifier link: https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.RandomForestClassifier.html

>The model is a random forest classifier from scikit learn. It was trained for binary classification in determining if an individual earns more than 50,000 dollars annually. It was trained using a 1994 census dataset created for this exact purpose.

## Intended Use
>This model is intended for educational purposes only. This model is used for predicting whether someone makes more than 50,000 dollars based on additional factors such as education, employement-status, and native country.

## Training Data
link: https://archive.ics.uci.edu/dataset/20/census+income
>This model was trained using a dataset from the 1994 U.S. Census which is linked above for more information. It contains various datapoints such as a persons education, employement-status, age, and native country. The training data is an 80% portion of the full original dataset.

## Evaluation Data
>A 20% portion of the original dataset was used for testing purposes to evaluate the model.

## Metrics
This model's performance was measured using three primary indicators:

* Precision - measures the accuracy of positive  predictions.
* Recall - measures the models ability to correctly identify all positive instances.
* F1 - considers both precision and recall to give a balanced score for the models

The overall scoring concluded with:
Precision: 0.7227 | Recall: 0.6452 | F1: 0.6817

>scoring varied greatly depending on the categorical value. The highest scoring predictiors were those that gauranteed a correct prediction such as being unemployed, extreme young age, and a lack-of or low levels of education.


## Ethical Considerations
>The dataset used for training and validation may contain biases due to imbalances and disproportionate representation of different groups within the dataset. The model has not been thoroughly tested and any inferences made using this model should not be considered accurate without the use of additional tools and research.

## Caveats and Recommendations
>No inferences should be made using this model. The age of the training data combined with unknown and unintended biases likely has compromised the accuracy of any prediction made outside of using the original dataset.
