# Blue/Green Deployment of an App on Kubernetes Cluster using Helm and Spinnaker

A sample python flask application with a home page displaying "app version" and "hostname" and status page displaying "status response" would be dockerized and deployed on a kubernetes cluster with Helm and Spinnaker.

## Environment
1. Docker for Desktop on MAC Book
2. A simple Python Flask application
3. Kubernetes cluster created on "Docker for Desktop" app.
4. Local Helm Installation
5. Spinnaker deployed on local Kubernetes cluster with dedicated namespace and AWS S3 as backend data storage.

## Contents of the Repository
1. Dockerfile for the app - Dockerfile
2. Application code - sample-flask.py
3. Helm Packages under helm-charts folder
4. README.md file
5. kubernetes definition files under kubernetes-files
6. Screenshots


## Screenshots
![SampleFlask App Home Page](https://github.com/rokie582/kubernetes-demo/blob/master/Sample-Flask-app-home-page.png)
