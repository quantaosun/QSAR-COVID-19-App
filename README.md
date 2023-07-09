# QSAR-COVID-19-App

## By providing a simple SMILES string, this app will give you a prediction of pIC50 of 3C-like protease.

- APP rebuild  by [Quantao Sun](https://github.com/quantaosun)
- App framework from `Python` + `Streamlit` by [Chanin Nantasenamat](https://medium.com/@chanin.nantasenamat) (aka [Data Professor](http://youtube.com/dataprofessor))
- Descriptor calculated using [PaDEL-Descriptor](http://www.yapcwsoft.com/dd/padeldescriptor/) [[Read the Paper]](https://doi.org/10.1002/jcc.21707).
- References 1 https://github.com/dataprofessor/bioactivity-prediction-app
- Reference 2 https://github.com/quantaosun/QSAR-COVID-19

**Only works on Linux, and Mac**

https://github.com/quantaosun/QSAR-COVID-19-App/assets/75652473/5f167897-e293-4c89-9da2-62cfcb992f50

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
<img width="1260" alt="image" src="https://github.com/quantaosun/QSAR-COVID-19-App/assets/75652473/dcc3674b-de1a-406d-b2db-51ea1cb37e64">

Next, you can click Upload a txt file containing the SMILES strings you want to predict, then click Predict will return the result at the bottom, you can upload as many as SMILES you like as long as the total txt file size is smaller than 200 M. The file format should be each line for each single molecule followed by a name without any space. You can name it whatever you like as long as the format is  .txt.
like,

``` c1ccccc1 benzene``` 

if you have two molecules

```
    c1ccccc1 Molecule1
    C1CCCCC1 Molecule2
```


