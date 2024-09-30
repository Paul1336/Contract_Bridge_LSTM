# Demo Repository for Bridge Game Model Training

This repository is for demo usage. Follow the steps below to train your own model:

## Steps to Train Your Model

1. **Download Game History Data**  
   To download the bridge game history from BBO, run the following script:
   
   ```bash
   download_txt_2_csv_id
   ```

2. **Encode the Data**  
   After downloading the data, run the following script to encode your data:

   ```bash
   csv_2_csv_onehot_handfeature_cleaned
   ```

3. **Train the Model**  
   Finally, run the LSTM model tuning script and adjust the hyperparameters as needed:

   ```bash
   exp2_LSTM_tuning_0930
   ```

## Pretrained Model

Here is an example pretrained model:  
`083003_finalmodel.pgz`
