import pandas as pd
from imblearn.under_sampling import RandomUnderSampler

# Load your dataset (replace with your data loading method)
# df = pd.read_csv('your_dataset.csv')

# Placeholder for demonstration (replace with actual data)
# df = pd.DataFrame({'features': range(43268), 'label': [0]*25000 + [1]*18268})

# Check original class distribution
print("Original class distribution:")
print(df['label'].value_counts())

# Define sampling strategy: 15,000 samples for each class
sampling_strategy = {0: 15000, 1: 15000}

# Apply RandomUnderSampler
rus = RandomUnderSampler(sampling_strategy=sampling_strategy, random_state=42)
X_res, y_res = rus.fit_resample(df.drop('label', axis=1), df['label'])

# Combine features and labels into a new DataFrame
reduced_df = pd.concat([pd.DataFrame(X_res, columns=df.drop('label', axis=1).columns), pd.Series(y_res, name='label')], axis=1)

# Verify new class distribution
print("\nBalanced reduced class distribution:")
print(reduced_df['label'].value_counts())

# Save the reduced dataset if needed
# reduced_df.to_csv('balanced_reduced_dataset.csv', index=False)