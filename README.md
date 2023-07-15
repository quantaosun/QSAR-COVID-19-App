# QSAR-COVID-19-App

# Try it as a web app here https://sars-covid-3cl-prediciton.streamlit.app/ 

- App framework from `Python` + `Streamlit` by [Chanin Nantasenamat](https://medium.com/@chanin.nantasenamat) (aka [Data Professor](http://youtube.com/dataprofessor))
- Descriptor calculated using [PaDEL-Descriptor](http://www.yapcwsoft.com/dd/padeldescriptor/) [[Read the Paper]](https://doi.org/10.1002/jcc.21707).
- References 1 https://github.com/dataprofessor/bioactivity-prediction-app
- Reference 2 https://github.com/quantaosun/QSAR-COVID-19
- For convenience purposes, what is provided is actually SARS-COV 3C-like protease, not SARS-COV-2 due to a lack of enough datapoint for the latter. But it could be transformed into a COVID-19 model at any time when have enough data.

**Only works on Linux, and Mac**

https://github.com/quantaosun/QSAR-COVID-19-App/assets/75652473/5f167897-e293-4c89-9da2-62cfcb992f50

# Model training 
## Protein target
The model was built with 133 bioactivity data in the Chembl database in July 2023, with a random forest regression model.

<img width="998" alt="image" src="https://github.com/quantaosun/QSAR-COVID-19-App/assets/75652473/99d963f5-8e31-48c3-8802-c7118f6660d1">
Image from https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3927/
<img width="991" alt="image" src="https://github.com/quantaosun/QSAR-COVID-19-App/assets/75652473/038a4e1c-0a76-4d3d-9a46-e33e9d585983">
Image from https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL3927/

## Model Performance
```
model = RandomForestRegressor(n_estimators=500, random_state=42)
model.fit(X, Y)
r2 = model.score(X, Y)
r2
```
gives an r2 = 0.8635050710434334
## Predicted vs Experimental based on this model (note this is not an external prediction but all from the Chembl training set)
![image](https://github.com/quantaosun/QSAR-COVID-19-App/assets/75652473/99b008a7-3aa9-47d6-a635-749245aaf675)

# Run the app locally

pre-requirements

- streamlit
- sklearn

## Java needed 

### On Linux run 

```sudo apt install default-jdk```

It will go to PATH automatically
### On Mac, run
```brew install java``` 
and we need to put the path into PATH by
```
echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
Then download this repo to your local machine and enter it inside

```
git clone https://github.com/quantaosun/QSAR-COVID-19-App.git
cd QSAR-COVID-19-App.git
```
launch the app by
```
streamlit run app.py
```
Your browser will open an interface for the APP 

Next, you can click Upload a txt file containing the SMILES strings you want to predict, then click Predict will return the result at the bottom,  You can name it whatever you like as long as the format is  .txt.
like,

``` c1ccccc1 benzene``` 
You are advised to predict one molecule at one time for the moment.
# What happened after you clicked the predict button

- 1. The smiles will be converted into a binary string with 264 bits, the same length as our model expected
- 2. The binary string then will be allocated as variable matrix X
- 3. The X variable will be fed into our built model, and returns the Y value, which essentially is the pIC50
