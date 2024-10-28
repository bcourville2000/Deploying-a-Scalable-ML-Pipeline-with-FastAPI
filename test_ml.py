import pytest
import pickle
import pandas as pd
from ml.model import compute_model_metrics
from train_model import y_test, preds
from sklearn.ensemble import RandomForestClassifier

def test_algo_type():
    """
    Simple test to check and ensure the algo type is the one specified
    """
    # Expected algorithm type. replace as necessary with the expected type 
    algorithm_type = RandomForestClassifier #change as necessary

    # Load pickle file with model.
    with open("model/model.pkl", "rb") as f:
        model = pickle.load(f)
    
    # Check if model matches expected algorithm type.
    assert isinstance(model, algorithm_type), print(f"expected algorithm: {algorithm_type} model algorithm: {type(model)}")

def test_metrics():
    """
    test to ensure the metrics produced are the expected ones for repeatability.
    """
    # compute metric values
    metrics = compute_model_metrics(y_test, preds)

    # round metric values to 3 places
    metrics = [round(i, 3) for i in metrics]
    
    #define expected values
    prec = 0.723 # Precision value produced by compute_model_metrics.
    rec = 0.645 # Recall value produced by compute_model_metrics.
    f1 = 0.682 # F1 value produced by compute_model_metrics.
    exp_vals = [prec, rec, f1]

    #compare metrics with expected values
    
    assert exp_vals == metrics, print(f"The expected metric values:{exp_vals} was not in the list of metrics:{metrics}")

def test_data_verify():
    """
    ensure the dataset contains the correct number of columns and the correct names for columns.
    """
    # define expected values in dataset
    num_cols = 15 # expected number of columns 
    csv_cols = [ #expected column names
        'age',
        'workclass',
        'fnlgt',
        'education',
        'education-num',
        'marital-status',
        'occupation',
        'relationship',
        'race',
        'sex',
        'capital-gain',
        'capital-loss',
        'hours-per-week',
        'native-country',
        'salary'
        ]
    
    #load csv
    df = pd.read_csv("data/census.csv")

    # compare number of columns
    assert len(df.columns) == num_cols, print(f"Expected number of columns: {num_cols} actual number of columns: {len(df.columns)}")

    #create list of column names from csv
    df_cols = list(df.columns.values)

    #compare column name lists
    assert df_cols == csv_cols, print("Column names do not match expected values!!!")
