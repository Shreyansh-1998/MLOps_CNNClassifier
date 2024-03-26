## This is an END-to-END CNNClassifier with MLOps Project

To run this project :
1. ```
    git clone https://github.com/Shreyansh-1998/MLOps_CNNClassifier.git
   ```
2. ```
    conda create -n your_env python==3.8 -y
    ```
3. ```
    conda activate
   ```
4.  ```
    pip install -r requirements.txt
    ```
5.  ```
    python3 app.py
    ```

This project also contains Data Version Control(Dvc) for pipeline tracking to save computational power. It is integrated with Mlflow to track experiments using [Dagshub](https://dagshub.com/).

[MLflow tutorial and documentation](https://mlflow.org/)

Steps for dvc execution:
```dvc init
```
```
dvc dag
```
```
dvc repro
```
## The project also renders a flask application and hosts it locally.
1. [flask application would run on](http://localhost:8080)
2. Additional step would be to host it on AWS cloud with ci/cd.