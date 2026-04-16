PART 1: Create Bio-Data Web Page (VS Code)
## Step 1: Create folder
Open terminal:
```bash
cd Desktop
mkdir biodata-app
cd biodata-app
 Step 2: Open in VS Code
```bash
code .
 Step 3: Create HTML file
In VS Code:
 Right click → New File
* Name:
index.html
Step 4: Write HTML code
Paste:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Bio Data</title>
</head>
<body>
    <h1>My Bio Data</h1>
    <p><b>Name:</b> Deeksha V</p>
    <p><b>Register Number:</b> 23BCT0221</p>
    <p><b>Department:</b> CSE</p>
    <p><b>Skills:</b> Java, Python, Web Development</p>
</body>
</html>
Save file.
 PART 2: Push to GitHub
 Step 5: Initialize Git
```bash
git init
git add .
git commit -m "Initial biodata page"
Step 6: Create repository on GitHub
* Click New Repository
* Name:
```
biodata-app
```
* Click Create
Step 7: Connect and push
```bash
git remote add origin https://github.com/your-username/biodata-app.git
git branch -M main
git push -u origin main
 PART 3: Docker (Containerization)
 Step 8: Create Dockerfile
In VS Code:
* New File
* Name:
```
Dockerfile
 Step 9: Add Dockerfile content
```dockerfile
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
 Step 10: Build Docker image

Open terminal:
```bash
docker build -t biodata-app .
 Step 11: Run container
```bash
docker run -d -p 8083:80 biodata-app
 Step 12: Verify in browser
Open:

http://localhost:8083
```
Your bio-data page should display.
# PART 4: Kubernetes (Deployment)
  Step 13: Ensure Kubernetes is running

Open Docker Desktop → Settings → Kubernetes
Make sure it shows:

Kubernetes is running
 Step 14: Create deployment file
Create file:

deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: biodata-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: biodata
  template:
    metadata:
      labels:
        app: biodata
    spec:
      containers:
      - name: biodata-container
        image: biodata-app
        ports:
        - containerPort: 80
 Step 15: Create service file
Create file:
```
service.yaml

Paste:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: biodata-service
spec:
  type: NodePort
  selector:
    app: biodata
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30007
Step 16: Apply Kubernetes files
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
Step 17: Check status
```bash
kubectl get pods
kubectl get services
 Step 18: Open application
```
http://localhost:30007
 PART 5: Jenkins (CI/CD Pipeline)
Step 19: Open Jenkins
http://localhost:8080
 Step 20: Create new pipeline
* Click New Item
* Name:
```
biodata-pipeline
```
* Select Pipeline
* Click OK
 Step 21: Configure pipeline

Scroll to Pipeline → Script and paste:
```groovy
pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/biodata-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t biodata-app .'
            }
        }
        stage('Run Container') {
            steps {
                bat 'docker run -d -p 8090:80 biodata-app'
            }
        }
        stage('Kubernetes Deploy') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
}
```
Click Save.
---

## Step 22: Run pipeline

Click:

```
Build Now
```

---

## Step 23: Verify output

Open:

```
http://localhost:30007
```

