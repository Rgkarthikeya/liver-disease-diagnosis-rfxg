# Liver Disease Diagnosis using RFXG Classifier 🧬

This project contains code, notebooks, and data used in a research paper on liver disease detection using a custom ensemble model: RFXG (Random Forest + XGBoost + GradientBoost).

## 🔬 Project Highlights

- Balanced dataset using under/over sampling
- Advanced preprocessing for better accuracy
- Overfitting control and model explanation
- Visualization and evaluation of results

## 📁 Files Overview

| File                              | Description                              |
|-----------------------------------|------------------------------------------|
| `)_over_fitting_preprossing.ipynb` | Overfitting reduction techniques         |
| `explanation_for_the_model (2).ipynb` | RFXG model explanation                  |
| `final_datase (1).ipynb`          | Final cleaned dataset                    |
| `from_non_eligible_to_eligibility (2).ipynb` | Logic to adjust label categories     |
| `holidays.csv`                    | Supplementary dataset                    |
| `preprocess_balancing.ipynb`      | Class balancing code                     |
| `preprocessing_dataset (2).ipynb` | Raw dataset cleaning                     |
| `reduction of dataset.py`         | Under-sampling script                    |
| `result_prediction.ipynb`         | Model result prediction                  |
| `results/`                        | Saved visualizations/output              |
| `visualization_balanced (2).ipynb`| Data visualization after balancing       |

## 🛠 Requirements

- Python 3.8+
- pandas
- scikit-learn
- imbalanced-learn
- xgboost
- matplotlib

Install them using:

```bash
pip install -r requirements.txt
