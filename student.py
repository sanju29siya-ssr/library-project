SET 1 – COMPLETE STEP-BY-STEP (START → END)
PART 1: Create Maven Project
Step 1: Go to working folder
Open terminal:
bash
cd Desktop 
Step 2: Create Maven project
mvn archetype:generate
 Enter:
GroupId: com.example
ArtifactId: number-utility-kit
Version: 1.0-SNAPSHOT
Package: com.example
Type:
```text
Y
Step 3: Move into project
```bash
cd number-utility-kit
```
---
 Step 4: Build project
bash
mvn clean install

BUILD SUCCESS
PART 2: Modify Code
 Step 5: Open in VS Code
```bash
code .
 Step 6: Go to file
```text
src → main → java → com → example → App.java
 Step 7: Replace code
```java
package com.example;
public class App {

    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= n/2; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public static int factorial(int n) {
        int fact = 1;
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }

    public static boolean isPalindrome(int n) {
        int temp = n, rev = 0;
        while (n > 0) {
            rev = rev * 10 + n % 10;
            n /= 10;
        }
        return temp == rev;
    }

    public static void main(String[] args) {
        System.out.println("Prime: " + isPrime(5));
        System.out.println("Factorial: " + factorial(5));
        System.out.println("Palindrome: " + isPalindrome(121));
    }
}
 Step 8: Build again
```bash
mvn clean install
```
---
 PART 3: Git Setup
 Step 9: Initialize Git
```bash
git init
 Step 10: Add files
```bash
git add .
 Step 11: Commit
```bash
git commit -m "Initial commit - Number Utility Kit"
 PART 4: Push to GitHub
 Step 12: Create repo on GitHub
* Click **New repository**
* Name:
```text
number-utility-kit
 Step 13: Connect & push
```bash
git remote add origin https://github.com/your-username/number-utility-kit.git
git branch -M main
git push -u origin main
```
 PART 5: Clone in VS Code (IMPORTANT STEP)
Step 14:
In VS Code:

* Press `Ctrl + Shift + P`
* Select:
```text
Git: Clone
```
* Paste GitHub URL
* Open project
 Step 15: Modify code again
Add one line:
```java
System.out.println("Updated version");
 Step 16: Push again
```bash
git add .
git commit -m "Updated code"
git push
 PART 6: Jenkins Pipeline
 Step 17: Open Jenkins
```text
http://localhost:8080
 Step 18: Create pipeline
* Click **New Item**
* Name:
```text
number-utility-pipeline
```
* Select Pipeline
 Step 19: Configure pipeline
Scroll → Pipeline → Script
Paste:
```groovy
pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/number-utility-kit.git'
            }
        }
        stage('Build') {
            steps {
                bat 'mvn clean compile'
            }
        }
        stage('Test') {
            steps {
                bat 'mvn test'
            }
        }
        stage('Package') {
            steps {
                bat 'mvn package'
            }
        }
    }
}
 Step 20: Run pipeline
Click:
```text
Build Now
 Step 21: Check output
✔ Console Output → must show:
```text
BUILD SUCCESS
